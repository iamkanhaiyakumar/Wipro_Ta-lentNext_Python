import sys

#  Write a program to accept two numbers as command line arguments and display their sum.

if len(sys.argv) != 3:
    print("Usage: python exercise.py <num1> <num2>")
else:
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        print("Sum:", num1 + num2)
    except ValueError:
        print("Please provide valid numbers.")


# Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.

# Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.
