## 🧠 Architecture Overview

```text
User Request
   ↓
API Layer (FastAPI)
   ↓
Engine (Orchestrator)
   ├─ Dispatcher (Body Type)
   ├─ Agents (Planner / Rule)
   ├─ RAG (Retriever + Context)
   └─ Vision Pipeline
   ↓
Response
   ↓
PostgreSQL (Logs / State)
```
---
## 📁 Directory Structure

- api/      : External API entrypoint
- engine/   : Request orchestration
- agents/   : Reasoning agents
- rag/      : Retrieval & grounding
- vision/   : Multimodal processing
- schemas/  : Request contracts
- database/ : Persistence layer
