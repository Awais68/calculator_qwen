# Calculator Architecture Document

## 1. Architecture Sketch

### High-Level Architecture
```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Input       │───▶│  Calculator    │───▶│   Output      │
│   Expression  │    │  Service       │    │   Result      │
│   (string)    │    │                │    │   (float)     │
└─────────────────┘    └──────────────────┘    └─────────────────┘
       │                       │                       │
       ▼                       ▼                       ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│  Expression   │    │  Parsing &     │    │  Error        │
│  Validator    │    │  Evaluation    │    │  Handler      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

### Component Architecture
- **Calculator Service**: Main entry point that handles expression input and returns results
- **Expression Parser**: Tokenizes and parses the input string into an Abstract Syntax Tree (AST)
- **Evaluator**: Traverses the AST and performs calculations with proper operator precedence
- **Expression Validator**: Checks for valid syntax before processing
- **Error Handler**: Manages and formats error responses

## 2. Interfaces

### 2.1 Primary Interface
```python
def calculate(expression: str) -> float:
    """
    Evaluates a mathematical expression and returns the result.
    
    Args:
        expression: A string containing the mathematical expression to evaluate.
                   Whitespace is ignored during processing.
    
    Returns:
        float: The result of evaluating the expression.
        
    Raises:
        ValueError: If the expression is invalid, contains division by zero,
                   or attempts to take the square root of a negative number.
    """
    pass
```

### 2.2 Supporting Interfaces
```python
class ExpressionValidator:
    def validate(self, expression: str) -> bool:
        """
        Checks if the expression follows basic syntax rules.
        """
        pass

class ExpressionParser:
    def parse(self, expression: str) -> AST:
        """
        Converts the string expression into an Abstract Syntax Tree.
        """
        pass

class Evaluator:
    def evaluate(self, ast: AST) -> float:
        """
        Evaluates the AST and returns the result.
        """
        pass
```

## 3. Data Model

### 3.1 Core Data Structures
```python
from typing import Union, List, Optional
from enum import Enum

class TokenType(Enum):
    NUMBER = "number"
    OPERATOR = "operator"
    FUNCTION = "function"
    PARENTHESIS = "parenthesis"
    WHITESPACE = "whitespace"

class Token:
    def __init__(self, type: TokenType, value: str, position: int):
        self.type = type
        self.value = value
        self.position = position

class ASTNode:
    def __init__(self, node_type: str, value: Union[str, float] = None, children: List['ASTNode'] = None):
        self.type = node_type
        self.value = value
        self.children = children or []

class ExpressionAST:
    def __init__(self, root: ASTNode):
        self.root = root
```

### 3.2 Supported Operations
- **Basic Arithmetic**: `+`, `-`, `*`, `/`
- **Advanced Operations**: `^` (exponentiation), `sqrt` (square root)
- **Grouping**: `(`, `)`
- **Numbers**: Integer and floating-point values

## 4. Error Handling

### 4.1 Error Types
- **ValueError** (General): Raised for invalid expressions, syntax errors
- **ValueError** (Division by Zero): Raised when division by zero occurs
- **ValueError** (Math Domain): Raised when taking square root of negative numbers

### 4.2 Error Scenarios
1. **Invalid Syntax**:
   - Unbalanced parentheses: `"(10 + 5"`
   - Incomplete expressions: `"10 +"`
   - Invalid characters: `"10 @ 5"`

2. **Mathematical Errors**:
   - Division by zero: `"10 / 0"`
   - Square root of negative numbers: `"sqrt(-4)"`

3. **Parser Errors**:
   - Unexpected operator sequences: `"10 + * 5"`
   - Malformed function calls: `"sqrt"`

### 4.3 Error Handling Strategy
1. **Early Validation**: Check for basic syntax issues before processing
2. **Contextual Errors**: Provide meaningful error messages that indicate what went wrong
3. **Graceful Failures**: Ensure invalid input doesn't crash the application

## 5. Requirements

### 5.1 Functional Requirements
- **FR-01**: Basic Arithmetic Operations - Support `+`, `-`, `*`, `/` operations
- **FR-02**: Advanced Operations - Support `^` (exponentiation) and `sqrt` function
- **FR-03**: Parentheses Support - Proper handling of grouping with parentheses
- **FR-04**: Operator Precedence - Follow standard mathematical precedence (PEMDAS/BODMAS)
- **FR-05**: Whitespace Handling - Ignore all whitespace in the input expression
- **FR-06**: Output Format - Return results as floating-point numbers
- **FR-07**: Input Format - Accept a single string parameter
- **FR-08**: Error Handling - Raise appropriate errors for invalid expressions

### 5.2 Non-Functional Requirements
- **NFR-01**: Accuracy - Results must be accurate within a relative or absolute tolerance of 1e-9
- **NFR-02**: Usability - Simple and clear interface for performing calculations
- **NFR-03**: Robustness - Gracefully handle invalid inputs and edge cases without crashing
- **NFR-04**: Performance - Fast evaluation of expressions (response time < 100ms for typical expressions)

## 6. Important Decisions and Tradeoffs

### 6.1 Parsing Approach
**Options**:
1. **Recursive Descent Parser**: Hand-written parser with explicit grammar rules
2. **Shunting Yard Algorithm**: Convert to postfix notation then evaluate
3. **AST-based Parser**: Build an abstract syntax tree and evaluate

**Decision**: Choose AST-based parser
**Tradeoffs**: 
- Pros: Clean separation of parsing and evaluation, easier to extend with new operations
- Cons: More complex implementation than simple evaluation

### 6.2 Operator Precedence Implementation
**Options**:
1. **Fixed Precedence Table**: Define precedence levels in a lookup table
2. **Grammar-Based**: Encode precedence in the parsing grammar
3. **Token-Based**: Assign precedence to each token type

**Decision**: Use precedence table approach
**Tradeoffs**:
- Pros: Clear and maintainable, easy to modify precedence rules
- Cons: Requires updating table when adding new operators

### 6.3 Mathematical Function Implementation
**Options**:
1. **Built-in Math Functions**: Use Python's math module for sqrt
2. **Custom Implementation**: Implement mathematical functions from scratch
3. **External Library**: Use a third-party math library

**Decision**: Use Python's math module
**Tradeoffs**:
- Pros: Efficient, well-tested implementations, handles edge cases properly
- Cons: Depends on standard library, limited control over precision

### 6.4 Input Validation Strategy
**Options**:
1. **Early Validation**: Validate syntax before parsing
2. **During Parsing**: Check validity as part of parsing process
3. **Late Validation**: Let parser handle validation

**Decision**: Early validation with parsing-time validation
**Tradeoffs**:
- Pros: Clear error messages, prevents unnecessary processing of invalid expressions
- Cons: Multiple validation steps required

## 7. Testing Strategy

### 7.1 Unit Tests
**Components to Test**:
- Expression parsing functionality
- Tokenization
- AST construction
- Evaluation of individual operations
- Error handling for specific scenarios

**Test Cases**:
- Basic arithmetic: `10 + 5`, `10 - 3`, `4 * 6`, `15 / 3`
- Complex expressions: `10 * (5 - 2)`, `(10 + 5) / 3`
- Operator precedence: `2 + 3 * 4`, `2 ^ 3 * 4`
- Mathematical functions: `sqrt(16)`, `sqrt(2 ^ 2)`
- Error cases: Division by zero, invalid expressions

### 7.2 Integration Tests
**Scenarios**:
- End-to-end calculation from input to output
- Complex expressions with multiple operations
- Mixed function and operator usage
- Whitespace handling in various positions

**Test Cases**:
- `calculate("10 + 5")` → `15.0`
- `calculate(" 10 * (5 - 2) ")` → `30.0`
- `calculate("sqrt(16) + 2")` → `6.0`
- `calculate("2 ^ 3 + 1")` → `9.0`

### 7.3 Edge Case Tests
**Scenarios**:
- Extremely large numbers
- Very small numbers (close to 0)
- Negative numbers
- Decimal numbers with many places
- Maximum nesting of parentheses

**Error Handling Tests**:
- Division by zero: `"10 / 0"`
- Square root of negative: `"sqrt(-4)"`
- Unbalanced parentheses: `"(10 + 5"`
- Invalid syntax: `"10 +"`
- Empty string: `""`

### 7.4 Performance Tests
- Benchmark calculation speed for complex expressions
- Memory usage for large expressions
- Response time consistency

### 7.5 Acceptance Criteria Based Tests
Based on the original requirements:
- Simple arithmetic: `calculate("10 + 5")` → `15.0`
- Multiple operations: `calculate("10 * (5 - 2)")` → `30.0`
- Division by zero error: `calculate("10 / 0")` → `ValueError`
- Invalid expression: `calculate("10 +")` → `ValueError`
- Negative square root: `calculate("sqrt(-4)")` → `ValueError`
- Whitespace handling: `calculate(" 10 + 5 ")` → `15.0`

### 7.6 Test Coverage Goals
- 100% coverage of calculation logic
- 100% coverage of error handling paths
- Coverage of all supported operators and functions
- Boundary condition testing for all mathematical operations