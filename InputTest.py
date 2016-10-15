from pip._vendor.distlib.compat import raw_input

print('hello, this is a calculator')

num1 = raw_input("number1:\t")
num2 = raw_input("number2:\t")
operator = raw_input("operator:\t")

print("%s %s %s=" % (num1, num2, operator))
