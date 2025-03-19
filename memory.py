import json

class Memory:
    def __init__(self, file_path="memory.json"):
        self.file_path = file_path
        try:
            with open(self.file_path, "r") as f:
                self.data = json.load(f)  # Load existing memory
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = {}  # Initialize if no file exists

    def store(self, query, hypothesis, score):
        self.data[query] = {"hypothesis": hypothesis, "score": score}
        with open(self.file_path, "w") as f:
            json.dump(self.data, f,indent=4)  # Save memory to file

    def retrieve(self, query):
        return self.data.get(query, None)  # Return stored data if available
