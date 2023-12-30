import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculate BMI from height and weight"""
    if (not isinstance(height, list) or
            not isinstance(weight, list) or
            not all(isinstance(h, (int, float)) for h in height) or
            not all(isinstance(w, (int, float)) for w in weight)):
        raise TypeError("height and weight must be lists of int or float")
    if (len(height) != len(weight)):
        raise ValueError("height and weight must have the same length")
    return [w / (h ** 2) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Returns a list of boleans indicating if the BMI is above the limit"""
    if (not isinstance(bmi, list) or
            not all(isinstance(i, (int, float)) for i in bmi)):
        raise TypeError("bmi must be a list of int or float")
    if (not isinstance(limit, int)):
        raise TypeError("limit must be an int")
    return list(np.array(bmi) > limit)
