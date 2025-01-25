from flask import Flask, request, jsonify
from forecast import process_financial_data

app = Flask(__name__)

@app.route('/forecast', methods=['POST'])
def forecast():
    """API endpoint to accept price data and return sorted prices using a BST."""
    data = request.get_json()
    sorted_prices = process_financial_data(data['prices'])
    return jsonify(sorted_prices)

if __name__ == '__main__':
    app.run(debug=True)
