from support_tools.summarize_ticket import categorize_ticket, classify_priority
from support_tools.sentiment_analysis import analyze_sentiment

def auto_assign(ticket_text, customer_type="standard"):
    """
    Automatically assigns a ticket to the correct team based on:
    - Category
    - Priority
    - Sentiment
    - Customer type (VIP / Standard)
    - Keyword triggers
    """

    category = categorize_ticket(ticket_text)
    priority = classify_priority(ticket_text)
    sentiment = analyze_sentiment(ticket_text)["sentiment"]

    text_lower = ticket_text.lower()

    keyword_triggers = {
        "Billing": ["refund", "overcharged", "invoice", "billing", "payment"],
        "Tech Support": ["error", "crash", "bug", "not working", "unable"],
        "Security": ["fraud", "hack", "breach", "phishing"],
        "Product": ["feature", "idea", "feedback", "design"]
    }

    # Determine the correct team
    assigned_team = "General Support"

    # 1. By category
    if category == "Payments":
        assigned_team = "Billing"
    elif category == "Login":
        assigned_team = "Tech Support"
    elif category == "UI/UX":
        assigned_team = "Product"
    elif category == "Performance":
        assigned_team = "Tech Support"

    # 2. Keyword override (stronger signal)
    for team, keywords in keyword_triggers.items():
        if any(word in text_lower for word in keywords):
            assigned_team = team

    # 3. VIP rule (always escalate VIP to specialized queue)
    if customer_type.lower() == "vip":
        assigned_team = f"{assigned_team} — VIP Queue"

    # 4. High priority and negative sentiment rule
    if priority == "High" and sentiment == "Negative":
        assigned_team = f"{assigned_team} — Escalation"

    return {
        "assigned_team": assigned_team,
        "category": category,
        "priority": priority,
        "sentiment": sentiment,
        "customer_type": customer_type,
    }


if __name__ == "__main__":
    demo_ticket = """
    I was overcharged for my subscription again. 
    This billing error is happening every month and it's getting unacceptable.
    """

    print(auto_assign(demo_ticket, customer_type="VIP"))
