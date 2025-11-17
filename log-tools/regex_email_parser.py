import re

def parse_email(text):
    """
    Extracts structured data from raw customer emails such as:
    - Email addresses
    - Order IDs
    - URLs
    - Error codes
    """

    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    order_ids = re.findall(r"ORDER-[0-9]{5}", text)
    urls = re.findall(r"https?://[^\s]+", text)
    error_codes = re.findall(r"ERR-[0-9]{3}", text)

    return {
        "emails": emails,
        "order_ids": order_ids,
        "urls": urls,
        "error_codes": error_codes
    }


if __name__ == "__main__":
    sample_email = """
    Hi team,

    I’m getting error code ERR-503 every time I try to checkout.
    My order ID is ORDER-12345 and the issue appears on:
    https://example.com/checkout

    Please contact me at user_22@domain.com.

    Thanks!
    """

    print(parse_email(sample_email))
