def check_float(value: float, name: str = "value") -> float:
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} can only be a float or int")
    return float(value)
