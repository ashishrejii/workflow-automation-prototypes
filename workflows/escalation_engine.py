from support_tools.summarize_ticket import classify_priority, categorize_ticket
from support_tools.sentiment_analysis import analyze_sentiment

def should_escalate(ticket_text):
    """
    Determines whether a ticket should be escalated based on:
    - Priority
    - Sentiment
    - Critical keywords
    - Category type
    """

    priority = classify_priority(ticket_text)
    sentiment = analyze_sentiment(ticket_text)["sentiment"]
    category = categorize_ticket(ticket_text)

    critical_keywords = [
        "refund", 
        "angry", 
        "lawsuit",
        "fraud",
        "data loss",
        "crash",
        "not working",
        "outage",
        "breach"
    ]

    text_lower = ticket_text.lower()
    keyword_flag = any(word in text_lower for word in critical_keywords)

    escalation_reason = []

    if priority == "High":
        escalation_reason.append("High priority")

    if sentiment == "Negative":
        escalation_reason.append("Customer sentiment is negative")

    if keyword_flag:
        escalation_reason.append("Critical keyword detected")

    if category in ["Payments", "Security"]:
        escalation_reason.append(f"Sensitive category: {category}")

    should_escalate = len(escalation_reason) > 0

    return {
        "escalate": should_escalate,
        "priority": priority,
        "sentiment": sentiment,
        "category": category,
        "reason": escalation_reason
    }


if __name__ == "__main__":
    demo_ticket = """
    My payment failed again and this is extremely frustrating.
    I think there is some fraud happening. Fix this immediately.
    """

    print(should_escalate(demo_ticket))
