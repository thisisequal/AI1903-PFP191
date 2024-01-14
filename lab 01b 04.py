def main():
    try:
        input_func = raw_input
    except NameError:
        input_func = input
    
    while True:
        try:
            a = float(input_func("Input real number a: "))
            b = float(input_func("Input real number b: "))
            c = float(input_func("Input real number c: "))
            print(f"Maximum values between a, b, c: {max([a, b, c])}")
            print(f"Minimum values between a, b, c: {min([a, b, c])}")

            print(f"Arrange a, b, c in ascending order: {sorted([a, b, c])}")
            break
        except ValueError:
            print("Please input valid real numbers")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()