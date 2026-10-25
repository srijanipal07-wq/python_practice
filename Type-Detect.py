#Type Detecting using Python
def detect_type(value):
    if isinstance(value, int):
        return "Integer"
    elif isinstance(value, float):
        return "Float"
    elif isinstance(value, str):
        return "String"
    elif isinstance(value, list):
        return "List"
    elif isinstance(value, dict):
        return "Dictionary"
    elif isinstance(value, tuple):
        return "Tuple"
    elif isinstance(value, set):
        return "Set"
    else:
        return "Unknown Type"

print(detect_type(42))            # Output: Integer
print(detect_type(3.14))          # Output: Float
print(detect_type("Hello"))       # Output: String
print(detect_type([1, 2, 3]))     # Output: List
print(detect_type({"a": 1}))      # Output: Dictionary
print(detect_type((1, 2, 3)))     # Output: Tuple
print(detect_type({1, 2, 3}))     # Output: Set
print(detect_type(None))          # Output: Unknown Type
print(detect_type(True))          # Output: Unknown Type