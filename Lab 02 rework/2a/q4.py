import random
def isPalindrome(s):
    for i in range(0, int(len(s)/2)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

def maxima(lst):
    m = 0
    for i in lst:
        if i > m:
            m = i
    return m

def main():
    try:
        input_func = raw_input #python2
    except NameError:
        input_func = input #python3

    while True:
        try:
            a = input_func("Original number: ")
            break
        except ValueError:
            print("Please enter a valid number")
        except Exception as e:
            print(f"Error{e}")
    
    if isPalindrome(a):
        print("The given number is palindrome")
    else:
        print("The given number is not palindrome")

    n = random.randint(10, 20)
    lst = []
    for i in range(0, n):
        lst.append(random.randint(0, 100))
    print(lst)
    print(f"The biggest element in the list: {maxima(lst)}")

if __name__=="__main__":
    main()