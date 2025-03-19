from web_scraper import fetch_web_data
class GenerationAgent:
    def run(self, query):
        return f"Generated hypothesis for {query}"

class ReflectionAgent:
    def run(self, hypothesis):
        return f"Refined {hypothesis} with logical checks"

class RankingAgent:
    def process(self, hypothesis):
        """Assigns a score based on real-time web data"""
        print("✅ Ranking Agent: Fetching real-time data...")
        web_data = fetch_web_data(hypothesis)

        print(f"🟡 DEBUG: Web Data Retrieved for Ranking → {web_data}")

        score = 5  # Default base score
        if "breakthrough" in web_data.lower():
            score = 9
        elif "innovation" in web_data.lower():
            score = 8
        elif "new" in web_data.lower() or "technology" in web_data.lower():
            score = 7
        elif "Latest trend" in web_data:
            score = min(10, score + 1)  # Boost score if new trends are detected
        elif "No relevant data found" in web_data:
            score = max(6, score - 1)  # Prevents dropping too low but shows no improvement

        return f"Score: {score} (Based on web data: {web_data})"


class EvolutionAgent:
    def run(self, refined_hypothesis, ranking_output):
        """Evolves the hypothesis based on ranking feedback and real-time web data."""
        web_data = fetch_web_data(refined_hypothesis)

        print(f"🟡 DEBUG: Web Data Retrieved for Evolution → {web_data}")

        cleaned_hypothesis = refined_hypothesis.split(". Latest trend:")[0].strip()  # Remove repeated Wikipedia text

        if "No relevant data found" not in web_data:
            evolved_hypothesis = f"{cleaned_hypothesis}. Latest trend: {web_data}"
        else:
            evolved_hypothesis = f"{cleaned_hypothesis}. Suggests alternative methods for validation."

        return evolved_hypothesis


import re    
class ProximityAgent:
    def run(self, evolved_hypothesis, score, memory):
        previous_data = memory.retrieve(evolved_hypothesis)

        # Extract numeric value from score
        score_match = re.search(r"Score: (\d+)", score)
        current_score = int(score_match.group(1)) if score_match else 0

        if previous_data:
            prev_score_match = re.search(r"Score: (\d+)", previous_data.get("score", "Score: 0"))
            prev_score = int(prev_score_match.group(1)) if prev_score_match else 0

            if prev_score < current_score:
                return f"✅ Improved from past score {prev_score} → {current_score}"
            elif prev_score == current_score:
                return f"⚠️ Same score as before: {current_score} (Consider exploring different approaches)"
            else:
                return f"❌ Regression! Score dropped from {prev_score} to {current_score}. Needs review."
        else:
            memory.store(evolved_hypothesis, evolved_hypothesis, score)
            return "Stored for future reference."

class MetaReviewAgent:
    def run(self, query, evolved_hypothesis):
        return f"Process review for {query}: Looks Good!"
