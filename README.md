# OrchestrAI

OrchestrAI is an intelligent, multi-agent system that transforms high-level ideas into structured, actionable project blueprints.It helps project managers, founders, and teams move seamlessly from concept, PRD, project plan to ready-to-execute tasks, all through automation and AI orchestration.

# Problem It Solves ?

1. Project managers often struggle with:
    -Turning vague ideas into actionable plans
    -Structuring projects, epics, and issues efficiently
    -Maintaining consistency across documentation and planning tools

2. OrchestrAI eliminates this bottleneck by acting as an AI product architect — automatically designing project structures that are complete, organized, and ready for execution.

# This is for whom ?

This is for project managers, founders, and teams who want to move seamlessly from concept, PRD, project plan to ready-to-execute tasks, all through automation and AI orchestration.

# What it does ?
1. User Input → AI Understanding
    -The user provides a simple idea or topic (e.g., “Build a CRM for schools”).
    -OrchestrAI’s PRD Architect analyzes it, understands requirements, and generates a well-structured PRD (Product Requirements Document).

2. PRD → Project Structure
    -The generated PRD is passed to Project Planner.
    -Project Planner breaks it down into Projects, Epics, and Issues, with clear descriptions and dependencies.

3. Project Delivery
    -OrchestrAI automatically formats the PRD into a professional PDF document.
    -It can also push projects and issues directly to Jira (or other PM tools).
    -Finally, it emails the complete PRD and project breakdown to the user.

# Core Agents
    Agent		    Responsibility
    PRD Architect	Converts a topic or idea into a structured Product Requirements Document (PRD)
    Project Planner	Converts PRD text into Projects, Epics, and Issues (ready for Jira)
    Delivery Agent	Handles PDF creation, email dispatch, and API pushes

# Tech Stack 
1. Langchain
2. Langgraph
3. FastAPI 
4. FastMCP   
5. JIRA API

# How to run ?
1. Clone the repository
    -git clone https://github.com/your-repo/OrchestrAI.git
2. Install the dependencies
    -pip install -r requirements.txt
3. Run the application
    - python3 main.py


# Vision
    - “To empower every project manager and product team with an AI that can think, plan, and orchestrate ideas into execution.”

# License
    - MIT License