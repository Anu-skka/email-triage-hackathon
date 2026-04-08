# run_hackathon.py
import os
from dotenv import load_dotenv

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    print("❌ ERROR: Please add your OpenAI API key to .env file")
    print("Get one from: https://platform.openai.com/api-keys")
    exit(1)

from inference import run_agent_on_task

print("🚀 META HACKATHON 2026")
print("🏆 Email Triage AI Agent")
print("="*50)

results = {}
for task in ["easy", "medium", "hard"]:
    score = run_agent_on_task(task)
    results[task] = score

print("\n" + "="*50)
print("📊 FINAL SUBMISSION SCORES:")
print(f"  Easy:   {results['easy']:.2f}/4.00")
print(f"  Medium: {results['medium']:.2f}/4.00")
print(f"  Hard:   {results['hard']:.2f}/6.00")
print(f"\n  TOTAL:  {(results['easy']+results['medium']+results['hard']):.2f}/14.00")
print("="*50)