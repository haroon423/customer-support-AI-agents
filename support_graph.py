import os
from typing import TypedDict

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.runnables import RunnableLambda
from langgraph.graph import StateGraph, END

from langchain_groq import ChatGroq

load_dotenv()  # Load your GROQ_API_KEY from .env

# Define schema for state
class GraphState(TypedDict):
    question: str
    response: str

# Define your Groq LLM
llm = ChatGroq(temperature=0, model="llama3-8b-8192")

# Node that answers the question
def answer_question(state: GraphState) -> GraphState:
    question = state["question"]
    chat_response = llm.invoke([
        HumanMessage(content=question)
    ])
    return {
        "question": question,
        "response": chat_response.content
    }

# Build LangGraph
graph_builder = StateGraph(GraphState)
graph_builder.add_node("answer", RunnableLambda(answer_question))
graph_builder.set_entry_point("answer")
graph_builder.set_finish_point("answer")

support_graph = graph_builder.compile()
