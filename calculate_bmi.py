weight = 57.0
height = 1.73

def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
calculate_bmi(weight,height)

#Add code here to calculate BMI
bmi = weight/(height*height)
#Add code here to display calculate BMI
print("BMI = " +str(bmi) )
#Display BMI range

if (bmi < 18.5):
    print("Under Weight")
elif (bmi > 25.0):
    print("Over Weight")
else:
    print("Normal Weight")