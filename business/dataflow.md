# dataflow.md  

## 1. Overview  

The **Skill‑Graph** platform ingests heterogeneous AI‑skill artefacts, resolves their inter‑dependencies, materialises a **Directed Acyclic Graph (DAG)** and serves it to downstream tools (IDE plugins, CI pipelines, analytics dashboards). The data‑flow is split into six logical tiers, each with explicit authentication / authorization boundaries.

```
+-------------------+      +-------------------+      +-------------------+
| External Data     |      | Ingestion Layer   |      | Processing /      |
| Sources           |      | (API Gateway)     |      | Transform Layer   |
|                   |      |                   |      |                   |
|  • HuggingFace    | ---> |  • AuthN (API Key)| ---> |  • Skill Parser   |
|  • OpenAI / Azure |      |  • Rate‑Limiter   |      |  • Dep Resolver   |
|  • Git repos      |      |  • Queue (Kafka)  |      |  • Graph Builder  |
|  • User uploads   |      +-------------------+      |  • Enricher (LLM) |
+-------------------+                                 +-------------------+
          |                                                    |
          |                                                    v
          |                                           +-------------------+
          |                                           | Storage Tier      |
          |                                           |-------------------|
          |                                           |  • Graph DB (Neo4j)|
          |                                           |  • Metadata RDBMS |
          |                                           |  • Blob Store (S3) |
          |                                           |  • Cache (Redis)  |
          |                                           +-------------------+
          |                                                    |
          |                                                    v
          |                                           +-------------------+
          |                                           | Query / Serving   |
          |                                           | Layer             |
          |                                           |-------------------|
          |                                           |  • GraphQL API    |
          |                                           |  • REST Endpoints |
          |                                           |  • WebSocket Live |
          |                                           |  • AuthZ (OAuth2) |
          |                                           +-------------------+
          |                                                    |
          |                                                    v
          |                                           +-------------------+
          |                                           | Egress to User    |
          |                                           |-------------------|
          +------------------------------------------> |  • Web UI (React) |
                                                      |  • Export (JSON, |
                                                      |    GraphML, DOT) |
                                                      |  • Webhooks /     |
                                                      |    Slack alerts   |
                                                      +-------------------+
```

---

## 2. External Data Sources  

| Source | Type | Access Method | Typical Payload | Auth / AuthZ |
|--------|------|---------------|-----------------|--------------|
| **HuggingFace Model Hub** | Public model metadata & README | HTTPS GET (public) | Model ID, tags, config, license | API‑Key (optional for rate‑limit) |
| **OpenAI / Azure OpenAI** | LLM instruction sets, fine‑tune specs | HTTPS (REST) | Prompt templates, system messages | Bearer token (service account) |
| **Git Repositories** (GitHub, GitLab, Bitbucket) | Skill code, README, CI configs | Git clone / API | `skill.yaml`, source files | OAuth2 (repo‑scoped token) |
| **User‑provided Skill Packages** | ZIP/JSON uploads via UI | Multipart POST | `skill.json`, assets | Session JWT (user) |
| **Internal Skill Registry** (Axentx BRAIN) | Canonical skill definitions | gRPC / internal API | Skill ID, version, lineage | mTLS + service‑to‑service token |
| **Knowledge Bases** (Wikipedia, DBpedia) | Semantic enrichment (domains, synonyms) | SPARQL / REST | Entity triples | API‑Key (public) |

*All external calls are wrapped by the **Ingestion API Gateway** which enforces rate‑limiting, request validation and logs audit trails.*

---

## 3. Ingestion Layer  

| Component | Responsibility | Tech Stack | Auth Boundary |
|-----------|----------------|------------|---------------|
| **API Gateway** | Entry point, request validation, authN (API‑Key / OAuth2), throttling | Kong / AWS API GW + Lambda authorizer | Public → Service‑account |
| **Ingress Queue** | Decouples ingestion from processing, guarantees at‑least‑once delivery | Apache Kafka (topic: `skill_ingest`) | Service‑to‑service IAM role |
| **Ingestion Workers** | Pull messages, fetch remote artefacts, normalise payloads, store raw blobs | Python (FastAPI) + `requests` library | Service account with scoped permissions |
| **Blob Store** | Raw artefacts (ZIP, PDFs, model binaries) for audit & re‑processing | Amazon S3 (bucket `skill-graph-raw`) | IAM role `ingest-worker` (write) |

*All traffic inside this tier is protected by **mutual TLS** and **IAM‑based RBAC**.*

---

## 4. Processing / Transform Layer  

| Sub‑system | Function | Tech / Libraries | Auth Boundary |
|------------|----------|------------------|---------------|
| **Skill Parser** | Extract skill definition (name, inputs, outputs, version) from raw artefacts | `pyyaml`, `tree-sitter` for code parsing | Internal service token |
| **Dependency Resolver** | Detect explicit `requires` clauses, infer implicit dependencies via LLM similarity | Graph algorithms (NetworkX), OpenAI embeddings | Internal |
| **Graph Builder** | Assemble validated DAG, enforce acyclicity, compute topological order | Neo4j Python driver, custom DAG validator | Internal |
| **Enricher (LLM)** | Generate semantic tags, risk scores, compatibility hints | OpenAI `gpt‑4o-mini` via internal proxy | Service‑to‑service token |
| **Validator** | Run policy checks (e.g., no circular deps, version constraints) | JSON‑Schema, custom rule engine | Internal |
| **Change Detector** | Diff against previous version, emit events for downstream pipelines | `deepdiff`, Kafka producer (`skill_graph_updates`) | Internal |

All processing nodes run in a **Kubernetes** namespace `skill-graph-processing` with **Pod‑level RBAC** limiting access to the Graph DB and the Blob Store.

---

## 5. Storage Tier  

| Store | Purpose | Engine | Access Pattern | AuthZ |
|------|---------|--------|----------------|------|
| **Graph DB** | Persistent DAG, node/edge properties, traversal queries | Neo4j Aura (Causal Clustering) | Cypher reads/writes | Neo4j RBAC (role `graph_admin`) |
| **Metadata RDBMS** | Skill version history, audit logs, user permissions | PostgreSQL (RDS) | SQL CRUD | IAM role `db_rw` |
| **Blob Store** (raw & generated artefacts) | Original uploads, generated visualisations (SVG/PNG) | Amazon S3 (`skill-graph-artifacts`) | GET/PUT via pre‑signed URLs | IAM policies per bucket prefix |
| **Cache** | Hot DAG fragments, auth sessions | Redis (Elasticache) | GET/SET with TTL | Security group isolation, TLS‑in‑transit |

All storage endpoints enforce **encryption at rest** and **TLS 1.3** in transit. Access is mediated by **AWS IAM** roles or **Neo4j RBAC**.

---

## 6. Query / Serving Layer  

| Service | API | Rate Limits | AuthZ |
|---------|-----|-------------|-------|
| **GraphQL API** | `/graphql` – flexible queries (sub‑graph, lineage, risk) | 200 req/s per client | OAuth2 JWT scopes (`skill:read`) |
| **REST Endpoints** | `/v1/skills/{id}`, `/v1/graph/export` | 100 req/s | Same JWT scopes |
| **WebSocket Live** | Real‑time DAG updates for UI editors | 50 concurrent sockets per user | JWT + per‑socket token |
| **AuthZ Service** | Centralised policy engine (OPA) | – | Evaluates JWT claims against resource ACLs |

The serving layer runs behind an **API Management** layer (e.g., Kong) that terminates TLS, injects request IDs, and forwards to the backend services. All outbound responses are **signed** (JWT `kid`) to enable client‑side verification.

---

## 7. Egress to User  

| Channel | Format | Trigger | Auth |
|---------|--------|---------|------|
| **Web UI** (React + D3.js) | Interactive SVG/Canvas DAG | On‑load / user navigation | Session JWT (httpOnly cookie) |
| **Export Service** | JSON (SkillGraph v2), GraphML, DOT | User‑initiated download | Same JWT |
| **Webhooks** | POST JSON payload to user‑registered endpoint | DAG change events, validation failures | HMAC signature (`X-SkillGraph-Sig`) |
| **Slack / Teams Bot** | Message with summary + link | Critical policy breach | Bot token (app‑level) |
| **CLI** (`sgctl`) | Terminal output, JSON pipe | CI/CD integration | Personal access token (PAT) |

All egress channels respect **CORS** policies, enforce **same‑origin** checks for the UI, and include **audit logs** in the Metadata DB.

---

## 8. Security & Compliance Summary  

| Layer | Primary Controls |
|-------|-------------------|
| **External** | API‑Key validation, OAuth2 scopes, rate limiting |
| **Ingestion** | mTLS, IAM role‑based write access, immutable raw blobs |
| **Processing** | Namespace isolation, least‑privilege service accounts, runtime scanning (Trivy) |
| **Storage** | Encryption‑at‑rest, RBAC (Neo4j, PostgreSQL), bucket policies |
| **Serving** | OPA policy enforcement, JWT validation, audit logging |
| **Egress** | Signed payloads, HMAC verification for webhooks, CSRF tokens for UI |

---  

*End of `dataflow.md`.*