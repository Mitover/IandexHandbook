class Fraction:
    def __init__(self, *args):
        if isinstance(args[0], str):
            self.__num = int(args[0].split("/")[0])
            self.__den = int(args[0].split("/")[1])
        else:
            self.__num = args[0]
            self.__den = args[1]
        self.reduction()

    def find_gcd(self, a, b):
        while (b != 0):
            a, b = b, a % b
        return a

    def reduction(self):
        gcd = self.find_gcd(self.__num, self.__den)
        self.__num /= gcd
        self.__den /= gcd
        self.__num = int(self.__num)
        self.__den = int(self.__den)
        return self

    def __str__(self):
        return f"{self.__num}/{self.__den}"

    def __repr__(self):
        return f"Fraction('{self.__num}/{self.__den}')"

    def numerator(self, *num2):
        if len(num2):
            self.__num = num2[0]
            self.reduction()
        return abs(self.__num)

    def denominator(self, *den2):
        if len(den2):
            self.__den = den2[0]
            self.reduction()
        return abs(self.__den)
    def __neg__(self):
        return Fraction(-self.__num, self.__den)


# a = Fraction(1, 3)
# b = Fraction(-2, -6)
# c = Fraction(-3, 9)
# d = Fraction(4, -12)
# print(a, b, c, d)
# print(*map(repr, (a, b, c, d)))
print("____________________________")
a = Fraction('-1/2')
b = -a
print(a, b, a is b)
b.numerator(-b.numerator())
a.denominator(-3)
print(a, b)
print(a.numerator(), a.denominator())
print(b.numerator(), b.denominator())
