from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/items')
def items():
    data_path = os.path.join(os.path.dirname(__file__), 'items.json')
    items_list = []

    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            items_list = data.get('items', [])
    except FileNotFoundError:
        # If file is missing, keep items_list empty to trigger "No items found"
        items_list = []
    except json.JSONDecodeError:
        # If JSON is invalid, keep items_list empty to trigger "No items found"
        items_list = []

    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
