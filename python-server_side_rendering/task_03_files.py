from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# --- File Reading Functions ---
def load_json():
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return []

def load_csv():
    products = []
    try:
        with open('products.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row["id"].strip()),
                    "name": row["name"].strip(),
                    "category": row["category"].strip(),
                    "price": float(row["price"].strip())
                })
    except Exception as e:
        print(f"Error reading CSV: {e}")
    return products

# --- Route ---
@app.route('/products')
def products():
    source = request.args.get('source', 'json')  # default to JSON
    product_id = request.args.get('id', type=int)

    # Select source
    if source == 'json':
        data = load_json()
    elif source == 'csv':
        data = load_csv()
    else:
        return render_template('product_display.html',
                               products=[],
                               error="Wrong source. Use 'json' or 'csv'.")

    # Filter by id if provided
    if product_id:
        data = [p for p in data if p.get("id") == product_id]
        if not data:
            return render_template('product_display.html',
                                   products=[],
                                   error=f"Product with id {product_id} not found.")

    return render_template('product_display.html', products=data, error=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
