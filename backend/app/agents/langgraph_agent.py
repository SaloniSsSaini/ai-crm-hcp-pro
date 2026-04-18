from langgraph.graph import StateGraph
from app.tools.log_interaction import log_interaction
from app.tools.suggestion_tool import suggest
from app.tools.sentiment_tool import analyze_sentiment
from app.tools.memory_tool import load_memory

def build_agent():
    graph = StateGraph(dict)

    graph.add_node("memory", load_memory)
    graph.add_node("log", log_interaction)
    graph.add_node("sentiment", analyze_sentiment)
    graph.add_node("suggest", suggest)

    graph.set_entry_point("memory")

    graph.add_edge("memory", "log")
    graph.add_edge("log", "sentiment")
    graph.add_edge("sentiment", "suggest")

    return graph.compile()