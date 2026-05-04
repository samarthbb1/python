#1a.
marks = [85, 90, 78] # Example marks
total = sum(marks)
avg = total / len(marks)

# Grading logic
if avg >= 90: 
    grade = 'A'
elif avg >= 75: 
    grade = 'B'
else: grade = 'C'

print(f"Total: {total}, Average: {avg:.2f}, Grade: {grade}")





#1b.
stored_pw = "secret123"
attempt = input("Enter password: ")

if attempt == stored_pw:
    print("Access Granted “)
else:
    print("Access Denied ")

