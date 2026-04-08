# ============================================
# EASY TASK — Spam or Not Spam?
# ============================================
# This is the simplest task.
# The AI just needs to decide:
# Is this email SPAM or NOT SPAM?
# Score: 1.0 = correct, 0.0 = wrong
# ============================================

from environment import EmailTriageEnvironment, Action

class EasyTask:
    """
    Easy Task — Spam Detection
    The AI looks at an email and says
    'spam' or 'not spam'
    """

    def __init__(self):
        self.name = "easy"
        self.description = "Classify emails as spam or not spam"
        self.env = EmailTriageEnvironment(task_level="easy")

    def run(self, agent_fn) -> dict:
        """
        Runs the easy task with a given agent.
        agent_fn = a function that takes an email
                   and returns a category string
        """

        # Start fresh
        obs = self.env.reset()

        total_score = 0.0
        num_emails = 0
        results = []

        print("\n" + "="*50)
        print("🟢 EASY TASK — Spam Detection")
        print("="*50)

        # Keep going until all emails are done
        while obs is not None:
            print(f"\n📧 Email #{obs.email_id}")
            print(f"   Subject : {obs.subject}")
            print(f"   Sender  : {obs.sender}")

            # Ask the agent what category this is
            # Agent can only say 'spam' or 'not spam'
            category = agent_fn(obs)

            # Simplify — anything not spam = not spam
            if category not in ["spam", "urgent", "normal", "support"]:
                category = "normal"

            # Create action
            action = Action(
                email_id=obs.email_id,
                category=category
            )

            # Step the environment
            next_obs, reward, done, info = self.env.step(action)

            print(f"   AI said : {category}")
            print(f"   Score   : {reward.score}")
            print(f"   Feedback: {reward.feedback}")

            total_score += reward.score
            num_emails += 1
            results.append({
                "email_id": obs.email_id,
                "ai_answer": category,
                "score": reward.score
            })

            # Move to next email
            obs = next_obs

        # Final score
        final_score = total_score / num_emails if num_emails > 0 else 0.0

        print("\n" + "="*50)
        print(f"✅ EASY TASK COMPLETE!")
        print(f"   Final Score: {final_score:.2f} / 1.0")
        print("="*50)

        return {
            "task": "easy",
            "final_score": final_score,
            "emails_graded": num_emails,
            "results": results
        }