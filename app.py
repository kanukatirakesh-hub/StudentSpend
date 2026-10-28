Highest expenses
Your top spending items this month.

DSA: Sorting
{% if top_expenses %}
{% for expense in top_expenses %}
{{ loop.index }}
{{ expense.title }}{{ expense.category }} · {{ expense.expense_date }}
₹{{ '%.2f'|format(expense.amount) }}
{% endfor %}
{% else %}
↗
No expenses to rank
Once you add expenses, the largest ones appear here.

{% endif %}
Add an expense
Record a purchase or payment you made.

Quick entry
Description
e.g. Lunch at college
Amount (₹)
₹
0.00
Category
{{ category }}
Date
 
Note (optional)
Add a short note...
Your data is stored in a local SQLite database.＋ Add expense
Recent transactions
All expenses recorded for the selected month.

{{ expenses|length }} records
{% if expenses %}
{% for expense in expenses %} {% endfor %}
DESCRIPTION	CATEGORY	DATE	AMOUNT	
{{ expense.category[:1] }}
{{ expense.title }}{% if expense.note %}{{ expense.note }}{% endif %}
{{ expense.category }}	{{ expense.expense_date }}	₹{{ '%.2f'|format(expense.amount) }}	
×
{% else %}
▤
No transactions for this month
Add an expense using the form above to get started.

{% endif %}
StudentSpend · Built with Flask, SQLite, and DSA concepts Keep learning. Spend mindfully.
