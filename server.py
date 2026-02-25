from flask import Flask, jsonify
import requests

app = Flask(__name__)

API_URL = "https://www.mtsgold.co.th/mtsprice/priceData.php?c=1231243324"

def get_gold_price():
    try:
        response = requests.get(
            API_URL,
            timeout=5,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        data = response.json()

        buy = int(data["buyIn965"])
        sell = int(data["sellOut965"])

        return {
            "buy": f"{buy:,}",
            "sell": f"{sell:,}"
        }

    except Exception as e:
        return {"error": str(e)}

@app.route("/gold")
def gold():
    return jsonify(get_gold_price())

@app.route("/")
def home():
    return "Gold API Server Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
