# ROADMAP.md

## Skill-Graph: A Dynamic Skill Inventory for Validated Product Development

A centralized, graph-based system to map skills to roles, projects, and validate workforce needs. The skill-graph enables HR/BD to scout demand, PMs to align specs with skill availability, and engineers to plan resource allocation—ultimately ensuring products are built by validated, in-demand talent without redundancy.

---

## 1. MVP (Minimum Viable Product) — Launch Ready

The MVP focuses on foundational skill modeling and basic search capabilities to validate the core concept. All items marked **MVP-CRITICAL** are non-negotiable for launch.

### MVP Milestones
- **Skill Model Definition**  
  - Define a skill as a node with:  
    - `name` (e.g., "Python", "C++", "System Design")  
    - `description` (e.g., "Proficient in Python 3.11 and data structures")  
    - `tags` (e.g., "backend", "data", "core")  
    - `metadata` (e.g., "required for 80% of SDE roles")  

- **Skill Import & Management**  
  - Import skills via CSV or API (supports existing datasets like `instr-resp`, `messages`).  
  - CRUD operations for skills (create, read, update, delete).  

- **Basic Search & Discovery**  
  - Search skills by name, tag, or description (e.g., "search: 'backend'").  
  - Filter skills by license (e.g., "apache-2.0", "mit").  

- **Role-Skill Association**  
  - Associate a role (e.g., "Senior Software Engineer") with a skill (e.g., "Python").  
  - Track usage metrics (e.g., "used in 12 products").  

- **Data Validation**  
  - Ensure no duplicate skills are added (via hash comparison).  
  - Validate skill names against existing datasets (e.g., `auto`, `query-resp`).  

### MVP-Critical Items
- Skill model definition  
- CSV import functionality  
- Basic search API  
- Role-skill association  

---

## 2. v1 Phase — Graph & Integration

Build on the MVP with interactive graph features and integration with HR/BD systems to enhance collaboration and resource planning.

### v1 Milestones
- **Interactive Graph Visualization**  
  - Render a graph of skills and roles using a web-based UI (e.g., D3.js or vis.js).  
  - Highlight relationships (e.g., "Python → Data Science", "System Design → Iceoryx2").  

- **Role-Skill Matching Engine**  
  - Suggest skills for a given role based on historical data (e.g., "Software Engineer" → "Python", "C++", "
