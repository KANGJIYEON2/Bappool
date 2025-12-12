flowchart TB

User[User<br/>(Web / App)]
Frontend[Frontend<br/>(Next.js)]
Backend[Backend API<br/>(FastAPI)]
DB[(PostgreSQL)]

User --> Frontend
Frontend -->|HTTP / WebSocket| Backend

Backend --> CoreEngine

subgraph CoreEngine["Core Engine"]
  
  UserProfiler["User Profiler<br/>- Body Type Classifier"]
  
  EnvironmentFactory["Environment Factory"]
  PhysiologyEnv["Physiology Environment<br/>(4 Types)"]
  
  Simulator["Simulator Engine<br/>Daily / Weekly State Transition"]
  
  RLAgent["RL Planner Agent<br/>(PPO / PG)"]
  
  SafetyEngine["Safety Rule Engine"]
  
  Vision["Vision Pipeline<br/>(YOLO + SAM)"]
  
  Orchestrator["Multi-Agent Orchestrator"]
  
  RAG["RAG System"]
  
  Logging["Logging & Monitoring"]

end

UserProfiler --> EnvironmentFactory
EnvironmentFactory --> PhysiologyEnv
PhysiologyEnv --> Simulator

Simulator --> RLAgent
RLAgent --> SafetyEngine

Vision --> Orchestrator
RLAgent --> Orchestrator
SafetyEngine --> Orchestrator
Simulator --> Orchestrator
RAG --> Orchestrator

Orchestrator --> Logging

Backend --> DB
Logging --> DB
Vision --> DB
RAG --> DB
RLAgent --> DB
SafetyEngine --> DB
