#format methods

#in this program we will learn to print vavriables using {}

# lets some numbers


number1=300.1345678
number2=2.3456778
number3=20.20204023
number4=23333.45425


# 1st method

print('Lottory number 1 is {0} and second number is {1}'.format(number1,number2))

print('First num is {0:.4} and seond num is {1} and num 3 is {2:.3}' .format(number1,number2,number3))

#fractional points
print('first num is {0:.2f}'.format(number1))

#2nd methods

print(f'the prize number is {number1} and second number is {number2}')

print(f'number first {number1:.4}')
print(f'number first {number1:.4f}')