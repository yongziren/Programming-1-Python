#Programming I

##########################
#      Mission 2.2       #
#     Fix Those Bugs     #
##########################

#Background
#==========
#With Tom's newfound interest in Python programming, he decided to create
#the following program to calculate body mass index and basal metabolic rate.
#However, he is getting frustrated with the errors that he is facing with it.
#Maybe you can help him out? :)

#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.

#START CODING FROM HERE
#======================

#Calculate BMI
weight = float(input('Enter weight(kg): '))
height = float(input('Enter height(m): '))

bmi = weight / height**2

print('BMI: ', bmi)

#Calculate BMR
age = float(input('Enter age(years): '))
New = height*100
bmr =  10 * weight + 6.25 * New - 5 * age + 5

print('BMR: ', bmr)

