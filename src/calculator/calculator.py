import math
from enum import Enum
from typing import Union


class TokenType(Enum):
    NUMBER = "number"
    OPERATOR = "operator"
    FUNCTION = "function"
    PARENTHESIS = "parenthesis"
    EOF = "eof"


class Token:
    def __init__(self, type: TokenType, value: str, position: int = 0):
        self.type = type
        self.value = value
        self.position = position

    def __repr__(self):
        return f"Token({self.type.value}, '{self.value}', {self.position})"


class Lexer:
    def __init__(self, expression: str):
        self.expression = expression.replace(" ", "").replace("\t", "").replace("\n", "").replace("\r", "")
        self.position = 0
        self.tokens = []

    def tokenize(self) -> list[Token]:
        while self.position < len(self.expression):
            char = self.expression[self.position]
            
            if char.isdigit() or char == '.':
                self._parse_number()
            elif char in "+-*/^":
                self.tokens.append(Token(TokenType.OPERATOR, char, self.position))
                self.position += 1
            elif char == '(':
                self.tokens.append(Token(TokenType.PARENTHESIS, char, self.position))
                self.position += 1
            elif char == ')':
                self.tokens.append(Token(TokenType.PARENTHESIS, char, self.position))
                self.position += 1
            elif char.isalpha():
                self._parse_word()
            else:
                raise ValueError(f"Invalid character at position {self.position}: {char}")
        
        self.tokens.append(Token(TokenType.EOF, "", self.position))
        return self.tokens

    def _parse_number(self):
        start = self.position
        number_str = ""
        
        # Parse the number including possible decimal point
        while self.position < len(self.expression) and (self.expression[self.position].isdigit() or self.expression[self.position] == '.'):
            number_str += self.expression[self.position]
            self.position += 1
        
        if number_str.count('.') > 1:
            raise ValueError(f"Invalid number format at position {start}")
        
        self.tokens.append(Token(TokenType.NUMBER, number_str, start))

    def _parse_word(self):
        start = self.position
        word = ""
        while self.position < len(self.expression) and self.expression[self.position].isalpha():
            word += self.expression[self.position]
            self.position += 1
        
        if word == "sqrt":
            self.tokens.append(Token(TokenType.FUNCTION, word, start))
        else:
            raise ValueError(f"Invalid function name '{word}' at position {start}")


class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.position = 0

    def parse(self):
        if self.current_token().type == TokenType.EOF:
            raise ValueError("Empty expression")
        result = self._parse_expression()
        if self.current_token().type != TokenType.EOF:
            raise ValueError("Unexpected tokens after expression")
        return result

    def _parse_expression(self):
        return self._parse_addition_subtraction()

    def _parse_addition_subtraction(self):
        left = self._parse_multiplication_division()
        
        while self.current_token().type == TokenType.OPERATOR and self.current_token().value in ['+', '-']:
            operator = self.current_token().value
            self._consume(TokenType.OPERATOR)
            right = self._parse_multiplication_division()
            left = BinaryOpNode(operator, left, right)
        
        return left

    def _parse_multiplication_division(self):
        left = self._parse_exponentiation()
        
        while self.current_token().type == TokenType.OPERATOR and self.current_token().value in ['*', '/']:
            operator = self.current_token().value
            self._consume(TokenType.OPERATOR)
            right = self._parse_exponentiation()
            left = BinaryOpNode(operator, left, right)
        
        return left

    def _parse_exponentiation(self):
        left = self._parse_unary()
        
        if self.current_token().type == TokenType.OPERATOR and self.current_token().value == '^':
            operator = self.current_token().value
            self._consume(TokenType.OPERATOR)
            # Exponentiation is right-associative
            right = self._parse_exponentiation()
            left = BinaryOpNode(operator, left, right)
        
        return left

    def _parse_unary(self):
        # Handle unary minus and plus
        if self.current_token().type == TokenType.OPERATOR and self.current_token().value in ['-', '+']:
            operator = self.current_token().value
            self._consume(TokenType.OPERATOR)
            operand = self._parse_unary()  # Recursive call to handle multiple unary operators
            return UnaryOpNode(operator, operand)
        return self._parse_primary()

    def _parse_primary(self):
        token = self.current_token()
        
        if token.type == TokenType.NUMBER:
            value = float(token.value)
            self._consume(TokenType.NUMBER)
            return NumberNode(value)
        elif token.type == TokenType.FUNCTION:
            if token.value == "sqrt":
                func_name = token.value
                self._consume(TokenType.FUNCTION)
                if self.current_token().value != '(':
                    raise ValueError(f"Expected '(' after function {func_name}")
                self._consume(TokenType.PARENTHESIS)  # consume '('
                argument = self._parse_expression()
                if self.current_token().value != ')':
                    raise ValueError("Expected ')' after function argument")
                self._consume(TokenType.PARENTHESIS)  # consume ')'
                return FunctionNode(func_name, argument)
            else:
                raise ValueError(f"Unknown function: {token.value}")
        elif token.value == '(':
            self._consume(TokenType.PARENTHESIS)  # consume '('
            expr = self._parse_expression()
            if self.current_token().value != ')':
                raise ValueError("Expected ')' to close parentheses")
            self._consume(TokenType.PARENTHESIS)  # consume ')'
            return expr
        else:
            raise ValueError(f"Unexpected token: {token.type.value} '{token.value}'")

    def current_token(self):
        if self.position >= len(self.tokens):
            return self.tokens[-1]  # Return EOF token
        return self.tokens[self.position]

    def _consume(self, expected_type: TokenType):
        token = self.current_token()
        if token.type != expected_type:
            raise ValueError(f"Expected {expected_type.value}, got {token.type.value}")
        self.position += 1


class ASTNode:
    pass


class NumberNode(ASTNode):
    def __init__(self, value: float):
        self.value = value

    def __repr__(self):
        return f"NumberNode({self.value})"


class BinaryOpNode(ASTNode):
    def __init__(self, operator: str, left: ASTNode, right: ASTNode):
        self.operator = operator
        self.left = left
        self.right = right

    def __repr__(self):
        return f"BinaryOpNode({self.operator}, {self.left}, {self.right})"


class FunctionNode(ASTNode):
    def __init__(self, function_name: str, argument: ASTNode):
        self.function_name = function_name
        self.argument = argument

    def __repr__(self):
        return f"FunctionNode({self.function_name}, {self.argument})"


class UnaryOpNode(ASTNode):
    def __init__(self, operator: str, operand: ASTNode):
        self.operator = operator
        self.operand = operand

    def __repr__(self):
        return f"UnaryOpNode({self.operator}, {self.operand})"


class Evaluator:
    def evaluate(self, node: ASTNode) -> float:
        if isinstance(node, NumberNode):
            return float(node.value)
        elif isinstance(node, BinaryOpNode):
            left_val = self.evaluate(node.left)
            right_val = self.evaluate(node.right)
            
            if node.operator == '+':
                return left_val + right_val
            elif node.operator == '-':
                return left_val - right_val
            elif node.operator == '*':
                return left_val * right_val
            elif node.operator == '/':
                if right_val == 0:
                    raise ValueError("Division by zero")
                return left_val / right_val
            elif node.operator == '^':
                return left_val ** right_val
            else:
                raise ValueError(f"Unknown operator: {node.operator}")
        elif isinstance(node, UnaryOpNode):
            operand_val = self.evaluate(node.operand)
            
            if node.operator == '+':
                return operand_val
            elif node.operator == '-':
                return -operand_val
            else:
                raise ValueError(f"Unknown unary operator: {node.operator}")
        elif isinstance(node, FunctionNode):
            arg_val = self.evaluate(node.argument)
            
            if node.function_name == 'sqrt':
                if arg_val < 0:
                    raise ValueError("Square root of negative number")
                return math.sqrt(arg_val)
            else:
                raise ValueError(f"Unknown function: {node.function_name}")
        else:
            raise ValueError(f"Unknown node type: {type(node)}")


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
    if not expression or not expression.strip():
        raise ValueError("Empty expression")
    
    try:
        lexer = Lexer(expression)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        evaluator = Evaluator()
        result = evaluator.evaluate(ast)
        return float(result)
    except ValueError as e:
        # Re-raise ValueError as is
        raise e
    except Exception as e:
        # Convert any other exception to ValueError
        raise ValueError(f"Invalid expression: {str(e)}")