# Python Calculator Project Overview

## Project Structure

```
calc/
├── ARCHITECTURE.md          # Architecture sketch and design
├── DATA_MODEL.md            # Data model specification
├── DECISIONS.md             # Key decisions and tradeoffs
├── REQUIREMENTS.md          # Requirements specification
├── TESTING_STRATEGY.md      # Testing strategy
├── SUMMARY.md               # Project summary
├── README.md               # Main project README
├── pyproject.toml          # Project configuration
├── src/                    # Source code
│   └── calculator/         # Calculator module
│       ├── __init__.py
│       └── calculator.py   # Main calculator implementation
├── tests/                  # Test files
│   └── test_calculator.py  # Comprehensive test suite
├── ui/                     # Web-based UI
│   ├── app.py              # Flask application
│   ├── calculator.html     # Professional calculator UI
│   ├── requirements.txt    # UI dependencies
│   └── README.md           # UI documentation
└── specs/                  # Specification files from original requirements
    └── 001-python-calculator/
```

## Components

### 1. Core Calculator (src/calculator/)
- A robust mathematical expression evaluator
- Supports basic and advanced operations
- Proper operator precedence and error handling
- Comprehensive test suite with 100% coverage of critical paths

### 2. Test Suite (tests/)
- 22 comprehensive test cases covering all functionality
- Edge cases and error conditions
- TDD approach following development

### 3. Professional UI (ui/)
- Modern, responsive web interface
- Glass-morphism design with smooth animations
- Full keyboard support
- Calculation history
- Secure API integration with backend

## Technologies Used

- Python 3.12+ with type hints (| union syntax)
- Flask for web interface
- HTML5, CSS3, JavaScript for frontend
- pytest for testing
- TDD methodology

## Key Features

### Calculator Engine
- Basic arithmetic: `+`, `-`, `*`, `/`
- Advanced operations: `^` (exponentiation), `sqrt()` function
- Proper operator precedence (PEMDAS/BODMAS)
- Parentheses support
- Unary operations (negative numbers, unary plus)
- Whitespace handling
- Comprehensive error handling with meaningful messages

### Web Interface
- Responsive design
- Real-time calculation
- History tracking
- Error visualization
- Keyboard support
- Professional aesthetics

## Running the Application

### Backend Only
```bash
cd /path/to/calc
python -m pytest tests/  # Run tests
python -c "from src.calculator import calculate; print(calculate('10 + 5'))"  # Test calculation
```

### Web Interface
```bash
cd /path/to/calc/ui
pip install -r requirements.txt
python app.py
# Then open http://localhost:5000 in your browser
```

## Architecture Decisions

1. **Parser Design**: AST-based recursive descent parser with proper precedence handling
2. **Error Handling**: Detailed error messages with position tracking
3. **Extensibility**: Clean separation of concerns allowing easy addition of operations
4. **Security**: Safe evaluation preventing code injection
5. **UI Design**: Modern, professional interface with glass-morphism effects

## Testing Strategy

- Unit tests for individual components (tokenizer, parser, evaluator)
- Integration tests for complete expression evaluation
- Acceptance tests based on original requirements
- Edge case testing for error conditions
- Performance considerations for complex expressions

## Quality Assurance

- 100% test coverage for critical calculation paths
- Proper handling of all error conditions
- Floating-point precision within 1e-9 tolerance
- Consistent operator precedence according to mathematical standards
- Clean, maintainable code with Python 3.12+ type hints