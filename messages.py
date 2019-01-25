names = input('Enter the list of names : ') # get and process input for a list of names
assignments =  input('Enter list of missing assignment counts : ') # get and process input for a list of the number of assignments
grades = input('Enter list of grades : ') # get and process input for a list of grades

names = [name for name in names.split(',')]
assignments = [int(num) for num in assignments.split(',')]
grades = [int(num) for num in grades.split(',')]

print(names)

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for (name, assignment, grade) in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, grade + 2*assignment))