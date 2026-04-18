from app.utils.llm_client import call_llm

def log_interaction(state):
    text = state["input"]

    prompt = f"""
    Extract JSON:
    hcp_name, summary, sentiment, follow_up
    Input: {text}
    """

    result = call_llm(prompt)
    return {"parsed": result}