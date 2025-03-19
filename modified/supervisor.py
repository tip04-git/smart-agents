from memory import Memory
from agents.generation import GenerationAgent
from agents.reflection import ReflectionAgent
from agents.ranking import RankingAgent
from agents.evolution import EvolutionAgent
from agents.proximity import ProximityAgent
from agents.meta_review import MetaReviewAgent

class Supervisor:
    def __init__(self):
        self.memory = Memory()
        self.generation = GenerationAgent()
        self.reflection = ReflectionAgent()
        self.ranking = RankingAgent()
        self.evolution = EvolutionAgent()
        self.proximity = ProximityAgent()
        self.meta_review = MetaReviewAgent()

    def process_query(self, query):
        print("\n--- New Query Processing ---\n")
        
        hypothesis = self.generation.generate(query)
        print(hypothesis)

        reflection = self.reflection.reflect(hypothesis)
        print(reflection)

        ranking = self.ranking.rank(hypothesis)
        print(ranking)

        evolved_hypothesis = self.evolution.evolve(hypothesis)
        print(evolved_hypothesis)

        proximity = self.proximity.check_proximity(query, self.memory)
        print(proximity)

        meta_review = self.meta_review.review("Process Log")
        print(meta_review)

        self.memory.store(query, evolved_hypothesis)
        print("\nStored results in memory.\n")
