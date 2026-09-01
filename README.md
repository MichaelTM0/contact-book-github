# Contact Book

A beginner-friendly Python command-line application that allows users to create and manage a simple contact book.

## Features

* Add new contacts
* Prevent duplicate contacts from being added
* View all saved contacts
* Search for a contact by name
* Delete contacts
* Interactive command-line menu
* Input validation for menu selections

## Contact Information

Each contact stores:

* Name
* Phone number
* City
* State

## How It Works

The application uses a Python dictionary to store contacts. Each contact is stored using the contact's name as the key, with the contact's personal information stored in an inner dictionary.

Users can interact with the application through a menu with the following options:

1. Add Contact
2. View Contacts
3. Search Contact
4. Delete Contact
5. Exit

## Technologies Used

* Python 3
* Dictionaries
* Functions
* `while` loops
* `for` loops
* Conditional statements
* User input and validation

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the program with:

```bash
python contact_book.py
```

## Project Status

Version 1.0 — Complete

This project was created as a beginner Python project to practice working with dictionaries, functions, loops, conditionals, and menu-driven command-line applications.

## Future Improvements

Potential improvements for future versions include:

* Save contacts to a CSV file
* Load existing contacts when the program starts
* Edit existing contact information
* Add more contact information fields
* Improve the formatting of displayed contacts
