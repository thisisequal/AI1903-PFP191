def func1(*args):
    print("Printing values")
    for arg in args:
        print(arg)

def calculation(a, b):
    return a + b, a - b

def main():
    try:
        input_func = raw_input #python2
    except NameError:
        input_func = input  #python3

    func1(20, 40, 60)
    func1(80, 100)

    arr = input_func("Enter the arguments for the variable length function, separated by space: ").split()
    func1(*arr)

    res = calculation(40, 10)
    print(res)

    while True:
        try:
            a = float(input_func("Enter the first number: "))
            b = float(input_func("Enter the second number: "))
            print(calculation(a, b))
            break
        except ValueError:
            print("Please enter valid numbers")
        except Exception as e:
            print(f"Error: {e}")

if __name__=="__main__":
    main()