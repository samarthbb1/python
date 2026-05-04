# 4a. Add Two Complex Numbers (Operator Overloading)
class ComplexNum:
    def __init__(self, r, i):
        self.r, self.i = r, i

    def __add__(self, other):
        return ComplexNum(self.r + other.r, self.i + other.i)

    def __str__(self):
        return f"{self.r} + {self.i}j"

# Asking the user for input
print("--- Enter first complex number ---")
r1 = float(input("Enter real part: "))
i1 = float(input("Enter imaginary part: "))

print("\n--- Enter second complex number ---")
r2 = float(input("Enter real part: "))
i2 = float(input("Enter imaginary part: "))

# Creating objects with user data
c1 = ComplexNum(r1, i1)
c2 = ComplexNum(r2, i2)

# Displaying the result
print(f"\nResult of Addition: {c1 + c2}")










# 4b. Multiple Inheritance (Online Shopping System)
class Product:
    def __init__(self, name):
        self.name = name
    def p_info(self): 
        print(f"Product: {self.name}")

class Discount:
    def __init__(self, rate):
        self.rate = rate
    def d_info(self): 
        print(f"Discount: {self.rate}%")

class Order(Product, Discount):
    def __init__(self, name, rate):
        Product.__init__(self, name)
        Discount.__init__(self, rate)
    
    def show(self):
        self.p_info()
        self.d_info()

def run_program():
    try:
        # 1. Validate Product Name
        prod_name = input("Enter product name: ").strip()
        if not prod_name:
            raise ValueError("Product name cannot be empty.")

        # 2. Validate Discount Rate (Type and Range)
        rate_input = input("Enter discount percentage (0-100): ")
        disc_rate = float(rate_input) # May raise ValueError if not a number
        
        if disc_rate < 0 or disc_rate > 100:
            raise ValueError("Discount must be between 0 and 100.")

        # If all checks pass, create the object
        order = Order(prod_name, disc_rate)
        print("\n--- Order Summary ---")
        order.show()

    except ValueError as e:
        # Handles non-numeric inputs or custom range errors
        print(f"Input Error: {e}")
    except KeyboardInterrupt:
        # Handles cases where user stops the program (e.g., Ctrl+C)
        print("\nProgram stopped by user.")
    except Exception as e:
        # Catch-all for any other unexpected failures
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_program()

