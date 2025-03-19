from agents import GenerationAgent, ReflectionAgent, RankingAgent, EvolutionAgent, ProximityAgent, MetaReviewAgent
from memory import Memory

class Supervisor:
    def __init__(self,num_cycles=3):
        self.memory = Memory()
        self.num_cycles=num_cycles
        self.agents = {
            "generation": GenerationAgent(),
            "reflection": ReflectionAgent(),
            "ranking": RankingAgent(),
            "evolution": EvolutionAgent(),
            "proximity": ProximityAgent(),
            "meta_review": MetaReviewAgent(),
        }

    def run_pipeline(self, query):
        print(f"🔹 Supervisor: Processing query - {query}")

        # Step 1: Generate hypotheses
        hypothesis = self.agents["generation"].run(query)
        for cycle in range(1,self.num_cycles+1):
            print(f"\n Cycle {cycle}:")
            print(f"  ✅ Generation Agent: {hypothesis}")

        # Step 2: Reflect on the hypothesis
            refined_hypothesis = self.agents["reflection"].run(hypothesis)
            print(f"  ✅ Reflection Agent: {refined_hypothesis}")

        # Step 3: Rank the hypothesis
            ranking_output = self.agents["ranking"].process(refined_hypothesis)
            print(f"  ✅ Ranking Agent: Score {ranking_output}")

        # Step 4: Evolve the hypothesis
            evolved_hypothesis = self.agents["evolution"].run(refined_hypothesis,ranking_output)
            print(f"  ✅ Evolution Agent: {evolved_hypothesis}")

        # Step 5: Check past data
            related_info = self.agents["proximity"].run(evolved_hypothesis,ranking_output, self.memory)
            print(f"  ✅ Proximity Agent: {related_info}")

        # Step 6: Meta-review the process
            review = self.agents["meta_review"].run(query, evolved_hypothesis)
            print(f"  ✅ Meta-Review Agent: {review}")

        # Store the final refined hypothesis in memory
            self.memory.store(query, evolved_hypothesis, ranking_output)
            hypothesis=evolved_hypothesis

        print("\n Final Output After all cycles:")
        print(f"Hypotheisis:{hypothesis}")
        print(f" score:{ranking_output}")

        return hypothesis,ranking_output

