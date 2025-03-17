# app.py
from flask import Flask, request, jsonify
from ucb1_selector import UCB1Selector
from orchestrator import SkillOrchestrator
from database import Database

app = Flask(__name__)

# Initialize components
selector = UCB1Selector()
orchestrator = SkillOrchestrator()
db = Database()

@app.route("/select_skill", methods=["GET"])
def select_skill():
    """Selects the best skill dynamically using UCB1."""
    best_skill = selector.select_best_skill()
    return jsonify({"selected_skill": best_skill})

@app.route("/execute_skill", methods=["POST"])
def execute_skill():
    """Executes a selected skill and records its performance."""
    data = request.json
    skill_name = data.get("skill")

    if not skill_name:
        return jsonify({"error": "Skill name required"}), 400

    # Execute skill
    result, metrics = orchestrator.execute_skill(skill_name)

    # Log performance
    db.update_performance(skill_name, metrics)

    return jsonify({"result": result, "metrics": metrics})

@app.route("/leaderboard", methods=["GET"])
def leaderboard():
    """Returns skill rankings based on performance."""
    rankings = db.get_leaderboard()
    return jsonify(rankings)

if __name__ == "__main__":
    app.run(debug=True)
