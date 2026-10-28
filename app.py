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
    conn.commit()
    conn.close()
init_db()

@app.teardown_appcontext
def close(e):
    db = getattr(g, '_database', None)
    if db:
        db.close()

HTML_PAGE = """
<!DOCTYPE html><html><head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>StudentSpend</title>
<style>
*{box-sizing:border-box}body{margin:0;font-family:system-ui;background:#f8f9ff;padding-bottom:90px}
.head{background:linear-gradient(135deg,#6C5CE7,#a29bfe);color:white;padding:25px 20px 40px;border-radius:0 0 28px 28px}
.head h1{margin:0;font-size:26px}.head p{opacity:0.9;margin:6px 0 0}
.bal-card{background:white;margin:-28px 15px 15px;padding:18px;border-radius:20px;box-shadow:0 10px 30px rgba(108,92,231,0.15);display:flex;justify-content:space-between}
.bal-card b{font-size:20px;display:block}.green{color:#00b894}.red{color:#d63031}
.card{background:white;margin:12px 15px;padding:16px;border-radius:18px;border:1px solid #eee}
input,select{width:100%;padding:13px;margin:7px 0;border-radius:12px;border:1.5px solid #e9e9ff;background:#fcfcff}
.btn{background:#6C5CE7;color:white;border:none;padding:14px;width:100%;border-radius:14px;font-weight:700;font-size:16px}
.chip{padding:8px 16px;border-radius:20px;border:1.5px solid #ddd;background:white;margin:4px;cursor:pointer;display:inline-block}
.chip.active{background:#6C5CE7;color:white;border-color:#6C5CE7}
.row{display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid #f5f5f5}
.bottom{position:fixed;bottom:0;left:0;right:0;background:white;border-top:1px solid #eee;display:flex;justify-content:space-around;padding:10px 0}
.bottom a{text-decoration:none;color:#b2bec3;text-align:center;font-size:20px}.bottom a.active{color:#
