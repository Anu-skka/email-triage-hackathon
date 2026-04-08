# ============================================
# MEDIUM TASK — Category + Urgency
# ============================================
# Harder than easy! The AI now needs to:
# 1. Classify the email category
# 2. Also judge the urgency (low/medium/high)
# Score: 0.6 for category + 0.2 for urgency
# Max score = 0.8
# ============================================

from environment import EmailTriageEnvironment, Action

class MediumTask:
    """
    Medium Task — Category + Urgency
    The AI classifies the email AND
    judges how urgent it is
    """

    def __init__(self):
        self.name = "medium"
        self.description = "Classify emails by category and urgency level"
        self.env = EmailTriageEnvironment(task_level="medium")

    def run(self, agent_fn) -> dict:
        """
        Runs the medium task with a given agent.
        agent_fn = a function that takes an email
                   and returns (category, urgency)
        """

        # Start fresh
        obs = self.env.reset()

        total_score = 0.0
        num_emails = 0
        results = []

        print("\n" + "="*50)
        print("🟡 MEDIUM TASK — Category + Urgency")
        print("="*50)

        while obs is not None:
            print(f"\n📧 Email #{obs.email_id}")
            print(f"   Subject : {obs.subject}")
            print(f"   Sender  : {obs.sender}")

            # Ask agent for category AND urgency
            category, urgency = agent_fn(obs)

            # Validate values
            if category not in ["spam", "urgent", "normal", "support"]:
                category = "normal"
            if urgency not in ["low", "medium", "high"]:
                urgency = "low"

            # Create action
            action = Action(
                email_id=obs.email_id,
                category=category,
                urgency=urgency
            )

            # Step the environment
            next_obs, reward, done, info = self.env.step(action)

            print(f"   AI said : category={category}, urgency={urgency}")
            print(f"   Score   : {reward.score}")
            print(f"   Feedback: {reward.feedback}")

            total_score += reward.score
            num_emails += 1
            results.append({
                "email_id": obs.email_id,
                "ai_answer": {"category": category, "urgency": urgency},
                "score": reward.score
            })

            obs = next_obs

        # Max possible score per email is 0.8
        max_possible = num_emails * 0.8
        final_score = total_score / max_possible if max_possible > 0 else 0.0

        print("\n" + "="*50)
        print(f"✅ MEDIUM TASK COMPLETE!")
        print(f"   Final Score: {final_score:.2f} / 1.0")
        print("="*50)

        return {
            "task": "medium",
            "final_score": final_score,
            "emails_graded": num_emails,
            "results": results
        }