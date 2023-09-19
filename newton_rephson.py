def func(x):
    return x**3 - x**2 + 2

def deriv_func(x):
    return 3*x**2 - 2*x

def newton_raphson(initial_guess, tolerance):
    x = initial_guess
    
    while True:
        h = func(x) / deriv_func(x)
        x = x - h
        
        if abs(h) < tolerance:
            return x

# Input values
initial_guess = 1.0
tolerance = 1e-6

# Call the Newton-Raphson method function
root = newton_raphson(initial_guess, tolerance)

print(f"The value of the root is: {root:.6f}")