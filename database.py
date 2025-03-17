import sqlite3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Database:
    def __init__(self, db_path="skills.db"):
        """Initialize the database connection and create required tables."""
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cur = self.conn.cursor()
        self.setup()

    def setup(self):
        """Creates database tables for tracking skill performance."""
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS skill_performance (
                skill TEXT PRIMARY KEY,
                executions INTEGER DEFAULT 0,
                avg_reward REAL DEFAULT 0
            )
        """)
        self.conn.commit()

    def update_performance(self, skill, accuracy):
        """
        Updates skill performance metrics.

        If the skill exists, update executions and new average accuracy.
        Otherwise, insert a new skill entry.
        """
        self.cur.execute("SELECT executions, avg_reward FROM skill_performance WHERE skill = ?", (skill,))
        row = self.cur.fetchone()

        if row:
            executions, avg_reward = row
            new_executions = executions + 1
            new_avg_reward = (avg_reward * executions + accuracy) / new_executions
            self.cur.execute(
                "UPDATE skill_performance SET executions = ?, avg_reward = ? WHERE skill = ?",
                (new_executions, new_avg_reward, skill)
            )
        else:
            self.cur.execute(
                "INSERT INTO skill_performance (skill, executions, avg_reward) VALUES (?, ?, ?)",
                (skill, 1, accuracy)
            )

        self.conn.commit()
        logging.info(f"Updated performance: {skill} -> Accuracy: {accuracy}")

    def get_all_skills(self):
        """Retrieves all skills and their performance metrics."""
        self.cur.execute("SELECT skill, executions, avg_reward FROM skill_performance")
        rows = self.cur.fetchall()
        skills = [{"name": row[0], "executions": row[1], "avg_reward": row[2]} for row in rows]
        return skills

    def get_leaderboard(self, limit=10):
        """Returns top skills ranked by performance."""
        self.cur.execute(
            "SELECT skill, avg_reward FROM skill_performance ORDER BY avg_reward DESC LIMIT ?",
            (limit,)
        )
        leaderboard = [{"skill": row[0], "score": row[1]} for row in self.cur.fetchall()]
        return leaderboard

    def close(self):
        """Closes the database connection."""
        self.conn.close()
        logging.info("Database connection closed.")
