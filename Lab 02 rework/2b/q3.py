def print_in_binary(n):
    print(f"Binary number format of {n}: {n:b}")

def digits_sum(n):
    result = 0
    for d in str(n):
        result += int(d)
    return result

def reverse(n):
    return int(str(n)[::-1])

def main():
    try:
        input_func = raw_input
    except NameError:
        input_func = input
    
    while True:
        try:
            n = int(input_func("Enter an integer number n: "))
            break
        except ValueError:
            print("Please enter a valid integer.")
        except Exception as e:
            print(f"Error: {e}")
    
    print_in_binary(n)

    n = int(input_func("Re-enter the integer number: "))
    print(f"Sum of digits of {n}: {digits_sum(n)}")
    m = reverse(n)
    print(f"Reverse of {n}: {m}")

if __name__=="__main__":
    main()