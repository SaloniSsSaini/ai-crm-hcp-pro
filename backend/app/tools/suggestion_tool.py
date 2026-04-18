from app.utils.llm_client import call_llm

def suggest(state):
    return {
        "suggestions": call_llm(
            f"Suggest next steps: {state['input']}"
        )
    }