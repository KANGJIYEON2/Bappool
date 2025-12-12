## System Architecture 초안

## System Architecture

- User (Web / App)
  - Frontend (Next.js)
    - Communication
      - HTTP
      - WebSocket
    - Backend API (FastAPI)
      - Core Engine
        - User Profiler
          - Body Type Classifier
            - Underweight
            - Normal
            - Obese
            - Athlete

        - Environment Factory
          - Physiology Environment (4 types)
            - Metabolic Dynamics
            - 3-Comp Model (Fat / Lean / Water)
            - Hunger & Binge Model
            - Adaptive Thermogenesis

        - Simulator Engine
          - Daily / Weekly State Transition Model

        - RL PlannerAgent (PPO / Policy Gradient)
          - Action Space
            - kcal
            - macros
            - exercise
            - refeed
            - scheduling
          - Reward Function
            - Fat loss
            - Lean mass preservation
            - Adherence
            - Safety

        - Safety Rule Engine
          - Medical Rules
            - Calorie floor
            - Lean-mass protection
          - Risk Rules
            - ED-risk
            - Binge-risk
          - Phase Rules
            - PMS
            - Recovery
          - Athlete Rules

        - Vision Pipeline (YOLO + SAM)
          - Food detection
          - Portion estimation
          - Macro & kcal extraction

        - Multi-Agent Orchestrator
          - RouterAgent
          - PlateauAgent
          - PlannerAgent
          - SafetyAgent
          - SimulatorAgent
          - ReportAgent
          - MemoryAgent
            - Long-term adherence memory

        - RAG System
          - Nutrition DB
          - Sports Science Papers
          - Physiology Articles
          - WHY Explanation Generator

        - Logging & Monitoring
          - Weight trajectory
          - Environmental parameters
          - Agent decisions
          - Safety events

- PostgreSQL Database
  - user_profile
  - body_type_params
  - simulation_logs
  - agent_actions
  - reward_history
  - vision_results
  - rag_sources
  - safety_events

