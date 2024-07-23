# Fraction Data Type in Python (OOP)

This project implements a custom `Fraction` class in Python using Object-Oriented Programming (OOP) principles to represent and manipulate fractions effectively.

**Key Features:**

- **Initialization:** Construct `Fraction` objects with numerator and denominator values. Defaults to 1 for both if not provided.
- **Arithmetic Operations:** Support addition, subtraction, multiplication, and division operations with other `Fraction` objects or integers.
- **String Representation:** Provide a clear and human-readable string representation for each `Fraction` object.
- **Comparison operators:** Equal to, greater than, less than, greater than or equal to, less than or equal to.
- **Automatic simplification:** Fractions are reduced to their simplest form automatically to their lowest terms using the greatest common divisor (GCD) algorithm..
- **Error handling:** Prevents division by zero.

**Installation:**

This project doesn't require any external dependencies. Simply clone or download the repository and use the `Fraction` class directly in your Python code.

**Usage Example:**

```python
from fraction import Fraction

# Create fractions
f1 = Fraction(3, 4)
f2 = Fraction(1, 2)

# Arithmetic operations
sum = f1 + f2  # Output: Fraction(5, 4)
difference = f1 - f2  # Output: Fraction(1, 4)
product = f1 * f2  # Output: Fraction(3, 8)
quotient = f1 / f2    # Output: Fraction(3, 2)

# Comparison operations
print(f1 == f2)  # Output: False
print(f1 >= f2)  # Output: True

# String representation
print(f"Fraction 1: {f1}")  # Output: Fraction 1: (3/4)
print(f"Fraction 2: {f2}")  # Output: Fraction 2: (1/2)
