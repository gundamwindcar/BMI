h = input (' Please enter your height (cm):')
w = input (' Please enter your weight (kg):')
h = int(h)
w = int(w)
h = h / 100
BMI = w / ( h * h )
if BMI < 18.5:
    print ('Your BMI is ', BMI, 'Underweight')
elif BMI >= 18.5 and BMI < 24:
    print ('Your BMI is ', BMI, 'Normal') 
elif BMI >= 24 and BMI < 27:
    print ('Your BMI is ', BMI, 'Overweight')
elif BMI >= 27 and BMI < 30:
    print ('Your BMI is ', BMI, 'Mild obesity')
elif BMI >= 30 and BMI < 35:
    print ('Your BMI is ', BMI, 'Moderate obesity')
elif BMI >= 35:
    print ('Your BMI is ', BMI, 'Severe obesity')
