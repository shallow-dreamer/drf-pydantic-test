# utils.py
import re

def camel_to_snake(name: str) -> str:
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

def snake_to_camel(name: str) -> str:
    parts = name.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])
