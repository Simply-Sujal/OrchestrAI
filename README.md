# 🎯 OrchestrAI

> Transform ideas into actionable projects with AI-powered automation

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![LangChain](https://img.shields.io/badge/LangChain-Powered-green.svg)](https://www.langchain.com/)

**OrchestrAI** is an intelligent, multi-agent system that transforms high-level ideas into structured, actionable project blueprints. It helps project managers, founders, and teams move seamlessly from concept → PRD → project plan → ready-to-execute tasks in Asana, all through automation and AI orchestration.

---

## 📋 Table of Contents

- [Problem Statement](#-problem-statement)
- [Who Is This For?](#-who-is-this-for)
- [What It Does](#-what-it-does)
- [Core Agents](#-core-agents)
- [Key Features](#-key-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Setup & Installation](#-setup--installation)
- [Asana Configuration](#-asana-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Vision](#-vision)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Problem Statement

Project managers and teams often struggle with:

- 🔄 **Turning vague ideas into actionable plans** — Ideas remain abstract without clear structure
- 📊 **Structuring projects, tasks, and subtasks efficiently** — Manual planning is time-consuming
- 🔗 **Maintaining consistency** across documentation and planning tools
- ⚡ **Moving quickly from concept to execution** — Traditional workflows create bottlenecks

**OrchestrAI eliminates these bottlenecks** by acting as an AI product architect — automatically designing project structures that are complete, organized, and ready for execution in Asana.

---

## 👥 Who Is This For?

- **Project Managers** — Automate project planning and task breakdown
- **Product Managers** — Generate PRDs and structured roadmaps instantly
- **Startup Founders** — Quickly scope and plan new product ideas
- **Development Teams** — Get organized task lists ready for sprint planning
- **Anyone** with an idea who wants to see it structured into an actionable plan

---

## ✨ What It Does

### 1️⃣ **User Input → AI Understanding**
- User provides a simple idea or topic (e.g., *"Build a todo list application"*)
- OrchestrAI's **PRD Architect** analyzes it, understands requirements, and generates a well-structured **Product Requirements Document (PRD)**

### 2️⃣ **PRD → Project Structure**
- The generated PRD is passed to the **Project Planner**
- Project Planner breaks it down into **Tasks** and **Subtasks** with:
  - Clear descriptions
  - Priority levels
  - Estimated hours
  - Tags for organization
  - Frequency indicators

### 3️⃣ **Automated Task Creation in Asana**
- OrchestrAI automatically pushes all tasks and subtasks to your **Asana workspace**
- Tasks are organized in your specified project with all metadata preserved
- Complete traceability from idea to execution

---

## 🤖 Core Agents

| Agent | Responsibility | Output |
|-------|---------------|--------|
| **PRD Architect** | Converts a topic or idea into a structured Product Requirements Document | PRD Text |
| **Project Planner** | Converts PRD into typed Tasks with subtasks, priorities, and estimates | Structured Task List |
| **Task Pusher** | Pushes tasks to Asana with all metadata (priority, tags, hours, etc.) | Asana Tasks |

---

## 🚀 Key Features

- ✅ **AI-Powered PRD Generation** — Leverages Google Gemini for intelligent document creation
- ✅ **Structured Task Planning** — Type-safe task generation with Pydantic models
- ✅ **Asana Integration** — Automatic task creation with full metadata support
- ✅ **Rich Task Metadata** — Priority, tags, estimated hours, frequency, assignees
- ✅ **Hierarchical Tasks** — Main tasks with subtasks for detailed breakdown
- ✅ **Real-time Progress Tracking** — Step-by-step workflow visibility
- ✅ **Extensible Architecture** — Easy to add new project management tools (Jira, ClickUp, etc.)

---

## 🏗️ Architecture

OrchestrAI uses a **multi-agent workflow** powered by LangGraph:

```
User Input
    ↓
┌─────────────────┐
│  PRD Architect  │ → Generates structured PRD
└────────┬────────┘
         ↓
┌─────────────────┐
│ Project Planner │ → Creates typed Tasks with Subtasks
└────────┬────────┘
         ↓
┌─────────────────┐
│  Task Pusher    │ → Pushes to Asana with metadata
└────────┬────────┘
         ↓
   Asana Project
```

### Workflow Components:
- **State Management**: TypedDict-based state graph
- **Typed Models**: Pydantic models for type safety
- **Helper Functions**: Reusable task body builder for Asana API
- **Factory Pattern**: Extensible adapter system for multiple PM tools

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| **AI Framework** | LangChain, LangGraph |
| **LLM** | Google Gemini 2.5 Pro |
| **Type Safety** | Pydantic |
| **Project Management** | Asana API |
| **Python** | 3.10+ |
| **Environment** | python-dotenv |

---

## 📦 Setup & Installation

### Prerequisites
- Python 3.10 or higher
- Google Gemini API key
- Asana account with API access

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/OrchestrAI.git
cd OrchestrAI
```

### 2. Create Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:

```env
# Google Gemini Configuration
GOOGLE_API_KEY_9=your_google_gemini_api_key_here
GOOGLE_GEMINI_MODEL="gemini-2.5-pro"

# Project Management Tool
PROJECT_MANAGEMENT_TOOL="ASANA"

# Asana Configuration
ASANA_ACCESS_TOKEN="your_asana_access_token_here"
ASANA_WORKSPACE_GID="your_workspace_gid_here"
ASANA_PROJECT_GID="your_project_gid_here"
```

---

## 🔑 Asana Configuration

### Step 1: Get Your Asana Access Token

1. **Log in to Asana** at [app.asana.com](https://app.asana.com)

2. **Navigate to Developer Console**:
   - Click on your **profile photo** in the top right
   - Select **"My Settings"**
   - Go to the **"Apps"** tab
   - Scroll down to **"Developer apps"**

3. **Create a Personal Access Token**:
   - Click **"Create new token"**
   - Enter a description (e.g., "OrchestrAI Integration")
   - Click **"Create token"**
   - **IMPORTANT**: Copy the token immediately (it won't be shown again!)

4. **Add to `.env`**:
   ```env
   ASANA_ACCESS_TOKEN="2/1234567890/abcdef123456:your_token_here"
   ```

### Step 2: Get Your Workspace GID

**Option A: Using the Debug Script** (Easiest)
```bash
python -c "
import asana, os
from dotenv import load_dotenv
load_dotenv()
config = asana.Configuration()
config.access_token = os.getenv('ASANA_ACCESS_TOKEN')
api_client = asana.ApiClient(configuration=config)
workspace_api = asana.WorkspacesApi(api_client=api_client)
workspaces = list(workspace_api.get_workspaces({}))
for ws in workspaces:
    print(f'Workspace: {ws[\"name\"]} | GID: {ws[\"gid\"]}')
"
```

**Option B: Using Asana Web UI**
1. Go to [app.asana.com](https://app.asana.com)
2. Look at the URL: `https://app.asana.com/0/1234567890/list`
3. The first number after `/0/` is your workspace GID

**Option C: Using Asana API Explorer**
1. Visit [Asana API Explorer](https://developers.asana.com/reference/getworkspaces)
2. Click "Try it" and authenticate
3. Your workspace GID will be in the response

4. **Add to `.env`**:
   ```env
   ASANA_WORKSPACE_GID="1208111540799808"
   ```

### Step 3: Get Your Project GID

**Option A: From Asana Web UI** (Easiest)
1. Open your desired project in Asana
2. Look at the URL: `https://app.asana.com/0/1234567890/9876543210`
3. The last number is your **project GID**

**Option B: Using the Debug Script**
```bash
python -c "
import asana, os
from dotenv import load_dotenv
load_dotenv()
config = asana.Configuration()
config.access_token = os.getenv('ASANA_ACCESS_TOKEN')
api_client = asana.ApiClient(configuration=config)
projects_api = asana.ProjectsApi(api_client=api_client)
workspace_gid = os.getenv('ASANA_WORKSPACE_GID')
projects = list(projects_api.get_projects({'workspace': workspace_gid}))
for proj in projects:
    print(f'Project: {proj[\"name\"]} | GID: {proj[\"gid\"]}')
"
```

4. **Add to `.env`**:
   ```env
   ASANA_PROJECT_GID="1211682077640154"
   ```

### Step 4: Verify Configuration

Run this verification script:
```bash
python -c "
import os
from dotenv import load_dotenv
load_dotenv()
print('✅ Configuration Check:')
print(f'Google API Key: {'✅' if os.getenv('GOOGLE_API_KEY_9') else '❌'} Set')
print(f'Asana Token: {'✅' if os.getenv('ASANA_ACCESS_TOKEN') else '❌'} Set')
print(f'Workspace GID: {'✅' if os.getenv('ASANA_WORKSPACE_GID') else '❌'} Set')
print(f'Project GID: {'✅' if os.getenv('ASANA_PROJECT_GID') else '❌'} Set')
"
```

---

## 🎮 Usage

### Basic Usage

```bash
python main.py
```

### Expected Output

```
============================================================
🎯 OrchestrAI Workflow Started
============================================================

📝 Generating PRD...
✅ PRD Generated Successfully

📋 Planning Tasks...
✅ Generated 8 Tasks Successfully

🚀 Pushing Tasks to Asana...

============================================================
✅ Successfully created 34 tasks in Asana
============================================================
```

### Customizing Input

Edit `main.py` to change the project idea:

```python
input = {"user_input": "create a mobile app for fitness tracking"}
```

### Generated Files

After running, you'll find:
- `prd_text.txt` — The generated PRD
- `project_plan.json` — Structured task breakdown with full metadata

---

## 📁 Project Structure

```
OrchestrAI/
├── adapter/                    # Project management adapters
│   ├── asana/
│   │   ├── asana.py           # Asana adapter implementation
│   │   ├── service.py         # Asana API service
│   │   └── helper.py          # Task body builder helper
│   ├── base_adapter.py        # Base adapter interface
│   ├── types.py               # Pydantic models (Task, Subtask, ProjectPlan)
│   └── tracking_tool_factory.py
├── prompts/                   # LLM prompts
│   ├── prd_generator_prompt.py
│   └── project_planner_prompt.py
├── tools/                     # Agent tools
│   └── prd_generator_tool.py # PRD, Planning, and Push tools
├── main.py                    # Entry point
├── requirements.txt           # Dependencies
├── .env                       # Configuration (create this)
├── .env.example              # Example configuration
└── README.md                 # This file
```

---

## 🌟 Vision

> **"To empower every project manager and product team with an AI that can think, plan, and orchestrate ideas into execution."**

We envision a future where:
- Ideas transform into execution-ready plans in minutes, not days
- AI handles the tedious parts of project planning
- Teams can focus on building, not planning
- Project management becomes truly intelligent and automated

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Areas for Contribution
- 🔧 Add support for more PM tools (Jira, ClickUp, Monday.com)
- 🎨 Improve prompts for better task generation
- 📊 Add analytics and reporting features
- 🧪 Write tests for better code coverage
- 📝 Improve documentation

---

## 🐛 Troubleshooting

### Common Issues

**Issue**: `WorkspacesApi.get_workspaces() missing 1 required positional argument`
- **Solution**: Make sure you've pulled the latest code with the fixed Asana API calls

**Issue**: Tasks created but not visible in Asana
- **Solution**: Check that `ASANA_PROJECT_GID` is set in `.env` and points to a valid project

**Issue**: Google API quota exceeded
- **Solution**: Wait for the rate limit to reset or upgrade your Gemini API plan

**Issue**: ImportError for `adapter.types`
- **Solution**: Make sure you're running from the project root directory

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **LangChain Team** for the amazing framework
- **Google** for Gemini API
- **Asana** for their robust API
- **Open Source Community** for inspiration and support

---

## 📞 Contact & Support

- **Issues**: [GitHub Issues](https://github.com/your-username/OrchestrAI/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-username/OrchestrAI/discussions)
- **Email**: your.email@example.com

---

<div align="center">

**Made with ❤️ by the OrchestrAI Team**

⭐ **Star this repo** if you find it helpful!

</div>
