from supervisor import Supervisor

class IterativeSupervisor(Supervisor):
    def iterative_process(self, query, cycles=3):
        hypothesis = self.generation.generate(query)  # Generate first hypothesis

        for cycle in range(cycles):
            print("\n" + "="*40)
            print(f"🔄  Cycle {cycle + 1} - Processing Query: {query}")
            print("="*40)

            print(f"\n📌 Hypothesis Before Evolution: {hypothesis}")
            
            # Evolve the hypothesis
            hypothesis = self.evolution.evolve(hypothesis)

            print(f"🔬 Hypothesis After Evolution: {hypothesis}")

            # Process with other agents
            print("\n--- 🧠 Reflection Agent ---")
            reflection = self.reflection.reflect(hypothesis)
            print(f"✅ {reflection}")

            print("\n--- 📊 Ranking Agent ---")
            ranking = self.ranking.rank(hypothesis)
            print(f"🏅 {ranking}")

            print("\n--- 🔗 Proximity Agent ---")
            proximity = self.proximity.check_proximity(query, self.memory)
            print(f"🔍 {proximity}")

            print("\n--- 📝 Meta-Review Agent ---")
            meta_review = self.meta_review.review("Process Log")
            print(f"📢 {meta_review}")

            # Store the evolved hypothesis
            self.memory.store(query, hypothesis)
            print("\n💾 Stored evolved hypothesis in memory.")

            print("\n" + "-"*40)

if __name__ == "__main__":
    iterative_supervisor = IterativeSupervisor()
    iterative_supervisor.iterative_process("Renewable energy for urban areas", 3)
