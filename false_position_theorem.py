def equation(x):
    return x**2 - x - 2

def regula_falsi(a, b, tolerance):
    while abs(b - a) > tolerance:
        c = a - equation(a) * (b - a) / (equation(b) - equation(a))
        
        if equation(c) == 0:
            return c  # Found an exact root
        elif equation(c) * equation(a) < 0:
            b = c
        else:
            a = c
    
    return (a + b) / 2  # Approximate root

# Input values
a = 1.0
b = 3.0
tolerance = 0.0001

# Call the Regula Falsi method function
root = regula_falsi(a, b, tolerance)

print(f"Approximate root: {root:.6f}")