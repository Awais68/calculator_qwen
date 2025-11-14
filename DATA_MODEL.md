# Data Model for Python Calculator

## 1. Core Data Structures

### 1.1 Token Representation
```python
from enum import Enum
from typing import Union, List, Optional

class TokenType(Enum):
    NUMBER = "number"
    OPERATOR = "operator"
    FUNCTION = "function"
    PARENTHESIS = "parenthesis"
    EOF = "eof"  # End of file/input marker

class Token:
    """
    Represents a single token in the mathematical expression.
    
    Attributes:
        type: The type of token (NUMBER, OPERATOR, etc.)
        value: The actual value of the token (e.g., "5", "+", "sqrt")
        position: The position in the original expression string
    """
    def __init__(self, type: TokenType, value: str, position: int):
        self.type = type
        self.value = value
        self.position = position
    
    def __repr__(self):
        return f"Token({self.type.value}, '{self.value}', {self.position})"
    
    def __eq__(self, other):
        if not isinstance(other, Token):
            return False
        return (self.type == other.type and 
                self.value == other.value and 
                self.position == other.position)
```

### 1.2 Abstract Syntax Tree (AST) Nodes
```python
from typing import Union, List, Optional

class ASTNode:
    """
    Base class for all AST nodes in the calculator.
    
    Attributes:
        node_type: Type of the node (e.g., "binary_op", "number", "function")
        value: The value associated with the node (for literals)
        children: Child nodes for operations with operands
    """
    def __init__(self, node_type: str, value: Union[str, float, int] = None, 
                 children: List['ASTNode'] = None):
        self.type = node_type
        self.value = value
        self.children = children or []
    
    def __repr__(self):
        if self.children:
            return f"ASTNode({self.type}, value={self.value}, children={self.children})"
        else:
            return f"ASTNode({self.type}, value={self.value})"

class NumberNode(ASTNode):
    """
    Represents a number in the expression.
    
    Example: In "5", the node represents the number 5.
    """
    def __init__(self, value: float):
        super().__init__("number", value)

class BinaryOpNode(ASTNode):
    """
    Represents a binary operation between two operands.
    
    Example: In "5 + 3", this represents the addition operation with
    left=NumberNode(5), operator="+", right=NumberNode(3).
    
    Attributes:
        operator: The operator symbol ("+", "-", "*", "/", "^")
        left: The left operand AST node
        right: The right operand AST node
    """
    def __init__(self, operator: str, left: ASTNode, right: ASTNode):
        super().__init__("binary_op", operator, [left, right])
        self.operator = operator
        self.left = left
        self.right = right

class FunctionNode(ASTNode):
    """
    Represents a function application.
    
    Example: In "sqrt(16)", this represents the square root function
    applied to the argument 16.
    
    Attributes:
        function_name: The name of the function ("sqrt")
        argument: The argument to the function
    """
    def __init__(self, function_name: str, argument: ASTNode):
        super().__init__("function", function_name, [argument])
        self.function_name = function_name
        self.argument = argument

class ParenthesesNode(ASTNode):
    """
    Represents an expression in parentheses.
    
    Example: In "(5 + 3)", this represents the parenthesized expression.
    
    Attributes:
        inner_expression: The expression inside the parentheses
    """
    def __init__(self, inner_expression: ASTNode):
        super().__init__("parentheses", None, [inner_expression])
        self.inner_expression = inner_expression
```

## 2. Operator Precedence and Associativity

### 2.1 Operator Definition
```python
from typing import Dict, Tuple

# Operator precedence and associativity definition
# Format: {operator: (precedence, associativity)}
# Precedence: Higher number means higher precedence
# Associativity: 'left' or 'right'
OPERATOR_PRECEDENCE: Dict[str, Tuple[int, str]] = {
    '+': (1, 'left'),
    '-': (1, 'left'),
    '*': (2, 'left'),
    '/': (2, 'left'),
    '^': (3, 'right'),  # Right associative: 2^3^2 = 2^(3^2)
    'sqrt': (3, 'function')
}

# For parentheses handling
PARENTHESIS_SYMBOLS = {
    '(': 'open',
    ')': 'close'
}
```

### 2.2 Supported Operations
```python
# Basic arithmetic operations
BASIC_OPERATIONS = {'+', '-', '*', '/', '^'}

# Mathematical functions
MATH_FUNCTIONS = {'sqrt'}

# All supported operators and functions
SUPPORTED_OPERATIONS = BASIC_OPERATIONS.union(MATH_FUNCTIONS)
```

## 3. Error and Validation Data

### 3.1 Error Types
```python
from typing import NamedTuple

class CalculationError(Exception):
    """Base exception for calculation errors."""
    pass

class ParseError(CalculationError):
    """
    Exception raised for parsing errors.
    
    Attributes:
        message: Description of the error
        position: Position in the expression where error occurred
        expression: The expression that caused the error
    """
    def __init__(self, message: str, position: int, expression: str):
        self.message = message
        self.position = position
        self.expression = expression
        super().__init__(f"{message} at position {position} in '{expression}'")

class EvaluationError(CalculationError):
    """
    Exception raised for evaluation errors.
    
    Attributes:
        message: Description of the error
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)
```

### 3.2 Validation Results
```python
from typing import List, NamedTuple

class ValidationResult(NamedTuple):
    """
    Result of expression validation.
    
    Attributes:
        is_valid: Whether the expression is valid
        errors: List of errors found during validation
        warnings: List of warnings (if any)
    """
    is_valid: bool
    errors: List[str]
    warnings: List[str]
```

## 4. Expression Representation

### 4.1 Token Stream
```python
class TokenStream:
    """
    Represents a stream of tokens for parsing.
    
    Attributes:
        tokens: List of tokens in the expression
        position: Current position in the token stream
    """
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.position = 0
    
    def current_token(self) -> Optional[Token]:
        """Get the current token without advancing position."""
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return None
    
    def advance(self) -> Optional[Token]:
        """Advance to the next token and return it."""
        if self.position < len(self.tokens):
            token = self.tokens[self.position]
            self.position += 1
            return token
        return None
    
    def peek(self, offset: int = 1) -> Optional[Token]:
        """Peek at a token ahead without advancing position."""
        peek_pos = self.position + offset
        if peek_pos < len(self.tokens):
            return self.tokens[peek_pos]
        return None
    
    def is_at_end(self) -> bool:
        """Check if we've reached the end of the token stream."""
        return self.position >= len(self.tokens)
```

## 5. Examples of Data Structure Usage

### 5.1 Example Expression: "10 + 5 * 2"
Tokenization:
```
[Token(NUMBER, "10", 0), Token(OPERATOR, "+", 3), Token(NUMBER, "5", 5), 
 Token(OPERATOR, "*", 7), Token(NUMBER, "2", 9)]
```

AST Structure:
```
BinaryOpNode(
  operator="+",
  left=NumberNode(10.0),
  right=BinaryOpNode(
    operator="*",
    left=NumberNode(5.0),
    right=NumberNode(2.0)
  )
)
```

### 5.2 Example Expression: "sqrt(16) + 2"
Tokenization:
```
[Token(FUNCTION, "sqrt", 0), Token(PARENTHESIS, "(", 4), Token(NUMBER, "16", 5),
 Token(PARENTHESIS, ")", 7), Token(OPERATOR, "+", 9), Token(NUMBER, "2", 11)]
```

AST Structure:
```
BinaryOpNode(
  operator="+",
  left=FunctionNode(
    function_name="sqrt",
    argument=NumberNode(16.0)
  ),
  right=NumberNode(2.0)
)
```

This data model provides a clear structure for representing mathematical expressions as tokens and AST nodes, enabling proper parsing and evaluation with correct operator precedence and error handling.