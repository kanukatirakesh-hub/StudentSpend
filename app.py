
from flask import Flask, request, redirect

app = Flask(__name__)

expenses = []

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>StudentSpend</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{font-family:Arial;background:#f5f7fb;margin:0;padding:20px}
.card{background:white;max-width:800px;margin:auto;padding:20px;border-radius:12px;box-shadow:0 4px 12px rgba(0,0,0,0.1)}
h1{color:#4F46E5;text-align:center}
input,select{width:100%;padding:10px;margin:6px 0;border-radius:8px;border:1px solid #ccc}
button{background:#4F46E5;color:white;border:none;padding:12px;width:100%;border-radius:8px;font-size:16px;cursor:pointer}
button:hover{background:#4338CA}
table{width:100%;margin-top:20px;border-collapse:collapse}
th,td{padding:10px;border-bottom:1px solid #eee;text-align:left}
.high{background:#EEF2FF;padding:10px;border-radius:8px;margin-bottom:15px}
.badge{background:#4F46E5;color:white;padding:3px 8px;border-radius:12px;font-size:12px}
</style>
</head>
<body>
<div class="card">
<h1>💰 StudentSpend</h1>
<p style="text-align:center;color:#666">Track your student expenses smartly</p>

<div class="high">
<h3>Highest Expenses</h3>
{% if top %}
{% for e in top %}
<div>🔹 <b>{{e['title']}}</b> - {{e['category']}} - ₹{{e['amount']}} <span class="badge">{{e['date']}}</span></div>
{% endfor %}
{% else %}
<p>No expenses yet. Add one below!</p>
{% endif %}
</div>

<form action="/add" method="POST">
<input name="title" placeholder="Expense Title (e.g. Books, Food)" required>
<select name="category"><option>Food</option><option>Books</option><option>Travel</option><option>Fees</option><option>Other</option></select>
<input name="amount" type="number" step="0.01" placeholder="Amount ₹" required>
<input name="date" type="date" required>
<button type="submit">+ Add Expense</button>
</form>

{% if all_exp %}
<table><tr><th>Title</th><th>Category</th><th>Amount</th><th>Date</th></tr>
{% for e in all_exp %}
<tr><td>{{e['title']}}</td><td>{{e['category']}}</td><td>₹{{e['amount']}}</td><td>{{e['date']}}</td></tr>
{% endfor %}
</table>
{% endif %}

<p style="text-align:center;margin-top:20px;color:#888">Live at studentspend-2.onrender.com | Deployed Successfully ✅</p>
</div>
</body>
</html>
"""

from flask import render_template_string

@app.route('/')
def index():
    top = sorted(expenses, key=lambda x: float(x['amount']), reverse=True)[:5]
    return render_template_string(HTML_PAGE, top=top, all_exp=expenses)

@app.route('/add', methods=['POST'])
def add():
    expenses.append({
        'title': request.form.get('title'),
        'category': request.form.get('category'),
        'amount': request.form.get('amount'),
        'date': request.form.get('date')
    })
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
