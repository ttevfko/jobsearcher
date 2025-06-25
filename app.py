from flask import Flask, request, render_template
from modules.pdf_parser import extract_text_from_pdf
from modules.job_scraper import search_jobs

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_cv', methods=['POST'])
def upload_cv():
    file = request.files['file']
    text = extract_text_from_pdf(file)  # PDF içeriğini al

    keywords = ["CNC", "operatörü", "freze", "fanuc"]
    job_links = search_jobs(keywords, location="Türkiye")

    print(job_links)  # Burada iş ilanı linklerini konsola yazdır

    return render_template('results.html', job_matches=job_links)

if __name__ == '__main__':
    app.run(debug=True)

