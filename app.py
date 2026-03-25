from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# হোম রুট - এখানে আপনার অ্যাপটি লোড হবে
@app.route('/')
def index():
    return render_template('index.html')

# উদাহরণ: পাইথন দিয়ে পেমেন্ট ভেরিফাই করার এপিআই (অপশনাল)
@app.route('/api/verify-payment', methods=['POST'])
def verify_payment():
    data = request.json
    trx_id = data.get('trxId')
    method = data.get('method')
    
    # এখানে আপনি পাইথন দিয়ে অটোমেটিক পেমেন্ট চেক করার লজিক লিখতে পারেন
    # বর্তমানে এটি শুধু সাকসেস মেসেজ পাঠাবে
    return jsonify({"status": "success", "message": f"Checking TrxID: {trx_id} via {method}"})

if __name__ == '__main__':
    # অ্যাপটি লোকালহোস্টে রান হবে
    app.run(debug=True, port=5000)