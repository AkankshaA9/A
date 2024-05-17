from flask import Flask, render_template

app = Flask(__name__)

def identify_citations(response_text, sources):
    """Identify which sources contribute to the response text by checking for common words."""
    response_words = set(response_text.lower().split())
    citations = []
    for source in sources:
        source_words = set(source['context'].lower().split())
        if response_words.intersection(source_words):
            citations.append({
                "id": source['id'],
                "link": source.get('link', '')
            })
    return citations

@app.route('/')
def index():
    """Fetch data, identify citations, and render the results in the template."""
    # Sample hardcoded data for testing
    data = [
        {
            "response": "Yes, we offer online delivery services through major platforms like Swiggy and Zomato. You can also reserve a table directly from our website if you are planning to have breakfast!",
            "sources": [
                {
                    "id": "71",
                    "context": "Order online Thank you for your trust in us! We are available on all major platforms like zomato, swiggy. You can also order directly from our website",
                    "link": "https://orders.brikoven.com"
                },
                {
                    "id": "75",
                    "context": "Do you give franchise if the brand No, we currently don't offer franchise opportunities for BrikOven! Although do feel free to drop in an email at theteam@brikoven. com so we can get in touch with you at a later stage if we do decide to give out franchisees'",
                    "link": ""
                },
                {
                    "id": "8",
                    "context": "Breakfast Reservations For Breakfast, we recommend making reservations in advance. Reservation is only available through our website",
                    "link": "https://www.brikoven.com/reservations"
                },
            ]
        }
    ]
    results = []
    for item in data:
        response_text = item['response']
        sources = item['sources']
        citations = identify_citations(response_text, sources)
        results.append({
            'response': response_text,
            'citations': citations
        })
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
