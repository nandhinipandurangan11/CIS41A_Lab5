# CIS41A: Lab5: Named Tuples and Iterators: Nandhini Pandurangan
# This program uses 3 named tuples to convert an integer into a roman numeral
# This program makes use of comprehensions, maps, and joins

"""
Using these lists:

     ones = [ "I","II","III","IV","V","VI","VII","VIII","IX" ]
     tens = [ "X", "XX","XXX", "XL", "L", "LX", "LXX", "LXXX", "XC" ]
     hundreds = [ "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM","M" ]

Convert these list to named tuples and store them in a class. Then write a member function(s)
for the class to convert a 'int' to a 'roman numeral'. in the range of 1 to 1000.
Use comprehensions, map, reduce or join where appropriate.
"""

import collections


class Roman_Int():
    def __init__(self):
        """ Constructor creates 3 named tuples to hold ones, tens, and hundreds roman numerals """

        # creating named tuples for ones, tens, and hundreds list
        self.Ones = collections.namedtuple('Ones', ['o1', 'o2', 'o3', 'o4', 'o5', 'o6', 'o7', 'o8', 'o9'])
        self.o = self.Ones("I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX")

        self.Tens = collections.namedtuple('Tens', ['t10', 't20', 't30', 't40', 't50', 't60', 't70', 't80', 't90', ])
        self.t = self.Tens("X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC")

        self.Hundreds = collections.namedtuple("Hundreds", ['h100', 'h200', 'h300', 'h400', 'h500', 'h600', 'h700',
                                                            'h800', 'h900', 'h1000', ])
        self.h = self.Hundreds("C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM", "M")

    def return_ones(self, ones_digit):
        """ Uses a comprehension to return the matching roman numeral for the ones digit"""

        if ones_digit > 0:
            # making a list to hold the roman numeral character that matches the ones_digit
            ones_digit = ([self.o[i] for i in range(len(self.o)) if i + 1 == ones_digit])

            # returning the first element (matching roman numeral) as a string
            return ones_digit[0]

        # if ones digit is zero, return empty string
        else:
            return ""

    def return_tens(self, tens_digit):
        """ Uses a comprehension to return the matching roman numeral for the tens digit"""

        if tens_digit > 0:
            tens_digit = ([self.t[i] for i in range(len(self.t)) if i + 1 == (tens_digit % 10)])

            # returning the first element (matching roman numeral) as a string
            return tens_digit[0]

        # if tens digit is zero, return empty string
        else:
            return ""

    def return_hundreds(self, hundreds_digit):
        """ Uses a comprehension to return the matching roman numeral for the hundreds digit"""

        hundreds_digit = ([self.h[i] for i in range(len(self.h)) if i + 1 == (hundreds_digit % 100)])

        # returning the first element (matching roman numeral) as a string
        return hundreds_digit[0]

    def convert(self, num):
        """Performs input validation and calls appropriate functions to convert from int to roman numeral"""

        original_num = num
        ones_digit = [0]
        tens_digit = [0]
        hundreds_digit = [0]

        # input validation
        if num <= 0:
            print("Out of range")

        # if the number is 1000, return the roman numeral equivalent to 1000
        elif num == 1000:
            print(self.h.h1000)

        # else the number is between 0 and 999
        else:
            remainder = []

            # appending the ones, tens, and hundreds digits to remainder list
            while num > 0:
                remainder.append(num % 10)
                num = num // 10

            # creating an iterable with only one element: the ones, tens, or hundreds digit
            # each of the following 3 variables is a list with one element
            # this is so because we want to be able to use map() on them

            ones_digit = [remainder[0]]

            if original_num >= 10:
                tens_digit = [remainder[1]]

            if original_num >= 100:
                hundreds_digit = [remainder[2]]

            # using the map built-in to append to the roman list
            # map returns a list, so we are only appending the first element of the list to the roman list
            roman = []

            if original_num >= 100:
                roman.append((list(map(self.return_hundreds, hundreds_digit)))[0])

            if original_num >= 10:
                roman.append((list(map(self.return_tens, tens_digit)))[0])

            roman.append(list(map(self.return_ones, ones_digit))[0])

            # using a separator to join the elements of the roman list
            sep = ""
            numerals = sep.join(roman)
            print(numerals)


# creating a Roman_Int object and calling convert() function with some integer
r = Roman_Int()
r.convert(123)
