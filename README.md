Addition Drill Generator
Description
This Python program generates a customizable addition drill worksheet in PDF format, complete with a solutions page. Users can specify the number of digits for the addition problems (e.g., 1-digit, 2-digit, 3-digit) and the grid size (e.g., 5x5, 6x6). The worksheet includes an extra row and column for calculating totals, enhancing the learning experience. The program is designed to be user-friendly, with options to use default settings or customize the drill, and includes robust error handling and an exit option at any input stage.
Requirements

Python 3.x
reportlab library

Installation
To install the required reportlab library, run the following command:
pip install reportlab

Usage

Run the script:python addition_drill_generator.py


Follow the prompts:
Choose whether to use default settings (2-digit addition, 5x5 grid) by entering 'y' or 'n'.
If you choose 'n', enter the desired number of digits and grid size when prompted.
Type 'exit' at any prompt to quit the program.


A PDF named addition_drill_X.pdf (where X is an incrementing serial number) will be generated in the current directory.

Features

Customizable Settings: Choose the number of digits and grid size for the addition problems.
Default Option: Quickly generate a 2-digit, 5x5 grid drill.
Totals Row and Column: An extra row and column are included for calculating totals of the sums.
Problem and Solution Pages: The PDF contains a problem page with blank cells and a solution page with all sums and totals filled in.
Error Handling: The program gracefully handles invalid inputs and ensures only valid data is accepted.
Exit Option: Type 'exit' at any input prompt to terminate the program.

File Naming
Each generated PDF is automatically named with an incrementing serial number, such as addition_drill_1.pdf, addition_drill_2.pdf, etc., based on existing files in the directory.
License
[Optional: Add a license if applicable]
