import requests
import json

def send_slack_message(webhook_url, message):
    """
    Sends a message to a Slack channel using an Incoming Webhook.
    """

    payload = {
        "text": message
    }

    try:
        response = requests.post(
            webhook_url,
            data=json.dumps(payload),
            headers={"Content-Type": "application/json"}
        )

        # Raise error for non-200 responses
        response.raise_for_status()

        return {"status": "success", "detail": "Message sent to Slack"}

    except requests.exceptions.HTTPError as http_err:
        return {"status": "error", "detail": f"HTTP error: {http_err}"}
    except requests.exceptions.ConnectionError:
        return {"status": "error", "detail": "Connection error"}
    except Exception as e:
        return {"status": "error", "detail": f"Unexpected error: {e}"}


if __name__ == "__main__":
    # Placeholder for demonstration — replace with your own webhook if testing
    TEST_WEBHOOK = "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"

    print(send_slack_message(TEST_WEBHOOK, "New ticket received! 🚀"))
