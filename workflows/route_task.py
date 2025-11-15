def route_task(ticket):
    """
    Simple workflow router that assigns a ticket to the right team
    based on keywords, priority, and fallback logic.
    """

    text = ticket.get("text", "").lower()
    priority = ticket.get("priority", "Medium")

    # Keyword-based routing
    routing_rules = {
        "login": "Authentication Team",
        "password": "Authentication Team",
        "refund": "Billing Team",
        "payment": "Billing Team",
        "crash": "Engineering",
        "error": "Engineering",
        "slow": "Performance Team",
        "loading": "Performance Team"
    }

    for keyword, team in routing_rules.items():
        if keyword in text:
            return {
                "assigned_to": team,
                "reason": f"Matched keyword: {keyword}",
                "priority": priority
            }

    # Priority-based escalation
    if priority == "High":
        return {
            "assigned_to": "Critical Escalations",
            "reason": "High priority fallback",
            "priority": priority
        }

    # Default fallback routing
    return {
        "assigned_to": "General Support",
        "reason": "No keyword match; default routing",
        "priority": priority
    }


if __name__ == "__main__":
    sample_ticket = {
        "text": "My payment failed and the page is showing an error.",
        "priority": "High"
    }

    print(route_task(sample_ticket))
