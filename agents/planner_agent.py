class PlannerAgent:
    def __init__(self, llm):
        self.llm = llm

    def route_query(self, query):
        prompt = f"""
        Analyze the user query: "{query}"
        Classify it into one of two categories:
        1. 'SEARCH': The user is asking about technical content, syllabus, or specific data.
        2. 'GREET': The user is saying hello, asking how you are, or small talk.
        
        Return ONLY the word 'SEARCH' or 'GREET'.
        """
        decision = self.llm.invoke(prompt).strip().upper()
        return "SEARCH" if "SEARCH" in decision else "GREET"
