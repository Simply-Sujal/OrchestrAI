from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict
from dotenv import load_dotenv
import os
load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY_9")
model = os.getenv("GOOGLE_GEMINI_MODEL")

llm = ChatGoogleGenerativeAI(model=model, api_key=google_api_key)

class GraphState(TypedDict):
    question: str
    answer: str

def greet(state: GraphState):
    qst = state["question"]
    prompt = f"""
        Answer the following question asked by the user {qst}, in a one liner sentence strictly in a more technical way.
    """
    result = llm.invoke(prompt)
    return {"answer": result.content}

workflow = StateGraph(state_schema=GraphState)

workflow.add_node("greet", greet)
workflow.add_edge(START, "greet")
workflow.add_edge("greet", END)


app = workflow.compile()

input = {"question": "What are proxy servers ?"}

final_output = app.invoke(input)

print(final_output["answer"])




