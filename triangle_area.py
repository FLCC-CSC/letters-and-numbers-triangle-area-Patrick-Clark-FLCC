# FILE NAME - triangle_area.py

# NAME: Patrick Clark
# DATE: 2/23/2025
# BRIEF DESCRIPTION: This code will ask the user two dimensions of a triangle (height and base), then output the area of the triangle descibed by the user.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions below
# 4. The Sample Output has been included in this code for your convenience





########## ENTER YER CODE BELOW THIS LINE ##########

height_triangle = int(input('Enter the height: '))
base_triangle = int(input('Enter the base: \n'))   
area_triangle = (height_triangle * base_triangle)/2

print(f'The area of the triangle is {area_triangle}')  

########### END YER CODE ABOVE THIS LINE ###########





########################################
#          SAMPLE OUTPUT
########################################

'''

Enter the height: 1
Enter the base: 1

The area of the triangle is 0.5

'''



'''

Enter the height: 8
Enter the base: 4

The area of the triangle is 16.0

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is the flow of the program? Which line of code kicks off the process?
# The flow of the program is to ask the user for the height of the triangle, then ask the user for the base of the triangle. After this, the code outputs a message
# including the area of the triangle described. The line of code that kicks off this process is the first line of code "height_triangle = int(input('Enter the height '))".
# This line asks the user to enter the height value and saves it as an integer.




2. What was the hardest part of this lab?
#For me, it was to remember that the user values needed to be saved as integers at first. This allowed the math to work.




'''
