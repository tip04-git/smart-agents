from supervisor import Supervisor

if __name__ == "__main__":
    supervisor = Supervisor()
    query = "solar panels"
    final_output, score = supervisor.run_pipeline(query)

    print("\n🔹 Final Output:")
    print(f"  Hypothesis: {final_output}")
    print(f"  Score: {score}")
