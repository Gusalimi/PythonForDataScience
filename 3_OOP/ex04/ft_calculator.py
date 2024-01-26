class calculator:
    """Calculation between 2 vectors"""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Dot product between 2 vectors"""
        print(f"Dot product is: {sum([x * y for x, y in zip(V1, V2)])}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Addition between 2 vectors"""
        print(f"Add Vector is : {[float(x + y) for x, y in zip(V1, V2)]}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Substraction between 2 vectors"""
        print(f"Sous Vector is: {[float(x - y) for x, y in zip(V1, V2)]}")
