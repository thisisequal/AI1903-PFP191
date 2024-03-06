def summation(n):
    return n * (n + 1) / 2

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def sum_fraction(n):
    result = 0
    for i in range(1, n + 1):
        result += 1/i
    return result

def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
    return True

def main():
    try:
        input_func = raw_input #python2
    except NameError:
        input_func = input #python3

    while True:
        try:
            n = int(input_func("Enter an integer number n larger than 5: "))
        except ValueError:
            print("Please enter a valid integer number")
        except Exception as e:
            print(f"Error: {e}")

        if n <= 5:
            print("Please enter an integer larger than 5")
            continue
        else:
            break
    
    print(f"S1 = {summation(n)}")
    print(f"S2 = {factorial(n)}")
    print(f"S3 = {sum_fraction(n)}")

    while True:
        try:
            n = int(input_func("Re-enter n: "))
        except ValueError:
            print("Please enter a valid integer number")
        except Exception as e:
            print(f"Error: {e}")

        if n <= 5:
            print("Please enter an integer larger than 5")
            continue
        else:
            break
    
    print(f"{n} is a prime number") if isPrime(n) else print(f"{n} is not a prime number")

if __name__ == "__main__":
    main()