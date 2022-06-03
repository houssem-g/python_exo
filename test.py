def stupid_addition(a, b):
    return int(a) + int(b) if isinstance(a, str) and isinstance(b, str) else str(a)+ str(b) if isinstance(a, int) and isinstance(b, int) else None

print(stupid_addition("5", "7"))