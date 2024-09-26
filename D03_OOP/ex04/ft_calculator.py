class calculator:
    """"""

    def __init__(self) -> None:
        pass

    @classmethod
    def dotproduct(cls, V1: list[float], V2: list[float]) -> None:
        """"""
        total = 0
        for i in range(len(V1)):
            total += V1[i] * V2[i]
        print(f"Dot product is: {total}")

    @classmethod
    def add_vec(cls, V1: list[float], V2: list[float]) -> None:
        """"""
        print(f"Add Vector is : {[V1[i] + V2[i] for i in range(len(V1))]}")

    @classmethod
    def sous_vec(cls, V1: list[float], V2: list[float]) -> None:
        """"""
        print(f"Sous Vector is: {[V1[i] - V2[i] for i in range(len(V1))]}")
