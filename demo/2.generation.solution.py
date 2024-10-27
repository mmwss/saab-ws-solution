"""
Create a Python script that analyzes sentiment in customer reviews. The script should:

- Read customer reviews from a JSON file.
- Use a sentiment analysis API to determine the sentiment (positive, negative, neutral) of each review.
- Aggregate the results to show the total number of reviews in each sentiment category.
- Save the annotated reviews with their sentiments back to a new JSON file.
"""

import json

# Hypothetical sentiment analysis function
def analyze_sentiment(text):
    # Placeholder for actual sentiment analysis logic
    # For this exercise, we'll simulate responses
    if 'good' in text or 'great' in text:
        return 'positive'
    elif 'bad' in text or 'terrible' in text:
        return 'negative'
    else:
        return 'neutral'

def main():
    # Read reviews from JSON file
    with open('data/reviews.json', 'r') as infile:
        reviews = json.load(infile)

    sentiment_counts = {'positive': 0, 'negative': 0, 'neutral': 0}
    annotated_reviews = []

    # Analyze sentiment for each review
    for review in reviews:
        sentiment = analyze_sentiment(review['text'])
        review['sentiment'] = sentiment
        annotated_reviews.append(review)
        sentiment_counts[sentiment] += 1

    # Save annotated reviews to a new JSON file
    with open('data/annotated_reviews.json', 'w') as outfile:
        json.dump(annotated_reviews, outfile, indent=2)

    print("Sentiment Analysis Results:")
    for sentiment, count in sentiment_counts.items():
        print(f"{sentiment.capitalize()}: {count} reviews")

if __name__ == "__main__":
    main()
