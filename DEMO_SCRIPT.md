demo script
Open the dashboard at http://127.0.0.1:5000.
Explain the problem: students can lose track of small daily expenses.
Add an example:
Description: Lunch
Amount: 80
Category: Food
Date: today's date
Add another example:
Description: Bus pass
Amount: 300
Category: Travel
Date: today's date
Point out that total spending and transaction count update automatically.
Show the category chart. Explain that a dictionary/hash map groups amounts by category.
Show Highest expenses. Explain that sorting arranges transactions from largest to smallest.
Click Edit budget, set a small test budget, and show the remaining amount or budget warning.
Scroll to Recent transactions and show that records can be deleted.
Explain the stack: HTML/CSS/JavaScript for frontend, Flask/Python for backend, SQLite for storage.
Sample viva answers
What is the aim? To help students track expenses and manage a monthly budget.
Where is DSA used? Lists store expense records, dictionaries group amounts by category, and sorting finds the largest expenses.
Why use a hash map? It lets us store a running total for each category by using the category name as a key.
What is the sorting complexity? The built-in comparison sort generally takes O(n log n) time for n expenses.
Why SQLite? It is a lightweight database that stores records in a local file without requiring a separate database server.
What is the backend? Python with Flask, which handles form submissions, database operations, calculations, and page rendering.
What is the frontend? HTML, CSS, and JavaScript, which display the dashboard and provide user interaction.
What are the limitations? The current version is for one local user, entries are manual, and the chart library loads from a CDN.
