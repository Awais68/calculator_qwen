# Professional Calculator UI

A modern, responsive web-based calculator interface for the Python Calculator project.

## Features

- Clean, professional design with glass-morphism effects
- Full support for all calculator operations (+, -, *, /, ^, sqrt)
- Responsive design that works on desktop and mobile
- Calculation history
- Keyboard support
- Error handling and validation

## Running the Application

1. Make sure you have Python 3.12+ installed
2. Install requirements: `pip install -r requirements.txt`
3. Run the application: `python app.py`
4. Open your browser and go to `http://localhost:5000`

## Technical Architecture

- Frontend: HTML, CSS, JavaScript with a clean, modern UI
- Backend: Flask API connecting to the Python Calculator
- Communication: REST API calls between frontend and backend

## Supported Operations

- Basic arithmetic: `+`, `-`, `*`, `/`
- Exponentiation: `^`
- Square root: `sqrt()`
- Parentheses for grouping: `()`
- Decimal numbers
- Negative numbers

## API Endpoints

- `GET /` - Serves the calculator UI
- `POST /calculate` - Calculate an expression (expects JSON: `{"expression": "..."}`)

## Usage Examples

The calculator supports expressions like:
- `10 + 5`
- `sqrt(16) + 2`
- `(10 + 5) * 2`
- `2 ^ 3 ^ 2` (right associative)
- `-5 + 3` (negative numbers)