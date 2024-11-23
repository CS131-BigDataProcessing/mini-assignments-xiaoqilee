def power(base, exponent):
    return base ** exponent

def divide(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print("Dividing by zero is undefined")
