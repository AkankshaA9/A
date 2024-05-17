import requests
from flask import Flask, render_template

app = Flask(__name__)

def fetch_data(api_url):
    """Fetch data from the paginated API."""
    data = []
    page = 1
    while True:
        response = requests.get(api_url, params={'page': page})
        if response.status_code != 200:
            break
        page_data = response.json()
        if not page_data:
            break
        data.extend(page_data)
        page += 1
    return data

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
    api_url = 'https://devapi.beyondchats.com/api/get_message_with_sources'
    data = fetch_data(api_url)
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
