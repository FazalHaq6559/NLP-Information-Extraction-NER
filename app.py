from flask import Flask, render_template, request
from spacy import displacy
import spacy

app = Flask(__name__)

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # Get the input text from the form
    text = request.form['text']
    
    # Process the text with spaCy
    doc = nlp(text)
    
    # Render the named entity visualization
    html = displacy.render(doc, style='ent', page=True)
    
    return render_template('index.html', text=text, visualization=html)

if __name__ == '__main__':
    app.run(debug=True)
