def showEmployee(name, salary=9000):
    print(f"Name: {name} salary: {salary}")

def inner_fun(a, b):
    return a + b

def outer_fun(a, b):
    return inner_fun(a, b) + 5

def main():
    try:
        input_func = raw_input  #python2
    except NameError:
        input_func = input  #python3

    while True:
        try:
            m = int(input_func("Enter integer m: "))
            n = int(input_func("Enter integer n: "))
            break
        except ValueError:
            print("Please enter a valid integer")
        except Exception as e:
            print(f"Error: {e}")

    showEmployee("Ben", 12000)
    showEmployee("Jessa")

    result = outer_fun(5, 10)
    print(result)
    print(f"m + n + 5 = {m} + {n} + 5 = {outer_fun(m, n)}")

if __name__=="__main__":
    main()