from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

#Cloudmersive API Key
API_KEY = ''

# API endpoint for barcode lookup
CLOUDMERSIVE_URL = 'https://api.cloudmersive.com/barcode/lookup/ean'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        barcode = request.form.get('barcode')
        if barcode:
            # Make a POST request to the Cloudmersive Barcode API
            headers = {
                'Apikey': API_KEY
            }
            params = {
                'BarcodeValue': barcode
            }
            response = requests.post(CLOUDMERSIVE_URL, headers=headers, json=params)
            
            # If response is successful, return product data
            if response.status_code == 200:
                product_data = response.json()
                return render_template('index.html', product_data=product_data, barcode=barcode)
            else:
                error_message = "Could not retrieve product data. Please try again."
                return render_template('index.html', error=error_message)
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
