# Login-System

A basic command-line login system written in Python that authenticates a user using a predefined username and password.

# Overview

This project demonstrates a simple authentication process in Python. The program prompts the user to enter a username and password and checks the input against predefined credentials.

If the credentials match, the user is granted access. Otherwise, the login attempt fails.

# Features

1.Accepts user input for username and password

2.Validates credentials using a login function

3.Displays success or failure messages

4.Simple and easy-to-understand logic

# How It Works

The program defines a function called login() that compares the user-provided credentials with stored values.

The authentication process follows these steps:

1.The user enters a username.

2.The user enters a password.

3.The program checks if both match the predefined credentials.

A success or failure message is displayed.

# Code Structure

login(username, password)
Checks whether the provided username and password match the stored credentials and returns True or False.
