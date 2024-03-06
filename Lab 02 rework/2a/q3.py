import time
import re

def addition_recursive(n):
    if n == 0:
        return 0
    return n + addition_recursive(n-1)

def addition_formula(n):
    return n * (n+1) / 2

def addition_loop(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result

def display_student(name, age):
    print(name, age)

def main():
    try:
        input_func = raw_input  #python2
    except NameError:
        input_func = input  #python3

    show_student = display_student

    display_student("Emma", 26)
    show_student("Emma", 26)

    print(f"Addition using formula: {addition_formula(10)}")
    print(f"Addition using loop: {addition_loop(10)}")
    print(f"Addition using recursive: {addition_recursive(10)}")

    print("User-inputted section")
    pattern = "\A[A-Z][a-z]+\Z"
    student_name = input_func("Enter student name: ")
    while True:
        if not re.match(pattern, student_name):
            student_name = input_func("Please enter a valid name: ")
            continue
        break
    
    while True:
        try:
            student_age = int(input_func("Enter student age: "))
        except ValueError:
            print("Please enter a valid integer")
            continue
        except Exception as e:
            print(f"Error: {e}")
        if student_age > 100:
            print("Number entered too high, please enter a reasonable age number")
            continue
        if student_age < 6:
            print("Number entered too low, please enter a reasonable age number")
            continue
        break
    
    print("display_student")
    display_student(student_name, student_age)
    print("show_student")
    show_student(student_name, student_age)

    while True:
        try:
            n = int(input_func("Enter integer n: "))
            break
        except ValueError:
            print("Please enter a valid integer")
        except Exception as e:
            print(f"Error: {e}")

    t0 = time.time()
    formula = addition_formula(n)
    print(f"Addition using formula with n = {formula}")
    time.sleep(0.5)
    t1 = time.time()
    dt1 = t1 - t0 - 0.5
    t0 = time.time()
    loop = addition_loop(n)
    print(f"Addition using loop with n = {loop}")
    time.sleep(0.5)
    t1 = time.time()
    dt2 = t1 - t0 - 0.5
    try: 
        t0 = time.time()
        recursion = addition_recursive(n)
        print(f"Addition using recursive with n = {recursion}")
        time.sleep(0.5)
        t1 = time.time()
        dt3 = t1 - t0 - 0.5
    except RecursionError:
        print("n too big to use recursion. Please keep n < 990")
        t1 = None

    print(f"Formula execution time: {dt1*1000} ms")
    print(f"Loop execution time: {dt2*1000} ms")
    if bool(t1):
        print(f"Recursion execution time: {dt3*1000} ms")

if __name__=="__main__":
    main()

