import requests

def fetch_user_data(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    try:
        response = requests.get(url)

        # Check for HTTP errors
        response.raise_for_status()

        data = response.json()

        return {
            "name": data.get("name", "Unknown"),
            "email": data.get("email", "Unknown"),
            "company": data.get("company", {}).get("name", "Unknown"),
            "city": data.get("address", {}).get("city", "Unknown")
        }

    except requests.exceptions.HTTPError as http_err:
        return {"error": f"HTTP error: {http_err}"}
    except requests.exceptions.ConnectionError:
        return {"error": "Connection error"}
    except requests.exceptions.Timeout:
        return {"error": "Request timed out"}
    except Exception as e:
        return {"error": f"Unexpected error: {e}"}

if __name__ == "__main__":
    print(fetch_user_data(1))

