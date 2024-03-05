def multi(a, b):
    print(f"The result is {a * b}")

def addition(a, b):
    print(f"The result is {a + b}")

def main():
    try:
        input_func = raw_input
    except NameError:
        input_func = input

    print("number1 = 20")
    print("number2 = 30")
    print("Multiplication")
    multi(20, 30)
    print("Addition")
    addition(20, 30)

    while True:
        try:
            n = int(input_func("Enter integer n: "))
            break
        except ValueError:
            print("Please enter a valid integer")
        except Exception as e:
            print(f"Error: {e}")
            
    print(f"Printing current and previous number sum in a range({n + 1})")
    for i in range(1, n + 1):
        current = i
        previous = i - 1 if i > 1 else 0
        print(f"Current number: {current}  Previous number: {previous}  Sum: {current + previous}")

    print("Name", "Is", "James", sep="**")
if __name__=="__main__":
    main()     
