from memory import Memory

class ProximityAgent:
    def check_proximity(self, query, memory: Memory):
        past_data = memory.retrieve(query)
        return f"Proximity: Recalling past result - {past_data}" if past_data else "Proximity: No past data found."
