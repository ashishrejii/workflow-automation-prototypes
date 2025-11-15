def analyze_sentiment(text):
    """
    Lightweight sentiment analysis using keyword matching.
    """

    text = text.lower()

    positive_words = [
        "great", "excellent", "good", "love", "amazing",
        "helpful", "fast", "smooth", "thank you"
    ]

    negative_words = [
        "bad", "terrible", "slow", "error", "hate",
        "not working", "problem", "issue", "frustrated"
    ]

    score = 0

    for word in positive_words:
        if word in text:
            score += 1

    for word in negative_words:
        if word in text:
            score -= 1

    if score > 0:
        sentiment = "Positive"
    elif score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "sentiment": sentiment,
        "score": score
    }


if __name__ == "__main__":
    sample_text = "The app is slow and keeps showing an error. Very frustrating."
    print(analyze_sentiment(sample_text))
