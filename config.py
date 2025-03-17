# config.py

# Flask API Settings
API_HOST = "127.0.0.1"
API_PORT = 5000
DEBUG_MODE = True  # Set to False for production

# Database Configuration
DATABASE_NAME = "skills.db"

# Reinforcement Learning (UCB1) Hyperparameters
EXPLORATION_FACTOR = 2  # Controls exploration-exploitation balance in UCB1
INITIAL_SKILL_SCORE = 0.5  # Default score for newly added skills

# Skill Execution Settings
MAX_EXECUTION_TIME = 5  # Maximum time (seconds) allowed per skill execution
RETRY_ATTEMPTS = 3  # Number of retries if a skill fails
LOG_PERFORMANCE = True  # Enable logging of skill performance

# Logging Configuration
LOGGING_ENABLED = True
LOG_FILE = "skill_selector.log"

# Meta-Skill Orchestration
ENABLE_META_SKILLS = True
MAX_CHAIN_LENGTH = 3  # Maximum number of skills in a meta-skill sequence

# Default Skill Weights (for weighted selection)
DEFAULT_WEIGHTS = {
    "accuracy": 0.6,  # Accuracy is prioritized
    "speed": 0.3,  # Faster skills get preference
    "cost_efficiency": 0.1,  # Lower cost gets slight preference
}

# API Rate Limiting (Prevents abuse)
RATE_LIMIT_REQUESTS_PER_MINUTE = 100
