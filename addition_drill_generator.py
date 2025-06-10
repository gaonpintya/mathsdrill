import random
import os
import re
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm

# Function to get the next serial number for the file name
def get_next_serial():
    files = os.listdir('.')
    pattern = r'addition_drill_(\d+)\.pdf'
    numbers = []
    for file in files:
        match = re.match(pattern, file)
        if match:
            numbers.append(int(match.group(1)))
    return max(numbers) + 1 if numbers else 1

# Function to get user input with exit option
def get_user_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == 'exit':
            print("Exiting the program.")
            exit()
        return user_input

# Function to get integer input with validation
def get_integer_input(prompt):
    while True:
        user_input = get_user_input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input. Please enter a positive integer or 'exit' to quit.")

# Prompt user for settings with validation
while True:
    use_default = get_user_input("Do you want to use default settings (2-digit addition, 5x5 grid)? (y/n): ")
    if use_default in ['y', 'n']:
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

if use_default == 'y':
    digit_length = 2
    grid_size = 5
else:
    digit_length = get_integer_input("Enter the number of digits for the addition table: ")
    grid_size = get_integer_input("Enter the grid size (e.g., 5 for 5x5): ")

# Determine the range for random numbers based on digit_length
if digit_length == 1:
    lower = 0
else:
    lower = 10 ** (digit_length - 1)
upper = 10 ** digit_length - 1

# Generate random numbers for the top row and first column
top_row = [random.randint(lower, upper) for _ in range(grid_size)]
first_column = [random.randint(lower, upper) for _ in range(grid_size)]

# Create problem data
problem_data = [['' for _ in range(grid_size + 2)] for _ in range(grid_size + 2)]
problem_data[0][0] = ''
for j in range(grid_size):
    problem_data[0][j + 1] = str(top_row[j])
problem_data[0][grid_size + 1] = 'Total'
for i in range(grid_size):
    problem_data[i + 1][0] = str(first_column[i])
problem_data[grid_size + 1][0] = 'Total'
# Inner cells and total cells remain blank

# Create solution data
solution_data = [['' for _ in range(grid_size + 2)] for _ in range(grid_size + 2)]
solution_data[0][0] = ''
for j in range(grid_size):
    solution_data[0][j + 1] = str(top_row[j])
solution_data[0][grid_size + 1] = 'Total'
for i in range(grid_size):
    solution_data[i + 1][0] = str(first_column[i])
solution_data[grid_size + 1][0] = 'Total'

# Fill inner cells with sums
for i in range(1, grid_size + 1):
    for j in range(1, grid_size + 1):
        sum_value = first_column[i - 1] + top_row[j - 1]
        solution_data[i][j] = str(sum_value)

# Fill row totals (excluding the first column)
for i in range(1, grid_size + 1):
    row_sum = sum(int(solution_data[i][j]) for j in range(1, grid_size + 1))
    solution_data[i][grid_size + 1] = str(row_sum)

# Fill column totals (excluding the first row)
for j in range(1, grid_size + 1):
    col_sum = sum(int(solution_data[i][j]) for i in range(1, grid_size + 1))
    solution_data[grid_size + 1][j] = str(col_sum)

# Fill grand total
grand_total = sum(int(solution_data[i][grid_size + 1]) for i in range(1, grid_size + 1))
solution_data[grid_size + 1][grid_size + 1] = str(grand_total)

# Define table style with shading
table_style = TableStyle([
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('FONTNAME', (1, 0), (grid_size, 0), 'Helvetica-Bold'),  # Top row numbers
    ('FONTNAME', (0, 1), (0, grid_size), 'Helvetica-Bold'),  # First column numbers
    ('FONTNAME', (grid_size + 1, 0), (grid_size + 1, 0), 'Helvetica-Bold'),  # 'Total' in top row
    ('FONTNAME', (0, grid_size + 1), (0, grid_size + 1), 'Helvetica-Bold'),  # 'Total' in first column
    ('BACKGROUND', (1, 0), (grid_size, 0), colors.lightgrey),  # Shading for top row numbers
    ('BACKGROUND', (0, 1), (0, grid_size), colors.lightgrey),  # Shading for first column numbers
    ('INNERGRID', (1, 1), (grid_size, grid_size), 0.5, colors.grey),  # Lighter grid for inner cells
    ('BOX', (0, 0), (-1, -1), 1, colors.black),
    ('PADDING', (0, 0), (-1, -1), 5),  # Add padding to cells
])

# Get the next serial number and set file name
serial_number = get_next_serial()
file_name = f"addition_drill_{serial_number}.pdf"

# Create the PDF
doc = SimpleDocTemplate(file_name, pagesize=A4, topMargin=20*mm, bottomMargin=20*mm)
elements = []
styles = getSampleStyleSheet()

# Custom styles for heading and digit info
heading_style = ParagraphStyle(name='Heading', fontName='Helvetica-Bold', fontSize=16, alignment=1, spaceAfter=6)
digit_info_style = ParagraphStyle(name='DigitInfo', fontName='Helvetica', fontSize=12, alignment=1, spaceAfter=12)

# Add heading and digit info for problem page
heading = Paragraph(f"Addition Drill #{serial_number}", heading_style)
elements.append(heading)
digit_info = Paragraph(f"{digit_length}-Digit Addition", digit_info_style)
elements.append(digit_info)

# Add instructions
instructions = Paragraph(
    "Add the numbers from the top row and the first column and write the sum in the corresponding cell. "
    "Calculate the totals for each row and column, excluding the numbers in the first row and first column.",
    styles['Normal']
)
elements.append(instructions)
elements.append(Spacer(1, 12*mm))

# Create problem table
col_widths = [60] * (grid_size + 2)
row_heights = [60] * (grid_size + 2)
problem_table = Table(problem_data, colWidths=col_widths, rowHeights=row_heights)
problem_table.setStyle(table_style)
elements.append(problem_table)

# Add page break
elements.append(PageBreak())

# Add heading and digit info for solutions page
elements.append(heading)
elements.append(digit_info)

# Add solutions title
solutions_title = Paragraph("Solutions", styles['Normal'])
elements.append(solutions_title)
elements.append(Spacer(1, 12*mm))

# Create solution table
solution_table = Table(solution_data, colWidths=col_widths, rowHeights=row_heights)
solution_table.setStyle(table_style)
elements.append(solution_table)

# Build the PDF
doc.build(elements)

print(f"PDF generated: {file_name}")