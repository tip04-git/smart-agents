class EvolutionAgent:
    def evolve(self, hypothesis):
        print(f"DEBUG: Evolving hypothesis: {hypothesis}")  # Debugging Log

        # Ensure multiple levels of evolution
        if "solar panels" in hypothesis.lower():
            return "Solar window panels for urban areas."  # First evolution
        elif "solar window panels" in hypothesis.lower():
            return "Transparent solar windows for buildings."  # Second evolution
        elif "transparent solar windows" in hypothesis.lower():
            return "Next-generation smart solar windows."  # Third evolution
        
        return hypothesis  # If already fully evolved, return unchanged
