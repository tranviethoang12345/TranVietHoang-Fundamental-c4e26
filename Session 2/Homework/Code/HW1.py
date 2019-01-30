cm = int(input('Pls enter your height: '))
kg = int(input('Pls enter your weight: '))

m = cm / 100
BMI = kg / (m * m)

print('This is your BMI:', BMI)

if BMI < 16:
    print('Based on the BMI, I can tell you that you are severely underweight')
elif BMI < 18.5:
    print('Based on the BMI, I can tell you that you are underweight')
elif BMI < 25:
    print('Based on the BMI, I can tell you that you are normal')
elif BMI < 30:
    print('Based on the BMI, I can tell you that you are overweight')
else:
    print('Based on the BMI, I can tell you that you are obese')
