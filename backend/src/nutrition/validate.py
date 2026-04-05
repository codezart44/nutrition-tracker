from nutrition.errors import ValidationError

def validate_list_of(expected_type: type, values) -> list:

    if not isinstance(values, list):
        raise ValidationError(f"non list: {type(values).__name__}")
    
    for i, v in enumerate(values):
        if not isinstance(v, expected_type):
            raise ValidationError(f"non {expected_type.__name__} ({i}): {type(v).__name__}")
        
    return values

def validate_equal_lengths(a: list, b: list) -> tuple[list, list]:

    if len(a) != len(b):
        raise ValidationError(f"different lengths: {len(a)} != {len(b)}")
    
    return a, b

def validate_str(pattern) -> str:

    if not isinstance(pattern, str):
        raise ValidationError(f"non str: {type(pattern).__name__}")
    
    if not pattern:
        raise ValidationError(f"empty str: {pattern}")
    
    for i, c in enumerate(pattern):
        if not c.isalnum() and not c.isspace():
            raise ValidationError(f"non alnum ({i}): {c}")

    return pattern

