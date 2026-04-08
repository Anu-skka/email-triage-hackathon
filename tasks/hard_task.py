# ============================================
# HARD TASK — Category + Urgency + Department
# ============================================
# The hardest task! The AI needs to:
# 1. Classify the email category
# 2. Judge the urgency (low/medium/high)
# 3. Assign the right department
# Score: 0.6 + 0.2 + 0.2 = 1.0 max
# ============================================

from environment import EmailTriageEnvironment, Action

class HardTask:
    """
    Hard Task — Category + Urgency + Department
    The AI classifies the email, judges urgency
    AND assigns it to the right department
    """

    def __init__(self):
        self.name = "hard"
        self.description = "Classify emails by category, urgency, and department"
        self.env = EmailTriageEnvironment(task_level="hard")

    def run(self, agent_fn) -> dict:
        """
        Runs the hard task with a given agent.
        agent_fn = a function that takes an email
                   and returns (category, urgency, department)
        """

        # Start fresh
        obs = self.env.reset()

        total_score = 0.0
        num_emails = 0
        results = []

        print("\n" + "="*50)
        print("🔴 HARD TASK — Category + Urgency + Department")
        print("="*50)

        while obs is not None:
            print(f"\n📧 Email #{obs.email_id}")
            print(f"   Subject : {obs.subject}")
            print(f"   Sender  : {obs.sender}")

            # Ask agent for all three
            category, urgency, department = agent_fn(obs)

            # Validate values
            if category not in ["spam", "urgent", "normal", "support"]:
                category = "normal"
            if urgency not in ["low", "medium", "high"]:
                urgency = "low"
            if department not in [
                "technical", "finance", "hr",
                "admin", "operations", "management", "none"
            ]:
                department = "none"

            # Create action
            action = Action(
                email_id=obs.email_id,
                category=category,
                urgency=urgency,
                department=department
            )

            # Step the environment
            next_obs, reward, done, info = self.env.step(action)

            print(f"   AI said : category={category}, urgency={urgency}, department={department}")
            print(f"   Score   : {reward.score}")
            print(f"   Feedback: {reward.feedback}")

            total_score += reward.score
            num_emails += 1
            results.append({
                "email_id": obs.email_id,
                "ai_answer": {
                    "category": category,
                    "urgency": urgency,
                    "department": department
                },
                "score": reward.score
            })

            obs = next_obs

        # Max possible score per email is 1.0
        final_score = total_score / num_emails if num_emails > 0 else 0.0

        print("\n" + "="*50)
        print(f"✅ HARD TASK COMPLETE!")
        print(f"   Final Score: {final_score:.2f} / 1.0")
        print("="*50)

        return {
            "task": "hard",
            "final_score": final_score,
            "emails_graded": num_emails,
            "results": results
        }