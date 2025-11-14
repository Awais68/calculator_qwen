# Feature Specification: Python Calculator

## 1. Introduction

This document outlines the requirements for a Python-based calculator that performs basic and advanced arithmetic operations. The calculator will be accessed through a single function that takes a string expression and returns a floating-point result.

## 2. Clarifications

### Session 2025-11-14

- Q: How should the `calculate` function handle an attempt to take the square root of a negative number? → A: Raise a `ValueError` (e.g., "Math domain error").
- Q: What is the precedence level of the `^` (exponentiation) and `sqrt` operators relative to multiplication and division? → A: `^` and `sqrt` have the same precedence as `*` and `/`.
- Q: How should the calculator handle whitespace (spaces, tabs) in the input expression? → A: Ignore all whitespace.

## 3. User Scenarios & Testing

### 3.1. Core Functionality

*   **Scenario:** A user wants to perform a simple arithmetic calculation.
    *   **Given** a user provides the expression "10 + 5".
    *   **When** the `calculate` function is called with the expression.
    *   **Then** the function should return `15.0`.

*   **Scenario:** A user wants to perform a calculation with multiple operations.
    *   **Given** a user provides the expression "10 * (5 - 2)".
    *   **When** the `calculate` function is called.
    *   **Then** the function should return `30.0`.

### 3.2. Edge Cases

*   **Scenario:** A user attempts to divide by zero.
    *   **Given** a user provides the expression "10 / 0".
    *   **When** the `calculate` function is called.
    *   **Then** the function should raise a `ValueError`.

*   **Scenario:** A user provides an invalid expression.
    *   **Given** a user provides the expression "10 +".
    *   **When** the `calculate` function is called.
    *   **Then** the function should raise a `ValueError`.

*   **Scenario:** A user attempts to take the square root of a negative number.
    *   **Given** a user provides the expression "sqrt(-4)".
    *   **When** the `calculate` function is called.
    *   **Then** the function should raise a `ValueError`.

## 4. Functional Requirements

| ID | Requirement | Acceptance Criteria |
|---|---|---|
| FR-01 | Basic Arithmetic | The calculator must support addition (+), subtraction (-), multiplication (*), and division (/). |
| FR-02 | Advanced Operations | The calculator must support exponentiation (^) and square root (sqrt). |
| FR-03 | Error Handling | The calculator must raise a `ValueError` for invalid expressions, including division by zero and taking the square root of a negative number. |
| FR-04 | Input Format | The calculator must accept a single string as input, ignoring all whitespace. |
| FR-05 | Output Format | The calculator must return a floating-point number for valid calculations. |

## 5. Success Criteria

*   **Correctness:** All calculations must be accurate within a relative or absolute tolerance of 1e-9.
*   **Usability:** The `calculate` function provides a clear and simple interface for performing calculations.
*   **Robustness:** The calculator gracefully handles invalid inputs and edge cases without crashing.

## 6. Assumptions

*   The order of operations will follow standard mathematical precedence (PEMDAS/BODMAS), with exponentiation (^) and square root (sqrt) having the same precedence as multiplication (*) and division (/).
*   The input expression will be a valid string.
