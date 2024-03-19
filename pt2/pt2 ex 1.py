def replace_chars(input_str,char_to_replace,new_char):
    return input_str.replace(char_to_replace,new_char)
def main():
    input_str = input("Enter a string with no spaces: ")
    char_to_replace = input("Enter a character(s) you want to replace in the string: ")
    new_char = input("Enter a new character you want to add in the string: ")

    result = replace_chars(input_str,char_to_replace,new_char)

    print("Fixed string: ",result)

if __name__ == "__main__":
    main()