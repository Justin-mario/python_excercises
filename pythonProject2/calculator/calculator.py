class Calculator:

    def add(self, num2):
        total = self + num2
        return total


    def subtract(self, num2):
        total = self - num2
        return total


    def divide(self, num2):
        if num2 != 0:
            total = self / num2
            return total
        else:
            raise ZeroDivisionError

    @classmethod
    def multiple(cls, num1, num2):
        total = num1 * num2
        return total


