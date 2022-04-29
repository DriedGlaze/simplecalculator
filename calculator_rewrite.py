def evaluate():
    equation = input("Enter a math equation: ")
    solution = eval(equation)
    print(solution)
    equation2 =  input("Would you like to input another equation?: ")
    if equation2 == "yes":
        evaluate()
    if equation2 == "no":
        "Thanks for using, closing program..."
        equation = input("Enter a math equation: ")
    solution = eval(equation)
    print(equation)


































































evaluate()





























