    # project
    #### Video Demo:  <https://youtu.be/5BJd3MH-vzc>
    #### Description:  Building a Simple Calculator in Python

Introduction:

In the world of programming, creating a simple calculator is often one of the first projects that beginners undertake. It's an excellent way to learn about basic programming constructs like loops, conditionals, functions, and user input handling. In this project, we'll explore a Python program that implements a straightforward calculator with four fundamental operations: addition, subtraction, multiplication, and division. This project serves as an educational example of how to design and build a simple console-based application.

Project Structure:

The project consists of a single Python script organized into the following key components:

Main Function (main()):

The program starts execution from the main() function.
It employs a while loop to create an interactive user interface that keeps running until the user decides to exit.
The user is presented with a menu of choices: add, subtract, multiply, divide, or exit.
The program takes user input to determine the operation to perform.
Mathematical Operations Functions:

Four separate functions are defined for each of the basic mathematical operations: add(), subtract(), multiply(), and divide().
These functions take two numbers as input and return the result of the corresponding operation.
For division, the program handles the special case of division by zero to prevent errors.
User Interaction:

The heart of this calculator project lies in its user interaction. Let's break down how it engages with the user:

Menu Presentation:

The user is presented with a clear menu displaying the available operations.
This menu makes it easy for users to understand their choices.
User Input Handling:

The program uses the input() function to gather user input.
It takes the user's choice and the two numbers to perform the selected operation.
It includes error handling for invalid inputs, such as non-numeric inputs or choosing an option outside the menu.
Operation Execution:

Depending on the user's choice, the program calls the corresponding mathematical operation function and displays the result.
Exit Option:

The user can choose to exit the program, ending the loop and displaying a goodbye message.
Error Handling:

The program includes some basic error handling to enhance user experience and prevent crashes:

It checks for division by zero when performing division and displays an error message if the denominator is zero.
If the user enters an invalid choice, it provides an error message and allows the user to try again.
Conclusion:

This simple calculator project in Python demonstrates the fundamental principles of programming and user interaction. It serves as an excellent starting point for beginners to learn about concepts like functions, loops, conditionals, and input handling. Moreover, it showcases the importance of error handling to ensure the program behaves gracefully in the face of unexpected inputs or errors.

While this calculator is a basic implementation, it can be expanded and improved upon in numerous ways. For example, you could add more mathematical functions, handle more complex expressions, or create a graphical user interface (GUI) for a more user-friendly experience. Nonetheless, this project provides a solid foundation for aspiring programmers to build upon as they continue to explore the world of Python and software development.