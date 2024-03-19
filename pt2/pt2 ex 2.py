def add_employee():
    with open("input.txt", "a") as file:
        code = input("Enter employee code: ")
        name = input("Enter employee name: ")
        salary = complex(input("Enter employee salary: "))
        allowance = complex(input("Enter employee allowance: "))
        file.write(f"{code},{name},{salary},{allowance}\n")
    print("Employee added successfully.")

def binary_search_by_name(name, lines):
    low = 0
    high = len(lines) - 1

    while low <= high:
        mid = (low + high) // 2
        data = lines[mid].strip().split(",")
        if data[1] == name:
            print("Employee found:")
            print(f"Code: {data[0]}, Name: {data[1]}, Salary: {data[2]}, Allowance: {data[3]}")
            return
        elif data[1] < name:
            low = mid + 1
        else:
            high = mid - 1
    print("Employee not found.")

def remove_employee_by_code(code):
    with open("input.txt", "r") as file:
        lines = file.readlines()

    with open("input.txt", "w") as file:
        removed = False
        for line in lines:
            data = line.strip().split(",")
            if data[0] != code:
                file.write(line)
            else:
                removed = True
        if removed:
            print("Employee removed successfully.")
        else:
            print("Employee not found.")

def print_sorted_list():
    try:
        with open("input.txt", "r") as file:
            lines = file.readlines()

        lines.sort(key=lambda x: float(x.strip().split(",")[2]) + float(x.strip().split(",")[3]), reverse=True)

        with open("result.txt", "w") as file:
            for line in lines:
                file.write(line)
        print("List printed in descending order based on salary + allowance. Saved in result.txt")
    except ValueError:
        print("Error: Invalid data format in input file. Please check the format of salary and allowance.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main_menu():
    while True:
        print("=" * 40)
        print("1. Add a new employee")
        print("2. Find employee by name")
        print("3. Remove employee by code")
        print("4. Print list in descending order based on salary + allowance")
        print("5. Exit")
        print("=" * 40)

        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            name = input("Enter employee name to search: ")
            with open("input.txt", "r") as file:
                lines = file.readlines()
            binary_search_by_name(name, lines)
        elif choice == "3":
            code = input("Enter employee code to remove: ")
            remove_employee_by_code(code)
        elif choice == "4":
            print_sorted_list()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main_menu()
