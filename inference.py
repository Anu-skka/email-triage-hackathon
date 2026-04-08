# inference.py - NO API KEY NEEDED!
import re
from environment import EmailTriageEnvironment, Action

class SmartRuleBasedAgent:
    """An intelligent agent that uses rules (no API needed!)"""
    
    def __init__(self, task_level="easy"):
        self.task_level = task_level
        print(f"🤖 Smart Rule-Based Agent ready for {task_level} tasks")
    
    def classify_email(self, email_text):
        """Smart classification using keyword detection"""
        text = email_text.lower()
        
        # Spam indicators
        spam_words = ['winner', 'lottery', 'prize', 'click here', 'verify your account', 
                      '$', 'million', 'congratulations', 'free', 'claim']
        if any(word in text for word in spam_words):
            return 'spam'
        
        # Urgent indicators  
        urgent_words = ['urgent', 'asap', 'immediate', 'critical', 'down', 'emergency',
                       'deadline', 'eod', 'as soon as possible', 'important']
        if any(word in text for word in urgent_words):
            return 'urgent'
        
        # Support indicators
        support_words = ['help', 'issue', 'problem', 'not working', 'bug', 'support',
                        'broken', 'error', 'failed']
        if any(word in text for word in support_words):
            return 'support'
        
        # Normal/regular emails
        return 'normal'
    
    def get_urgency(self, email_text):
        """Determine urgency level"""
        text = email_text.lower()
        urgent_words = ['urgent', 'asap', 'immediate', 'critical', 'emergency', 
                       'deadline', 'eod', 'now']
        return 'urgent' if any(word in text for word in urgent_words) else 'normal'
    
    def get_department(self, email_text):
        """Route to correct department"""
        text = email_text.lower()
        
        if any(word in text for word in ['server', 'bug', 'technical', 'system', 'error']):
            return 'engineering'
        if any(word in text for word in ['invoice', 'payment', 'salary', 'finance', 'money']):
            return 'finance'
        if any(word in text for word in ['customer', 'client', 'product', 'purchase']):
            return 'support'
        if any(word in text for word in ['contract', 'legal', 'law', 'agreement']):
            return 'legal'
        if any(word in text for word in ['meeting', 'client', 'deal', 'sales']):
            return 'sales'
        
        return 'general'

def run_agent_on_task(task_level="easy"):
    """Run the agent on a specific task"""
    env = EmailTriageEnvironment(task_level=task_level)
    agent = SmartRuleBasedAgent(task_level)
    
    obs = env.reset()
    total_reward = 0
    steps = 0
    
    print(f"\n{'='*50}")
    print(f"🎯 TASK: {task_level.upper()}")
    print(f"{'='*50}")
    
    while True:
        email_text = obs.email_text
        if email_text == "DONE":
            break
        
        # Extract subject for display
        subject_match = re.search(r'Subject: (.+?)\n', email_text)
        subject = subject_match.group(1) if subject_match else "No subject"
        
        # Get agent's decisions
        if task_level == "easy":
            prediction = agent.classify_email(email_text)
            # Convert to spam/not_spam for easy task
            if prediction in ['urgent', 'support', 'normal']:
                prediction = 'not_spam'
            action = Action(category=prediction)
            
        elif task_level == "medium":
            category = agent.classify_email(email_text)
            urgency = agent.get_urgency(email_text)
            action = Action(category=category, urgency=urgency)
            
        else:  # hard
            category = agent.classify_email(email_text)
            urgency = agent.get_urgency(email_text)
            department = agent.get_department(email_text)
            action = Action(category=category, urgency=urgency, department=department)
        
        # Get reward
        obs, reward, done, info = env.step(action)
        total_reward += reward
        steps += 1
        
        # Show progress
        print(f"\n📧 Email {steps}: {subject[:40]}")
        print(f"   🤖 Agent: {action.category}", end="")
        if action.urgency:
            print(f" | Urgency: {action.urgency}", end="")
        if action.department:
            print(f" | Dept: {action.department}", end="")
        print(f"\n   💰 Reward: +{reward:.2f}")
        
        if done:
            break
    
    # Final score
    percentage = (total_reward / env.max_score) * 100
    print(f"\n{'─'*50}")
    print(f"📊 SCORE: {total_reward:.2f} / {env.max_score} ({percentage:.1f}%)")
    
    # Grade based on performance
    if percentage >= 80:
        grade = "🌟 EXCELLENT!"
    elif percentage >= 60:
        grade = "👍 GOOD!"
    elif percentage >= 40:
        grade = "📈 DECENT"
    else:
        grade = "💪 NEEDS IMPROVEMENT"
    
    print(f"🏆 {grade}")
    
    return total_reward

def main():
    """Run all tasks and show final results"""
    print("\n" + "🏆"*20)
    print("   META HACKATHON 2026 - EMAIL TRIAGE AI")
    print("🏆"*20)
    print("\n🤖 Smart Rule-Based Agent (No API Key Required)")
    
    results = {}
    for task in ["easy", "medium", "hard"]:
        score = run_agent_on_task(task)
        results[task] = score
    
    # Final summary
    print("\n" + "="*50)
    print("🎯 FINAL SUBMISSION RESULTS")
    print("="*50)
    print(f"🟢 Easy Task:   {results['easy']:.2f} / 4.00")
    print(f"🟡 Medium Task: {results['medium']:.2f} / 4.00")
    print(f"🔴 Hard Task:   {results['hard']:.2f} / 6.00")
    
    total = results['easy'] + results['medium'] + results['hard']
    max_total = 14.0
    print(f"\n📈 TOTAL SCORE: {total:.2f} / {max_total:.2f} ({total/max_total*100:.1f}%)")
    
    # Hackathon ready message
    if total >= 10:
        print("\n🎉 READY FOR META HACKATHON SUBMISSION!")
    else:
        print("\n💪 Keep improving - you can do better!")
    
    print("\n✨ Features of this agent:")
    print("   • No API key needed")
    print("   • Smart keyword-based rules")
    print("   • Works offline")
    print("   • Department routing included")
    print("="*50)

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running", "message": "Email Triage AI - Meta Hackathon 2026"}

@app.get("/run")
def run():
    results = {}
    for task in ["easy", "medium", "hard"]:
        score = run_agent_on_task(task)
        results[task] = score
    return results

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)