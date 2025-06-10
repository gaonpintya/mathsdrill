📚 Addition Drill Generator
This Python program creates engaging addition drill worksheets in PDF format, complete with a solutions page. Perfect for students, educators, or anyone looking to practice math skills! Customize the number of digits (e.g., 1-digit, 2-digit) and grid size (e.g., 5x5, 6x6), with features like totals for rows and columns.

🚀 Features

Customizable Settings: Select the number of digits and grid size for your addition problems.
Default Option: Instantly generate a 2-digit, 5x5 grid drill.
Totals Row & Column: Includes an extra row and column to calculate totals of the sums.
Problem & Solution Pages: Get a problem page with blank cells and a solution page with all answers.
Error Handling: Safely handles invalid inputs with clear error messages.
Exit Option: Type exit at any prompt to stop the program.


🛠️ Requirements

Python 3.x
reportlab library

Install reportlab using:
pip install reportlab


📝 Usage

Run the script:python addition_drill_generator.py


Follow the prompts:
Choose default settings (2-digit addition, 5x5 grid) by entering y or n.
If n, enter the number of digits and grid size.
Type exit at any prompt to quit.


A PDF named addition_drill_X.pdf (where X is an incrementing serial number) will be generated in the current directory.


💾 File Naming
Each PDF is automatically named with an incrementing serial number (e.g., addition_drill_1.pdf, addition_drill_2.pdf), based on existing files in the directory.

📜 License
[Optional: Add a license if applicable]
