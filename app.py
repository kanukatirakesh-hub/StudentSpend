from flask import Flask, request, redirect, g, render_template_string
import sqlite3
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

HTML_PAGE = "<!DOCTYPE html><html><head>\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n<title>StudentSpend</title>\n<style>\n*{box-sizing:border-box}body{margin:0;font-family:system-ui;background:#f8f9ff;padding-bottom:90px}\n.head{background:linear-gradient(135deg,#6C5CE7,#a29bfe);color:white;padding:25px 20px 40px;border-radius:0 0 28px 28px}\n.head h1{margin:0;font-size:26px}.head p{opacity:0.9;margin:6px 0 0}\n.bal-card{background:white;margin:-28px 15px 15px;padding:18px;border-radius:20px;box-shadow:0 10px 30px rgba(108,92,231,0.15);display:flex;justify-content:space-between}\n.bal-card b{font-size:20px;display:block}.green{color:#00b894}.red{color:#d63031}\n.card{background:white;margin:12px 15px;padding:16px;border-radius:18px;border:1px solid #eee}\ninput,select{width:100%;padding:13px;margin:7px 0;border-radius:12px;border:1.5px solid #e9e9ff;background:#fcfcff}\n.btn{background:#6C5CE7;color:white;border:none;padding:14px;width:100%;border-radius:14px;font-weight:700;font-size:16px}\n.chip{padding:8px 16px;border-radius:20px;border:1.5px solid #ddd;background:white;margin:4px;cursor:pointer;display:inline-block}\n.chip.active{background:#6C5CE7;color:white;border-color:#6C5CE7}\n.row{display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid #f5f5f5}\n.bottom{position:fixed;bottom:0;left:0;right:0;background:white;border-top:1px solid #eee;display:flex;justify-content:space-around;padding:10px 0}\n.bottom a{text-decoration:none;color:#b2bec3;text-align:center;font-size:20px}.bottom a.active{color:#6C5CE7}\n.badge{font-size:11px;padding:3px 8px;border-radius:10px}.earn{background:#e0f7ef;color:#00b894}.spend{background:#ffe6e6;color:#d63031}\n.help-box{background:#f1f0ff;padding:12px;border-radius:12px;margin:8px 0}\n</style></head><body>\n<div class=\"head\"><h1>StudentSpend</h1><p>Track Smart. Spend Ambitious.</p></div>\n<div class=\"bal-card\">\n<div><small>Earnings</small><b class=\"green\">Rs.{{earn}}</b></div>\n<div style=\"text-align:center\"><small>Balance</small><b>Rs.{{bal}}</b></div>\n<div style=\"text-align:right\"><small>Spent</small><b class=\"red\">Rs.{{spend}}</b></div>\n</div>\n{% if page=='home' %}\n<div class=\"card\">\n<div style=\"text-align:center\">\n<a href=\"/?profile=Student&type={{ttype}}&filter={{filt}}\"><span class=\"chip {{'active' if profile=='Student' else ''}}\">Student</span></a>\n<a href=\"/?profile=Other&type={{ttype}}&filter={{filt}}\"><span class=\"chip {{'active' if profile=='Other' else ''}}\">Other</span></a>\n</div>\n<div style=\"text-align:center\">\n<a href=\"/?profile={{profile}}&type=Expense&filter={{filt}}\"><span class=\"chip {{'active' if ttype=='Expense' else ''}}\">Expenditure</span></a>\n<a href=\"/?profile={{profile}}&type=Earning&filter={{filt}}\"><span class=\"chip {{'active' if ttype=='Earning' else ''}}\">Earnings</span></a>\n</div>\n<form action=\"/add\" method=\"POST\" style=\"margin-top:12px\">\n<input type=\"hidden\" name=\"profile\" value=\"{{profile}}\">\n<input type=\"hidden\" name=\"type\" value=\"{{ttype}}\">\n<input name=\"title\" placeholder=\"Title\" required>\n<select name=\"category\">{% if ttype=='Earning' %}<option>Freelance</option><option>Part-time</option><option>Pocket Money</option><option>Other Earning</option>{% else %}<option>Food</option><option>Books</option><option>Travel</option><option>Fees</option><option>Other</option>{% endif %}</select>\n<input name=\"amount\" type=\"number\" step=\"0.01\" placeholder=\"Amount Rs\" required>\n<input name=\"date\" type=\"date\" value=\"{{today}}\" required>\n<button class=\"btn\">+ Add {{ttype}}</button>\n</form>\n</div>\n<div class=\"card\">\n<h3 style=\"margin:0\">This {{filt}}</h3>\n<p>{{profile}} - Earnings: Rs.{{f_earn}} | Spent: Rs.{{f_spend}} | Saved: Rs.{{f_bal}}</p>\n</div>\n{% elif page=='history' %}\n<div class=\"card\">\n<h3>History - {{filt}}</h3>\n<div>\n<a href=\"/history?filter=all\"><span class=\"chip {{'active' if filt=='all'}}\">All</span></a>\n<a href=\"/history?filter=week\"><span class=\"chip {{'active' if filt=='week'}}\">Week</span></a>\n<a href=\"/history?filter=month\"><span class=\"chip {{'active' if filt=='month'}}\">Month</span></a>\n<a href=\"/history?filter=earning\"><span class=\"chip {{'active' if filt=='earning'}}\">Earnings</span></a>\n<a href=\"/history?filter=expense\"><span class=\"chip {{'active' if filt=='expense'}}\">Expenses</span></a>\n</div>\n{% for r in rows %}\n<div class=\"row\"><div><b>{{r['title']}}</b> <span class=\"badge {{'earn' if r['type']=='Earning' else 'spend'}}\">{{r['type']}}</span><br>\n<small>{{r['profile']}} - {{r['category']}} - {{r['date']}}</small></div><div><b>{{r['amount']}}</b></div></div>\n{% else %}<p>No records</p>{% endfor %}\n</div>\n{% else %}\n<div class=\"card\">\n<h3>Help - Instant AI Answers</h3>\n<div class=\"help-box\"><b>Data potunda?</b><br>Database lo safe ga untadi.</div>\n<div class=\"help-box\"><b>Week / Month ela?</b><br>Week = last 7 days. Month = ee month 1st nundi.</div>\n<div class=\"help-box\"><b>Earnings vs Expenditure?</b><br>Green = Earnings. Red = Expenditure.</div>\n</div>\n{% endif %}\n<div class=\"bottom\">\n<a href=\"/?profile={{profile}}&type=Expense&filter={{filt}}\" class=\"{{'active' if page=='home'}}\">Home</a>\n<a href=\"/history?filter=all\" class=\"{{'active' if page=='history'}}\">History</a>\n<a href=\"/help\" class=\"{{'active' if page=='help'}}\">Help</a>\n</div>\n</body></html>\n"

@app.route('/')
def home():
    profile = request.args.get('profile','Student')
    ttype = request.args.get('type','Expense')
    filt = request.args.get('filter','month')
    db = get_db()
    rows = db.execute('SELECT * FROM transactions').fetchall()
    earn = sum(float(r['amount']) for r in rows if r['type']=='Earning')
    spend = sum(float(r['amount']) for r in rows if r['type']=='Expense')
    today = datetime.now().date()
    f_rows=[]
    for r in rows:
        try:
            d=datetime.strptime(r['date'],'%Y-%m-%d').date()
            if filt=='week' and d < today - timedelta(days=7): continue
            if filt=='month' and (d.month!=today.month or d.year!=today.year): continue
            f_rows.append(r)
        except:
            f_rows.append(r)
    f_earn = sum(float(r['amount']) for r in f_rows if r['type']=='Earning')
    f_spend = sum(float(r['amount']) for r in f_rows if r['type']=='Expense')
    return render_template_string(HTML_PAGE, page='home', earn=earn, spend=spend, bal=earn-spend, f_earn=f_earn, f_spend=f_spend, f_bal=f_earn-f_spend, profile=profile, ttype=ttype, filt=filt, today=datetime.now().strftime('%Y-%m-%d'))

@app.route('/history')
def hist():
    filt = request.args.get('filter','all')
    db = get_db()
    rows = db.execute('SELECT * FROM transactions ORDER BY date DESC, id DESC').fetchall()
    today = datetime.now().date()
    out=[]
    for r in rows:
        try:
            d=datetime.strptime(r['date'],'%Y-%m-%d').date()
            if filt=='week' and d < today - timedelta(days=7): continue
            if filt=='month' and (d.month!=today.month or d.year!=today.year): continue
            if filt=='earning' and r['type']!='Earning': continue
            if filt=='expense' and r['type']!='Expense': continue
            out.append(r)
        except:
            out.append(r)
    return render_template_string(HTML_PAGE, page='history', rows=out, filt=filt, earn=0, spend=0, bal=0, profile='Student', ttype='Expense')

@app.route('/help')
def help_page():
    return render_template_string(HTML_PAGE, page='help', rows=[], filt='all', earn=0, spend=0, bal=0, profile='Student', ttype='Expense')

@app.route('/add', methods=['POST'])
def add():
    db=get_db()
    db.execute('INSERT INTO transactions (title, category, amount, date, profile, type) VALUES (?,?,?,?,?,?)',
               (request.form['title'], request.form['category'], request.form['amount'], request.form['date'], request.form['profile'], request.form['type']))
    db.commit()
    return redirect(f"/?profile={request.form['profile']}&type={request.form['type']}&filter=month")

if __name__ == '__main__':
    app.run()

