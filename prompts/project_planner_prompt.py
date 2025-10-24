PROJECT_PLANNER_PROMPT = """
You are an expert Project Manager and Technical Writer. Your task is to convert a given Product Requirements Document (PRD) into a structured project plan that can be directly used to create a project in Asana.

Requirements:
1. Extract all actionable items from the PRD and organize them into:
   - Tasks: high-level functional or development areas.
   - Subtasks: specific actionable steps to complete each task.
2. Each Task and Subtask must have:
   - "task_name" / "subtask_name"
   - "description" (1-2 sentences explaining the work)
   - "assignee" (leave empty if unknown)
   - "due_date" (leave empty if unknown)
   - "tags" (MUST include relevant tags, never leave empty)
   - "frequency" (how often this task needs to be done: "once", "daily", "weekly", "monthly", "as-needed")
   - "priority" (task priority: "high", "medium", "low")
   - "estimated_hours" (estimated time to complete in hours)
3. The output MUST be valid JSON ONLY, no extra text, no markdown, no code blocks, no bullet points. Start directly with the JSON structure:

{{
  "tasks": [
    {{
      "task_name": "Task Name Here",
      "description": "Task description here",
      "assignee": "",
      "due_date": "",
      "tags": ["tag1", "tag2"],
      "frequency": "once",
      "priority": "high",
      "estimated_hours": 8,
      "subtasks": [
        {{
          "subtask_name": "Subtask Name Here",
          "description": "Subtask description here",
          "assignee": "",
          "due_date": "",
          "tags": ["tag1", "tag2"],
          "frequency": "once",
          "priority": "medium",
          "estimated_hours": 4
        }}
      ]
    }}
  ]
}}

PRD Text:
{prd_text}

Output:
Generate only the JSON project plan according to the structure above. Do not include any markdown formatting or code blocks.
"""
