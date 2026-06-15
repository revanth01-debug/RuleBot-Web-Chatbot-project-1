# ============================================================
#  Project 1: Rule-Based AI Chatbot
#  DecodeLabs Industrial Training Kit — Batch 2026
#  IPO Model: Input → Process → Output
# ============================================================

# ── KNOWLEDGE BASE (Dictionary) ───────────────────────────
# Each key is a user intent, each value is the bot response
knowledge_base = {

    # Greetings
    "hello":          "Hello! How can I help you today?",
    "hi":             "Hi there! What can I do for you?",
    "hey":            "Hey! Great to see you. What's on your mind?",
    "good morning":   "Good morning! Hope you're having a wonderful day.",
    "good afternoon": "Good afternoon! How can I assist you?",
    "good evening":   "Good evening! What can I help you with?",

    # Farewells
    "bye":      "Goodbye! Have a great day! 👋",
    "goodbye":  "See you later! Take care! 👋",
    "see you":  "See you soon! Feel free to come back anytime.",

    # Help
    "help": (
        "Sure! You can ask me about:\n"
        "  • Greetings        — hello, hi, hey\n"
        "  • About me         — who are you, what is your name\n"
        "  • Python & AI      — what is python, what is ai\n"
        "  • Machine Learning — what is machine learning, what is deep learning\n"
        "  • Neural Networks  — what is a neural network\n"
        "  • NLP              — what is natural language processing\n"
        "  • Computer Vision  — what is computer vision\n"
        "  • AI vs ML         — what is the difference between ai and ml\n"
        "  • Fun              — tell me a joke\n"
        "Type 'exit' or 'quit' to end the session."
    ),
    "what can you do": "I can answer predefined questions, greet you, and have a simple conversation. Type 'help' to see all topics.",

    # About the bot
    "what is your name": "I'm RuleBot, your friendly rule-based chatbot!",
    "who are you":       "I'm RuleBot — a simple AI chatbot powered by Python dictionaries.",
    "who made you":      "I was created as a Python project to demonstrate rule-based conversational AI.",
    "are you a robot":   "Yes, I'm a chatbot — not a human, but I'll do my best to help!",
    "are you human":     "Nope! I'm RuleBot, a Python-powered chatbot.",
    "what are you":      "I'm RuleBot, a rule-based chatbot that responds using a Python dictionary knowledge base.",

    # General questions
    "how are you":        "I'm doing great, thanks for asking! How about you?",
    "what time is it":    "I don't have access to a clock, but your device can tell you the current time!",
    "what is today's date": "I can't check the date directly, but your phone or computer has the answer.",
    "what is python":     "Python is a high-level, general-purpose programming language known for its clean syntax and versatility.",
    "what is ai":         "AI stands for Artificial Intelligence — the simulation of human intelligence by machines.",
    "what is a chatbot":  "A chatbot is a program designed to simulate conversation with users, like me!",
    "tell me a joke":     "Why don't scientists trust atoms? Because they make up everything! 😄",
    "what is the weather":"I can't check live weather, but try searching 'weather' in your browser for current conditions.",

    # AI & ML Topics (5 new intents)
    "what is machine learning":
        "Machine Learning is a branch of AI where systems learn from data to improve their performance over time — without being explicitly programmed.",
    "what is deep learning":
        "Deep Learning is a subset of Machine Learning that uses neural networks with many layers to learn patterns from large amounts of data. It powers image recognition and voice assistants.",
    "what is a neural network":
        "A Neural Network is a computing system inspired by the human brain. It consists of layers of connected nodes (neurons) that process data and learn to make decisions or predictions.",
    "what is natural language processing":
        "Natural Language Processing (NLP) is a branch of AI that helps computers understand, interpret, and generate human language. Chatbots like me use NLP concepts!",
    "what is computer vision":
        "Computer Vision is a field of AI that enables machines to interpret and understand visual information from images and videos — used in face recognition and self-driving cars.",
    "what is the difference between ai and ml":
        "AI (Artificial Intelligence) is the broad concept of machines simulating human intelligence. ML (Machine Learning) is a subset of AI where machines learn from data automatically.",

    # Gratitude
    "thank you": "You're welcome! Let me know if there's anything else I can help with.",
    "thanks":    "Happy to help! Anything else?",
    "awesome":   "Glad you think so! 😊",
    "great":     "Glad to hear that! 😊",

    # Small talk
    "ok":    "Got it! Is there anything else you'd like to know?",
    "okay":  "Sure thing! What else can I help with?",
    "cool":  "😎 Cool indeed! Anything else on your mind?",
    "yes":   "Great! What would you like to know?",
    "no":    "Alright! Let me know if you change your mind.",
}

# Exit commands that terminate the chatbot session
EXIT_COMMANDS = {"exit", "quit", "bye", "goodbye"}

# Default fallback response for unknown inputs
FALLBACK_RESPONSE = (
    "I'm sorry, I didn't quite understand that. 🤔 "
    "Try rephrasing, or type 'help' to see what I can answer."
)

DIVIDER = "-" * 50


# ── PHASE 1: INPUT & SANITIZATION ─────────────────────────
def sanitise(raw_input):
    """
    Sanitize user input:
    - Strip leading/trailing whitespace
    - Convert to lowercase for consistent matching
    """
    clean_input = raw_input.lower().strip()
    return clean_input


# ── PHASE 2: PROCESS (Intent Matching + if-else Logic) ────
def process(clean_input):
    """
    Process the sanitized input using if-else logic:
    - Check for blank input
    - Check for exit commands
    - Match against knowledge base dictionary
    - Return fallback for unknown inputs
    """
    # Rule 1: Handle blank input
    if clean_input == "":
        return "Please type something — I'm all ears!", False

    # Rule 2: Check for exit commands using if-else
    elif clean_input == "exit" or clean_input == "quit":
        return "Goodbye! It was nice chatting with you. 👋", True

    # Rule 3: Dictionary lookup using .get() method
    elif clean_input in knowledge_base:
        response = knowledge_base.get(clean_input)
        # Check if it's a farewell from knowledge base
        if clean_input in ("bye", "goodbye"):
            return response, True
        else:
            return response, False

    # Rule 4: Fallback for unknown inputs
    else:
        return FALLBACK_RESPONSE, False


# ── PHASE 3: OUTPUT & MAIN LOOP ───────────────────────────
def run_chatbot():
    """
    Main chatbot loop — runs continuously until exit command.
    Follows the IPO Model:
      Input      → Accept and sanitize user input
      Process    → Match intent using if-else + dictionary
      Output     → Display the bot's response
    """
    print(DIVIDER)
    print("  Welcome to RuleBot 🤖")
    print("  Rule-Based AI Chatbot | DecodeLabs 2026")
    print("  Type 'help' to see what I can do.")
    print("  Type 'exit' or 'quit' to leave.")
    print(DIVIDER)

    # ── Continuous interaction loop ────────────────────────
    while True:

        # ── INPUT: Accept user input from keyboard ─────────
        raw_input = input("\nYou: ")

        # ── INPUT: Sanitize — lowercase + strip spaces ─────
        clean_input = sanitise(raw_input)

        # ── PROCESS: Apply if-else logic + dict lookup ─────
        response, should_exit = process(clean_input)

        # ── OUTPUT: Display the bot's response ─────────────
        print(f"RuleBot: {response}")

        # ── EXIT: Break the loop if exit command given ─────
        if should_exit:
            print(DIVIDER)
            print("  Session ended. See you next time!")
            print(DIVIDER)
            break


# ── Entry point ────────────────────────────────────────────
if __name__ == "__main__":
    run_chatbot()