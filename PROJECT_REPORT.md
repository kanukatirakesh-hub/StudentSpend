Mini Project Report
1. Abstract
StudentSpend is a web-based personal expense tracking application designed to help students understand and manage their daily spending. Users can add expenses with an amount, date, category, and optional note. The dashboard calculates monthly expenditure, compares it with a user-defined budget, groups expenses by category, and ranks the highest transactions. The project demonstrates practical use of Data Structures and Algorithms (DSA), especially lists, hash maps, and sorting, in a real-life application.
2. Problem Statement
Students often make small daily purchases but may not keep a clear record of them. Without a simple tracking method, it becomes difficult to know total monthly spending, identify high-spending categories, or stay within a budget.
3. Objectives
Record daily expenses in one place.
Calculate total monthly spending and remaining budget.
Group expenditure by category.
Sort transactions to identify the largest expenses.
Demonstrate DSA concepts in a practical application.
Store records persistently using a database.
4. Proposed Solution
StudentSpend provides a browser-based dashboard. A user enters the expense description, amount, category, date, and optional note. The Flask backend validates the input and stores it in SQLite. When the dashboard loads, it retrieves the selected month's expenses, calculates totals, groups categories with a dictionary, sorts expenses by amount, and sends the results to the HTML template. The dashboard presents the information in summary cards, a category chart, and a transaction table.
5. Technologies Used
HTML: Structure of the user interface.
CSS: Layout, colors, responsive design, and styling.
JavaScript: Interactive chart and small UI interactions.
Python: Backend logic and DSA implementation.
Flask: Web framework that handles routes and requests.
SQLite: Local relational database for expenses and settings.
Chart.js: Category spending doughnut chart.
6. DSA Concepts
List / Array: Expense records are represented as a Python list. Iteration over this list calculates totals and counts. Total calculation is O(n), where n is the number of expenses.
Dictionary / Hash Map: The category_totals() function stores each category as a key and its accumulated amount as a value. It processes n records in O(n) expected time when dictionary operations are average O(1).
Sorting: The highest_expenses() function sorts transactions by amount in descending order and returns the top five. Comparison sorting generally takes O(n log n) time.
Why DSA matters: These techniques turn raw transaction records into useful information. Lists store collections, dictionaries group values efficiently, and sorting makes the most important spending items easy to identify.
7. Database Design
expenses
id: Primary key; unique transaction identifier.
title: Expense description.
amount: Amount spent.
category: Expense category.
expense_date: Date of the transaction.
note: Optional extra information.
settings
key: Setting name, used as the primary key.
value: Setting value; currently stores the monthly budget.
8. Main Modules
Add expense: validates and stores a new transaction.
Dashboard: displays monthly totals, remaining budget, and transaction count.
Category analysis: groups expenses and displays a chart.
Highest expense analysis: sorts transactions by amount.
Budget management: allows the user to update the monthly budget.
Delete transaction: removes an expense record.
Summary API: returns monthly summary data in JSON format.
9. Algorithm
Read the selected month.
Retrieve matching expenses from SQLite.
Initialize total to zero and add every expense amount.
Use a dictionary to accumulate amounts for each category.
Sort expenses by amount in descending order.
Compare total expenditure with the monthly budget.
Display summary cards, category chart, top expenses, and transaction table.
10. Testing Plan
Add an expense with a valid description and positive amount.
Attempt to add an expense with an empty description or invalid amount.
Add expenses to multiple categories and verify category totals.
Add transactions with different amounts and verify descending ranking.
Change the budget and verify remaining amount and warning behavior.
Delete a transaction and verify it disappears from the table and totals.
Change the selected month and verify only that month's records are shown.
11. Limitations
The current educational version is designed for one local user and does not include login or cloud synchronization.
The chart uses a CDN and needs an internet connection to load Chart.js.
It does not connect to real bank accounts; all expenses are entered manually.
12. Future Enhancements
Add login and multiple-user support.
Export reports to CSV or PDF.
Add recurring expenses and savings goals.
Add monthly trend charts and notifications.
Add receipt image uploads.
13. Conclusion
StudentSpend applies web development, database management, and DSA to a common student problem. It shows how lists, hash maps, and sorting can be used to calculate totals, group spending, and rank transactions. The project is small enough to understand and extend while demonstrating a practical application of computer science concepts.
