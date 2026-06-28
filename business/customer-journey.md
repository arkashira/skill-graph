# customer-journey.md  

**Product:** *skill‑graph* – Visual AI‑skill dependency manager that auto‑generates a Directed Acyclic Graph (DAG) of LLM‑prompt/skill relationships.  

**Target persona:** AI/ML Engineer, Prompt Engineer, AI Product Manager (mid‑size to enterprise AI teams).  

---  

## 1️⃣ AWARE  

| Element | Detail |
|---------|--------|
| **Trigger event** | • Reads a blog post / LinkedIn article about “Why AI pipelines break when prompts evolve”. <br>• Attends a conference session on “Scaling LLM‑driven products”. |
| **Friction points** | • Over‑abundance of generic static‑analysis tools (SonarQube, CodeQL) that don’t map LLM skill dependencies. <br>• No clear terminology for “AI skill graph”. |
| **User emotions** | Curiosity → Mild frustration (can’t find a solution). |
| **Opportunities to delight** | • Publish a **“State of AI Skill Dependency”** whitepaper (1‑page) with industry stats (e.g., 42 % of AI teams report >30 % downtime due to hidden skill coupling). <br>• Release a **short explainer video** (≤90 s) showing a live DAG being built from a sample prompt library. |
| **Metric** | **Impression‑to‑click rate** on awareness assets (target ≥ 8 %). |

---  

## 2️⃣ CONSIDER  

| Element | Detail |
|---------|--------|
| **Trigger event** | • Clicks the whitepaper/video and lands on the skill‑graph landing page. <br>• Sees a **“Free Dependency Audit”** offer (upload 10 prompt files, get a DAG preview). |
| **Friction points** | • Uncertainty about data privacy (prompt content may be proprietary). <br>• Lack of integration details with existing CI/CD / MLOps stacks. |
| **User emotions** | Analytical → Cautious optimism. |
| **Opportunities to delight** | • Provide a **one‑click “sandbox demo”** that runs entirely in‑browser (no data leaves the user). <br>• Publish a **comparative matrix** vs. static‑analysis tools, highlighting unique AI‑skill coverage. <br>• Offer a **risk‑free SLA**: “Your prompts never leave your network – we run the graph generator locally.” |
| **Metric** | **Landing‑page conversion** (audit‑request submit) **≥ 12 %** of visitors. |

---  

## 3️⃣ TRY  

| Element | Detail |
|---------|--------|
| **Trigger event** | • Receives the auto‑generated DAG preview (PDF/interactive). <br>• Email invites user to start a **14‑day free trial** with full integration (GitHub, Azure Pipelines, LangChain). |
| **Friction points** | • Setup time (installing CLI, connecting repos). <br>• Learning curve of the visual editor. |
| **User emotions** | Excitement → Slight anxiety (will it actually save time?). |
| **Opportunities to delight** | • **One‑click onboarding wizard** that detects existing prompt files and auto‑creates the graph. <br>• **In‑app guided tour** with contextual tooltips (“Click a node to see downstream impact”). <br>• **Dedicated 30‑min onboarding call** for teams >5 members (optional but high‑impact). |
| **Metric** | **Trial activation rate** (users who complete onboarding) **≥ 30 %** of audit‑requesters. |

---  

## 4️⃣ ADOPT  

| Element | Detail |
|---------|--------|
| **Trigger event** | • First successful CI run where skill‑graph blocks a breaking change (e.g., “Prompt X removed, downstream Y fails”). <br>• Team sees measurable reduction in pipeline roll‑backs. |
| **Friction points** | • Pricing perception (enterprise tier vs. budget). <br>• Need for role‑based access control and audit logs. |
| **User emotions** | Confidence → Satisfaction (real ROI). |
| **Opportunities to delight** | • **ROI calculator** embedded in the UI (e.g., “Saved 4 hrs/week = $X/month”). <br>• **Customizable policy templates** (e.g., “Never allow removal of core skill nodes”). <br>• **Early‑adopter badge** & **public case‑study spotlight** for teams that publish results. |
| **Metric** | **Paid conversion** (trial → paid) **≥ 60 %** within 30 days of first block event. |

---  

## 5️⃣ EXPAND  

| Element | Detail |
|---------|--------|
| **Trigger event** | • Organization adds new AI domains (e.g., vision + language) and wants a unified dependency view. |
| **Friction points** | • Scaling the graph to >10 k nodes may impact performance. <br>• Need for cross‑team governance (multiple product groups). |
| **User emotions** | Empowered → Expectation of continued value. |
| **Opportunities to delight** | • **Enterprise‑scale clustering** (horizontal graph rendering) released as a free upgrade for existing customers. <br>• **Marketplace of community‑built skill modules** (plug‑and‑play). <br>• **Quarterly health‑check webinars** showing emerging dependency patterns and recommending refactors. |
| **Metric** | **Expansion revenue** (upsell to Enterprise tier or add‑on modules) **≥ 20 %** of existing ARR within 90 days post‑adoption. |

---  

### Summary of Success Metrics  

| Phase | Primary KPI | Target |
|-------|-------------|--------|
| Aware | Impression‑to‑click | ≥ 8 % |
| Consider | Audit‑request conversion | ≥ 12 % |
| Try | Trial activation | ≥ 30 % |
| Adopt | Paid conversion (within 30 d) | ≥ 60 % |
| Expand | Expansion ARR (90 d) | ≥ 20 % of existing ARR |

These metrics, combined with the emotional and friction insights above, give a concrete roadmap for turning **skill‑graph** from a novel concept into a revenue‑validated product line.  