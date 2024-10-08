#v2.0
class Fraction():
    def __init__(self, *args) -> None:
        if isinstance(args[0], str):
            self.__num, self.__den = [int(c) for c in args[0].split('/')]
        else:
            self.__num = args[0]
            self.__den = args[1]
        self.__reduction()

    def __sign(self):
        return -1 if self.__num < 0 else 1

    def __neg__(self) -> 'Fraction':
        return Fraction(-self.__num, self.__den)

    def __gcd(self, a, b) -> int:
        while b:
            a, b = b, a % b
        return abs(a)

    def __reduction(self) -> 'Fraction':
        __gcd = self.__gcd(self.__num, self.__den)
        self.__num //= __gcd
        self.__den //= __gcd

        if self.__den < 0:
            self.__num = -self.__num
            self.__den = abs(self.__den)
        return self

    def __str__(self) -> str:
        return f'{self.__num}/{self.__den}'

    def __repr__(self) -> str:
        return f"Fraction('{self.__num}/{self.__den}')"

    def numerator(self, *args) -> int:
        if len(args):
            self.__num = args[0] * self.__sign()
            self.__reduction()
        return abs(self.__num)

    def denominator(self, *args) -> int:
        if len(args):
            self.__den = args[0]
        self.__reduction()
        return abs(self.__den)



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
