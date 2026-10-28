from flask import Flask, request, redirect, g, render_template_string
import sqlite3, os
from datetime import datetime, timedelta

app = Flask(__name__)
DB = 'expenses.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB)
        db.row_factory = sqlite3.Row
    return db

def init_db():
    conn = sqlite3.connect(DB)
    conn.execute('CREATE TABLE IF NOT EXISTS transactions (id INTEGER PRIMARY KEY, title TEXT, category TEXT, amount REAL, date TEXT, profile TEXT, type TEXT)')
    conn.commit(); conn.close()
init_db()

@app.teardown_appcontext
def close(e):
    db = getattr(g, '_database', None)
    if db: db.close()

CSS = """
<!DOCTYPE html><html><head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>StudentSpend</title>
<style>
*{box-sizing:border-box}body{margin:0;font-family:Inter,system-ui;background:#f8f9ff;padding-bottom:90px}
.head{background:linear-gradient(135deg,#6C5CE7,#a29bfe);color:white;padding:25px 20px 40px;border-radius:0 0 28px 28px}
.head h1{margin:0;font-size:26px;letter-spacing:0.5px}.head p{opacity:0.9;margin:6px 0 0}
.bal-card{background:white;margin:-28px 15px 15px;padding:18px;border-radius:20px;box-shadow:0 10px 30px rgba(108,92,231,0.15);display:flex;justify-content:space-between}
.bal-card b{font-size:20px;display:block}.green{color:#00b894}.red{color:#d63031}
.card{background:white;margin:12px 15px;padding:16px;border-radius:18px;border:1px solid #eee}
input,select{width:100%;padding:13px;margin:7px 0;border-radius:12px;border:1.5px solid #e9e9ff;background:#fcfcff}
.btn{background:#6C5CE7;color:white;border:none;padding:14px;width:100%;border-radius:14px;font-weight:700;font-size:16px}
.chip{padding:8px 16px;border-radius:20px;border:1.5px solid #ddd;background:white;margin:4px;cursor:pointer;display:inline-block}
.chip.active{background:#6C5CE7;color:white;border-color:#6C5CE7}
.row{display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid #f5f5f5}
.bottom{position:fixed;bottom:0;left:0;right:0;background:white;border-top:1px solid #eee;display:flex;justify-content:space-around;padding:10px 0;backdrop-filter:blur(10px)}
.bottom a{text-decoration:none;color:#b2bec3;text-align:center;font-size:20px}.bottom a.active{color:#6C5CE7}
.badge{font-size:11px;padding:3px 8px;border-radius:10px}.earn{background:#e0f7ef;color:#00b894}.spend{background:#ffe6e6;color:#d63031}
.help-box{background:#f1f0ff;padding:12px;border-radius:12px;margin:8px 0}
</style></head><body>
<div class="head"><h1>✨ StudentSpend</h1><p>Track Smart. Spend Ambitious.</p></div>
<div class="bal-card">
<div><small style="color:#636e72">Earnings</small><b class="green">₹{{earn}}</b></div>
<div style="text-align:center"><small style="color:#636e72">Balance</small><b>₹{{bal}}</b></div>
<div style="text-align:right"><small style="color:#636e72">Spent</small><b class="red">₹{{spend}}</b></div>
</div>

{% if page=='home' %}
<div class="card">
<div style="text-align:center;margin-bottom:10px">
<span class="chip {{'active' if profile=='Student' else ''}}" onclick="setP('Student')">🎓 Student</span>
<span class="chip {{'active' if profile=='Other' else ''}}" onclick="setP('Other')">💼 Other</span>
</div>
<div style="text-align:center">
<span class="chip {{'active' if ttype=='Expense' else ''}}" onclick="setT('Expense')">💸 Expenditure</span>
<span class="chip {{'active' if ttype=='Earning' else ''}}" onclick="setT('Earning')">💰 Earnings</span>
</div>
<form action="/add" method="POST" style="margin-top:12px">
<input type="hidden" name="profile" id="profile" value="{{profile}}">
<input type="hidden" name="type
