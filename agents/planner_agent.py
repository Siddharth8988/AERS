class PlannerAgent:
    def __init__(self, llm):
        self.llm = llm

    def route_query(self, query):
        prompt = f"""You must reply with exactly one word only.
If the input is a greeting or small talk, reply: GREET
If the input is a question about any topic, reply: SEARCH

Input: "{query}"
Reply:"""
        decision = self.llm.invoke(prompt).strip().upper()
        # Extract first word only in case Qwen adds explanation
        first_word = decision.split()[0] if decision else "SEARCH"
        return "SEARCH" if "SEARCH" in first_word else "GREET"
