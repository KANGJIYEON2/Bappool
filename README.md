# 아키텍처 초안
User
  ↓ (웹/앱)
Frontend (Next.js)
  ↓ HTTP / WebSocket
Backend API (FastAPI)
  ↓
Core Engine
  ├─ User Profiler
  │     └─ Body Type Classifier (Underweight / Normal / Obese / Athlete)
  │
  ├─ Environment Factory
  │     └─ Physiology Environment (4 types)
  │           ├─ Metabolic Dynamics
  │           ├─ 3-Comp Model (Fat/Lean/Water)
  │           ├─ Hunger & Binge Model
  │           └─ Adaptive Thermogenesis
  │
  ├─ Simulator Engine
  │     └─ Daily/Weekly State Transition Model
  │
  ├─ RL PlannerAgent (PPO/PG 기반)
  │     └─ Action Space: kcal / macros / exercise / refeed / scheduling
  │     └─ Reward: fat loss / lean preservation / adherence / safety
  │
  ├─ Safety Rule Engine
  │     ├─ Medical Rules (calorie floor, lean-mass protection)
  │     ├─ Risk Rules (ED-risk, binge-risk)
  │     ├─ Phase Rules (PMS, recovery)
  │     └─ Athlete Rules
  │
  ├─ Vision Pipeline (YOLO + SAM)
  │     ├─ Food detection
  │     ├─ Portion estimation
  │     └─ Macro & kcal extraction
  │
  ├─ Multi-Agent Orchestrator
  │     ├─ RouterAgent
  │     ├─ PlateauAgent
  │     ├─ PlannerAgent
  │     ├─ SafetyAgent
  │     ├─ SimulatorAgent
  │     ├─ ReportAgent
  │     └─ MemoryAgent (Long-term adherence memory)
  │
  ├─ RAG System
  │     ├─ Nutrition DB
  │     ├─ Sports Science Papers
  │     ├─ Physiology Articles
  │     └─ “WHY Explanation Generator”
  │
  └─ Logging & Monitoring
        ├─ Weight trajectory
        ├─ Environmental params
        ├─ Agent decisions
        └─ Safety events

↓  
PostgreSQL DB
  ├─ user_profile
  ├─ body_type_params
  ├─ simulation_logs
  ├─ agent_actions
  ├─ reward_history
  ├─ vision_results
  ├─ rag_sources
  └─ safety_events
