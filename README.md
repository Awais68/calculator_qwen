# Python Calculator

A mathematical expression evaluator that processes string inputs and returns floating-point results.

## Features

- Basic arithmetic operations: `+`, `-`, `*`, `/`
- Advanced operations: `^` (exponentiation), `sqrt` function
- Proper operator precedence following PEMDAS/BODMAS
- Parentheses support for grouping
- Whitespace handling (ignored)
- Comprehensive error handling
- Professional web-based UI

## Usage

### Direct Python Usage
```python
from calculator import calculate

result = calculate("10 + 5")  # Returns 15.0
result = calculate("sqrt(16) + 2")  # Returns 6.0
result = calculate("10 * (5 - 2)")  # Returns 30.0
```

### Web Interface
A professional web-based UI is available in the `ui/` directory:
1. Navigate to the ui directory: `cd ui/`
2. Install requirements: `pip install -r requirements.txt`
3. Run the application: `python app.py`
4. Open your browser and go to `http://localhost:5000`

## Requirements

- Python 3.12 or higher

## Installation

```bash
pip install -e .
```

## Testing

```bash
pytest
```