from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    query_text = req.get("queryResult", {}).get("queryText", "").lower()

    # Simple example logic for outfit suggestion
    if "casual" in query_text:
        reply = "Try a cute crop top with ripped jeans and sneakers!"
    elif "formal" in query_text:
        reply = "A classy blazer with fitted trousers and heels would be perfect!"
    elif "party" in query_text:
        reply = "How about a sparkly bodycon dress with ankle boots?"
    else:
        reply = "I'm thinking something trendy! Could you tell me the occasion?"

    return jsonify({
        "fulfillmentText": reply
    })

if __name__ == '__main__':
    app.run(port=5000)
