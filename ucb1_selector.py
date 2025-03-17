# ucb1_selector.py
import math
import random
from database import Database

class UCB1Selector:
    def __init__(self):
        self.db = Database()

    def select_best_skill(self):
        skills = self.db.get_all_skills()
        total_runs = sum(skill["executions"] for skill in skills)

        if total_runs == 0:
            return random.choice(skills)["name"]  # Pick a random skill initially

        best_skill = max(
            skills,
            key=lambda s: (s["avg_reward"] + math.sqrt(2 * math.log(total_runs) / (s["executions"] + 1)))
        )

        return best_skill["name"]
