import random

class RankingAgent:
    def rank(self, hypothesis):
        score = random.randint(5, 10)
        return f"Ranking: {hypothesis} scored {score}/10."
