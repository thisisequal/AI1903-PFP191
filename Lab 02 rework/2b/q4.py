def is_palindrome(s):
    for i in range(0, int(len(s)/2)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

def is_valid_input(m, n):
    return m < n

def main():
    try:
        input_func = raw_input #python2
    except NameError:
        input_func = input #python3

    while True:
        try:
                    
            m = int(input_func("Enter the integer m: "))
            n = int(input_func("Enter the integer n where n > m: "))
            
            if is_valid_input(m, n):
                break
            else:
                print("Error: m should be less than n. Please enter valid values.")
        except ValueError:
            print("Please enter valid integers")
        except Exception as e:
            print("Error: {e}")
    
    palind = [a for a in range(m, n + 1) if is_palindrome(str(a))]
    if palind:
        print(f"Palindromic numbers in the inteval [{m}, {n}]: {palind}")
    else:
        print(f"There are no palindromic numbers in the interval [{m}, {n}]")

if __name__=="__main__":
    main()