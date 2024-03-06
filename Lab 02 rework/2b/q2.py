import math

def common_divisor(a, b):
    common_divisors = []
    for i in range(1, max(a, b) + 1):
        if a % i == 0 and b % i == 0:
            common_divisors.append(i)
    return common_divisors

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

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
            m = int(input_func("Enter an integer number m : "))
            n = int(input_func("Enter an integer number n : "))
        
            divisor = common_divisor(m, n)

            print("Printing prime common divisors")
            for i in divisor:
                if isPrime(i):
                    print(f"{i}")
            
            print(f"Greatest common divisor of {m} and {n}: {math.gcd(m, n)}")
            print(f"Least common multiple of {m} and {n}: {lcm(m, n)}")
        
        except ValueError:
            print("Please enter a valid integer number")
        except Exception as e:
            print(f"Error: {e}")
    
if __name__=="__main__":
    main()