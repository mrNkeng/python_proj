import sys

from flask import Flask, request, jsonify
from forecast import process_financial_data

print(sys.path)

app = Flask(__name__)

@app.route('/forecast', methods=['POST'])
def forecast():
    try:
        data = request.get_json()
        # Assuming process_financial_data processes and returns sorted data
        result = process_financial_data(data['prices'])
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

print(sys.path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

print(sys.path)