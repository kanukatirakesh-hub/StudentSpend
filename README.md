A beginner-friendly Data Structures and Algorithms (DSA) mini project. It helps students record expenses, track monthly budgets, compare spending categories, and identify their highest expenses.
Features
Add and delete expenses
Categorize spending (Food, Travel, Education, Shopping, Bills, Health, Entertainment, Other)
Monthly dashboard with total spending, remaining budget, and transaction count
Editable monthly budget and budget warnings
Category spending chart
Highest-expense ranking
SQLite database stores data locally
JSON summary endpoint at /api/summary?month=YYYY-MM
Tech stack
Frontend: HTML, CSS, JavaScript, Chart.js
Backend: Python + Flask
Database: SQLite
DSA: Lists, dictionaries (hash maps), sorting
Run locally (Windows)
Install Python 3.10 or later from https://www.python.org/downloads/ (enable “Add Python to PATH” during setup).
Extract the StudentSpend.zip file.
Open the extracted StudentSpend folder.
In File Explorer, click the address bar, type cmd, and press Enter.
Run:
py -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py
If py is not recognized, try python instead.
Open http://127.0.0.1:5000 in your browser.
Stop the server by returning to the terminal and pressing Ctrl+C.
Run on macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
Then open http://127.0.0.1:5000.
Where DSA is used
List / Array: get_expenses() returns a list of expense records. The dashboard traverses it to calculate totals and counts.
Dictionary / Hash Map: category_totals() groups amounts by category in one pass using a dictionary.
Sorting: highest_expenses() uses sorted(..., reverse=True) to rank largest transactions first. Category totals are also sorted for display.
Complexity: For n expenses, calculating total and category totals takes O(n) time. Sorting expenses takes O(n log n) time. The dictionary uses average O(1) lookup/update per category.
Database
The SQLite database file studentspend.db is created automatically when the app starts. The expenses table stores transactions; settings stores the monthly budget.
API example
Open http://127.0.0.1:5000/api/summary?month=2026-10 while the server is running to see a JSON summary.
Notes
The first run creates an empty database automatically.
Chart.js is loaded from a CDN, so the chart requires internet access. The rest of the app works locally.
This is an educational demo, not a secure production finance system. It has no user accounts and stores data only on the computer running it.
