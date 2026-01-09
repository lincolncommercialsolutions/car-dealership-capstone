from flask import Flask, jsonify
from flask_cors import CORS
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
CORS(app)

# Download VADER lexicon for sentiment analysis
try:
    nltk.data.find('vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon', quiet=True)

sia = SentimentIntensityAnalyzer()


@app.route('/analyze/<string:text>', methods=['GET', 'POST'])
def analyze_sentiment(text):
    """
    Analyze sentiment of the given text.
    Returns: sentiment (positive/negative/neutral) and detailed scores
    """
    # Decode URL-encoded text
    text = text.replace('%20', ' ')
    
    # Get sentiment scores
    scores = sia.polarity_scores(text)
    
    # Determine overall sentiment
    compound = scores['compound']
    if compound >= 0.05:
        sentiment = 'positive'
    elif compound <= -0.05:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    
    return jsonify({
        'sentiment': sentiment,
        'scores': {
            'positive': scores['pos'],
            'negative': scores['neg'],
            'neutral': scores['neu'],
            'compound': compound
        },
        'text': text
    })


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'sentiment-analyzer'})


if __name__ == '__main__':
    print("Starting Sentiment Analyzer Service on port 5000...")
    app.run(debug=True, host='0.0.0.0', port=5000)
