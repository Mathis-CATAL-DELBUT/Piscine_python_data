class calculator:
    """Calculator class"""

    def __init__(self, lst) -> None:
        """Method docstring (calculator)"""
        self.lst = lst

    def __add__(self, nb) -> None:
        """Addition between a list and a number"""
        self.lst = [nb + self.lst[i] for i in range(len(self.lst))]
        print(self.lst)

    def __mul__(self, nb) -> None:
        """Multiplication between a list and a number"""
        self.lst = [nb * self.lst[i] for i in range(len(self.lst))]
        print(self.lst)

    def __sub__(self, nb) -> None:
        """Substraction between a list and a number"""
        self.lst = [self.lst[i] - nb for i in range(len(self.lst))]
        print(self.lst)

    def __truediv__(self, nb) -> None:
        """Division between a list and a number"""
        if nb == 0:
            print("Error: Division by zero")
            return
        self.lst = [self.lst[i] / nb for i in range(len(self.lst))]
        print(self.lst)
