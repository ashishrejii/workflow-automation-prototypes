import re

def summarize_ticket(text):
    summary = text.strip()
    return summary[:180] + "..." if len(summary) > 180 else summary

def classify_priority(text):
    text_lower = text.lower()

    high_keywords = ["error", "unable", "failed", "critical", "urgent", "crash", "not working"]
    medium_keywords = ["slow", "delay", "not loading", "minor", "confusing"]
    low_keywords = ["question", "help", "how do i", "info"]

    if any(word in text_lower for word in high_keywords):
        return "High"
    elif any(word in text_lower for word in medium_keywords):
        return "Medium"
    elif any(word in text_lower for word in low_keywords):
        return "Low"
    return "Medium"

def categorize_ticket(text):
    categories = {
        "Login": ["login", "password", "authentication", "reset"],
        "Payments": ["payment", "refund", "billing", "charge"],
        "UI/UX": ["button", "layout", "design"],
        "Performance": ["slow", "lag", "loading"],
        "Other": []
    }

    text_lower = text.lower()

    for category, keywords in categories.items():
        if any(keyword in text_lower for keyword in keywords):
            return category
    return "Other"

def analyze_ticket(text):
    return {
        "summary": summarize_ticket(text),
        "priority": classify_priority(text),
        "category": categorize_ticket(text)
    }

if __name__ == "__main__":
    sample_ticket = """
    I am unable to reset my password. The reset link shows an error and the page crashes.
    """
    print(analyze_ticket(sample_ticket))

