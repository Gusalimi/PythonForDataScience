class calculator:
    """Calculate vector with scalar"""
    def __init__(self, vec) -> None:
        if (not isinstance(vec, list)):
            raise TypeError("passed value must be a list")
        self._vec = vec

    def __add__(self, object) -> None:
        self._vec = [x + object for x in self._vec]
        print(self._vec)

    def __mul__(self, object) -> None:
        self._vec = [x * object for x in self._vec]
        print(self._vec)

    def __sub__(self, object) -> None:
        self._vec = [x - object for x in self._vec]
        print(self._vec)

    def __truediv__(self, object) -> None:
        if (object == 0):
            raise ZeroDivisionError("division by zero")
        self._vec = [x / object for x in self._vec]
        print(self._vec)
