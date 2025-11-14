from flask import Flask, request, jsonify, render_template_string
import sys
import os

# Add the src directory to the Python path so we can import the calculator
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import calculate

app = Flask(__name__)

@app.route('/')
def index():
    # Read the HTML file and serve it
    with open(os.path.join(os.path.dirname(__file__), 'calculator.html'), 'r') as f:
        html_content = f.read()
    return render_template_string(html_content)

@app.route('/calculate', methods=['POST'])
def calculate_api():
    try:
        data = request.get_json()
        expression = data.get('expression', '')
        
        if not expression:
            return jsonify({'error': 'Empty expression'}), 400
        
        result = calculate(expression)
        return jsonify({'result': result})
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Invalid expression'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)