# Write a program to calculate the grade of a student from his marks from the following grading system

'''

Grade	Scale	        Scale 2	            US Grade

A+	    5.00	        80.00 - 100.00	    A+
A	    4.00 - 4.99	    70.00 - 79.99	    A
A-	    3.50 - 3.99	    60.00 - 69.99	    A-
B	    3.00 - 3.49	    50.00 - 59.99	    B
C	    2.00 - 2.99	    40.00 - 49.99	    C
D	    1.00 - 1.99	    33.00 - 39.99	    D
F	    0.00 - 0.99	    0.00 - 32.99	    F

'''

mark = int(input("Enter mark: "))

if (0 <= mark <= 32):
    print("Grade: F")

elif (33 <= mark <= 39):
    print("Grade: D")

elif (40 <= mark <= 49):
    print("Grade: C")

elif (50 <= mark <= 59):
    print("Grade: B")

elif (60 <= mark <= 69):
    print("Grade: A-")

elif (70 <= mark <= 79):
    print("Grade: A")

elif (80 <= mark <= 100):
    print("Grade: A+")
else:
    print("INVALID INPUT. ¯\_(ツ)_/¯ ")
