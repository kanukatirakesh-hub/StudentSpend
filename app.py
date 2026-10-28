
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

expenses = []

@app.route('/')
def index():
    top_expenses = sorted(expenses, key=lambda x: x['amount'], reverse=True)[:5]
    return render_template('index.html', top_expenses=top_expenses) if len(expenses)>0 else "StudentSpend - Add your expenses!"

@app.route('/add', methods=['POST'])
def add_expense():
    title = request.form.get('title', 'Test')
    category = request.form.get('category', 'General')
    amount = float(request.form.get('amount', 0))
    expenses.append({'title': title, 'category': category, 'amount': amount, 'expense_date': '2025-10-29'})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
