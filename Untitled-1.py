def equation(x):
    return x**3 - 6*x**2 + 11*x - 6

def bisection_method(f, a, b, tolerance):
    while (b - a) / 2 > tolerance:
        c = (a + b) / 2
        if f(c) == 0:
            return c  # c is an exact root
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

# Input values
a = 1  # Left endpoint of the interval
b = 4   # Right endpoint of the interval
tolerance = 0.0001  # Tolerance or desired error

# Call the bisection method function
root = bisection_method(equation, a, b, tolerance)

if root is not None:
    print(f"Approximate Root: {root:.6f}")