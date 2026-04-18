from typing import TypedDict, Optional, List, Dict, Any


class AgentState(TypedDict, total=False):
    # 🔹 user input
    input: str

    # 🔹 parsed structured output from LLM
    parsed: Optional[Dict[str, Any]]

    # 🔹 sentiment result
    sentiment: Optional[str]

    # 🔹 AI suggestions
    suggestions: Optional[str]

    # 🔹 memory (previous interactions)
    memory: Optional[List[Dict[str, Any]]]

    # 🔹 final response
    output: Optional[Dict[str, Any]]

    # 🔹 metadata (future scaling)
    metadata: Optional[Dict[str, Any]]