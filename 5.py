# 5a. ATM Withdrawal with Exception Handling
balance = 5000

try:
    amt = int(input("Enter amount to withdraw: "))
    if amt > balance:
        raise ValueError("Insufficient Balance! ")
    if amt <= 0:
        raise ValueError("Invalid Amount! ")
    balance -= amt
    print(f"Withdrawal Successful! New Balance: {balance}")
except ValueError as e:
    print(f"Error: {e}")


# 5b. File Operations for Employee Details
def file_ops():
    # Write
    with open("emp.txt", "w") as f:
        f.write("ID: 101, Name: Alice\n")
    
    # Append
    with open("emp.txt", "a") as f:
        f.write("ID: 102, Name: Bob\n")
    
    # Read
    with open("emp.txt", "r") as f:
        print("\nEmployee Details from File:\n" + f.read())

file_ops()

