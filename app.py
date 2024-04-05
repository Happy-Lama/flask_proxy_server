from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Endpoint to receive POST requests from Arduino
@app.route('/post-data', methods=['POST'])
def receive_post_data():
    try:
        # Get the data from the POST request sent by Arduino
        data = request.get_json()
        
        # Forward the received data to the fypserver
        fypserver_url = 'https://fyp-server-django.onrender.com/api/data/gsm/'
        response = requests.post(fypserver_url, json=data)

        # Check if the request was successful
        if response.status_code == 200:
            return jsonify({'message': 'Data forwarded successfully'}), 200
        else:
            return jsonify({'error': 'Failed to forward data to fypserver'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0')
