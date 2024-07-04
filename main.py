
from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/generate-image', methods=['POST'])
def generate_image():
  product_data = request.form.to_dict()
  response = requests.post('http://localhost:5000/generate-image', json=product_data)
  image_url = response.json()['image_url']
  return redirect(url_for('results', image_url=image_url))

@app.route('/results')
def results():
  image_url = request.args.get('image_url')
  return render_template('results.html', image_url=image_url)

if __name__ == '__main__':
  app.run()
