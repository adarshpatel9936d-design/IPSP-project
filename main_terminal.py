from number_theory_logic import *

def print_menu():
    print("\n--- Number Theory Toolkit ---")
    print("1. Calculate GCD (Greatest Common Divisor)")
    print("2. Generate Prime Numbers up to n")
    print("3. Calculate Prime Factorization")
    print("4. Check for Armstrong Number")
    print("5. Check for Palindrome")
    print("6. Generate Fibonacci Sequence")
    print("7. Exit")
    print("-------------------------------")

def get_integer_input(msg):
    while True:
        try:
            inp = input(msg)
            val = int(inp)
            return val
        except ValueError:
            print("Error: '" + inp + "' is not a valid integer. Please try again.")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            n1 = get_integer_input("Enter Number A: ")
            n2 = get_integer_input("Enter Number B: ")
            result = calculate_gcd(n1, n2)
            print("Result: GCD(" + str(n1) + ", " + str(n2) + ") = " + str(result))
            
        elif choice == '2':
            l = get_integer_input("Enter upper limit (n): ")
            primes_list = generate_primes_up_to(l)
            print("Primes up to " + str(l) + ":")
            print(primes_list)
            
        elif choice == '3':
            n = get_integer_input("Enter number (n): ")
                
            f_dict = calculate_prime_factorization(n)
            
            if not f_dict:
                print("Result: " + str(n) + " has no prime factors (or is 0 or 1).")
            else:
                parts = []
                for b, e in f_dict.items():
                    parts.append(str(b) + "^" + str(e))
                
                out_str = " * ".join(parts)
                print("Result: " + str(n) + " = " + out_str)
                
        elif choice == '4':
            n = get_integer_input("Enter number (n): ")
                
            is_arm = is_armstrong_number(n)
            if is_arm:
                print("Result: YES, " + str(n) + " is an Armstrong number.")
            else:
                print("Result: NO, " + str(n) + " is not an Armstrong number.")
                
        elif choice == '5':
            n = get_integer_input("Enter number to check: ")
                
            is_pal = is_palindrome(n)
            if is_pal:
                print("Result: YES, '" + str(n) + "' is a palindrome.")
            else:
                print("Result: NO, '" + str(n) + "' is not a palindrome.")
                
        elif choice == '6':
            count = get_integer_input("Enter number of terms (n): ")
            
            if count < 0:
                print("Error: Please enter a non-negative integer.")
                input("\nPress Enter to return to the menu...")
                continue # Go back to the start of the loop
                
            fib_seq = generate_fibonacci_sequence(count)
            print("Sequence with " + str(count) + " terms:")
            print(fib_seq)
                
        elif choice == '7':
            print("Exiting toolkit. Goodbye!")
            break # Exit the while loop
        else:
            print("Invalid choice '" + choice + "'. Please select a number from 1 to 7.")
            
        # This will run for choices 1-6 and invalid choices
        input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    main()