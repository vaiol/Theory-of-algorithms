class Karatsuba:
    count = 0  # how many times the value encountered
    value = 0  # the desired value
    def getCount(self, number1, number2, value):
        """ Return how many times the desired value
        in the intermediate calculations.
        Necessary condition for the task.
        """
        self.count = 0
        self.value = value
        self.karatsuba(number1, number2)
        return self.count

    def karatsuba(self, number1, number2):
        """ Recursive multiplication using karatsuba method
        x = 10^n/2 * a + b
        y = 10^n/2 * c + d
        x * y = 10^n * ac + 10^(n/2) (ad+bc) + bd
        where (ad+bc) = (a+b)(c+d) - ac - bd
        """
        if number1 <= 10 and number2 <= 10:
            return number1 * number2
        number1 = str(number1)
        number2 = str(number2)

        maxLen = max(len(number1), len(number2))
        n = self.getDegree(2, maxLen)

        number1 = self.toLength(number1, n)
        number2 = self.toLength(number2, n)
        a = int(number1[0:n/2])
        b = int(number1[(n/2):n])
        c = int(number2[0:n/2])
        d = int(number2[(n/2):n])

        ac = self.karatsuba(a, c)
        bd = self.karatsuba(b, d)
        ad_bc = self.karatsuba(a+b, c+d) - ac - bd
        if ad_bc == self.value:
            self.count += 1
        sum1 = (10**n * ac)
        sum2 = ((10**(n/2)) * ad_bc)

        return sum1 + sum2 + bd

    @staticmethod
    def toLength(number, n):
        """
        Trim to length
        :param number: string, which need to trim
        :param n: trim length
        :return: string after trim
        """
        while len(number) < n:
            number = '0' + number
        return number

    @staticmethod
    def getDegree(n, len):
        """
        :param n: start degree of 2
        :param len: length of string
        :return: necessary degree of 2
        """
        i = 2
        while len > n:
            n = 2**i
            i += 1
        return n


# test
a = 1685287499328328297814655639278583667919355849391453456921116729
b = 7114192848577754587969744626558571536728983167954552999895348492
multi = Karatsuba()

print(multi.getCount(a, b, 105))
print(multi.getCount(a, b, 72))
print(multi.getCount(a, b, 12))
print(multi.karatsuba(a, b))
print a * b