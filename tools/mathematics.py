import math
from llama_index.core.tools import FunctionTool


def multiply(x: int, y: int) -> int:
    """Multiply two numbers."""
    return x * y


def divide(x: int, y: int) -> float:
    """Divide x by y."""
    return x / y


def add(x: int, y: int) -> int:
    """Add two numbers."""
    return x + y


def subtract(x: int, y: int) -> int:
    """Subtract y from x."""
    return x - y


def power(x: int, y: int) -> int:
    """Raise x to the power of y."""
    return x**y


def square_root(x: int) -> float:
    """Return the square root of x."""
    return x**0.5


def cube_root(x: int) -> float:
    """Return the cube root of x."""
    return x ** (1 / 3)


def absolute(x: int) -> int:
    """Return the absolute value of x."""
    return abs(x)


def factorial(x: int) -> int:
    """Return the factorial of x."""
    if x == 0:
        return 1
    return x * factorial(x - 1)


def log(x: int, base: int) -> float:
    """Return the log of x with base."""
    return math.log(x, base)


def sin(x: int) -> float:
    """Return the sine of x."""
    return math.sin(x)


def cos(x: int) -> float:
    """Return the cosine of x."""
    return math.cos(x)


def tan(x: int) -> float:
    """Return the tangent of x."""
    return math.tan(x)


def math_operations() -> list:
    """Perform multiple math operations."""
    return [
        add,
        subtract,
        divide,
        multiply,
        power,
        square_root,
        cube_root,
        absolute,
        factorial,
        log,
        sin,
        cos,
        tan,
    ]


def return_math_operations() -> list:
    """Return the math functions."""
    return [FunctionTool.from_defaults(fn=func) for func in math_operations()]
