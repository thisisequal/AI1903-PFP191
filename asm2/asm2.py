def read_books_info(filename):
    with open(filename, 'r') as file:
        num_books = int(file.readline().strip())
        books = []
        for _ in range(num_books):
            book_info = {
                "Ten_sach": file.readline().strip(),
                "Ten_tac_gia": file.readline().strip(),
                "Nha_xuat_ban": file.readline().strip(),
                "Nam_XB": int(file.readline().strip()),
                "Gia_ban": float(file.readline().strip())
            }
            books.append(book_info)
            file.readline()  # Read the blank line
    return books

# Function to write book information to file
def write_books_info(filename, books):
    with open(filename, 'w') as file:
        file.write(str(len(books)) + "\n")
        for book in books:
            file.write(book["Ten_sach"] + "\n")
            file.write(book["Ten_tac_gia"] + "\n")
            file.write(book["Nha_xuat_ban"] + "\n")
            file.write(str(book["Nam_XB"]) + "\n")
            file.write(str(book["Gia_ban"]) + "\n\n")

# Function to add book information
def add_books():
    num_books = int(input("Enter the number of books: "))
    books = []
    for _ in range(num_books):
        print(f"Book {len(books) + 1}:")
        ten_sach = input("Enter book title: ")
        ten_tac_gia = input("Enter author name: ")
        nha_xuat_ban = input("Enter publisher: ")
        nam_xb = int(input("Enter publication year: "))
        gia_ban = float(input("Enter book price: "))
        book_info = {
            "Ten_sach": ten_sach,
            "Ten_tac_gia": ten_tac_gia,
            "Nha_xuat_ban": nha_xuat_ban,
            "Nam_XB": nam_xb,
            "Gia_ban": gia_ban
        }
        books.append(book_info)
    write_books_info("FU.txt", books)
    print("Books information has been saved successfully.")

# Function to display book information
def display_books_info():
    books = read_books_info("FU.txt")
    print("Total number of books:", len(books))
    print("{:<30} {:<30} {:<10} {:<10}".format("Ten sach", "Ten tac gia", "Nam XB", "Gia"))
    for book in books:
        print("{:<30} {:<30} {:<10} {:<10}".format(book["Ten_sach"], book["Ten_tac_gia"], str(book["Nam_XB"]), str(book["Gia_ban"])))

# Function to sort book information by publication year and price in descending order
def sort_books_info():
    books = read_books_info("FU.txt")
    sorted_books = sorted(books, key=lambda x: (x["Nam_XB"], x["Gia_ban"]), reverse=True)
    write_books_info("FU2024.txt", sorted_books)
    print("Books information has been sorted and saved to FU2024.txt.")
    print("Total number of sorted books:", len(sorted_books))
    print("{:<30} {:<30} {:<10} {:<10}".format("Ten sach", "Ten tac gia", "Nam XB", "Gia"))
    for book in sorted_books:
        print("{:<30} {:<30} {:<10} {:<10}".format(book["Ten_sach"], book["Ten_tac_gia"], str(book["Nam_XB"]), str(book["Gia_ban"])))

# Function to search book by title
def search_by_title(title):
    books = read_books_info("FU.txt")
    found = False
    for book in books:
        if book["Ten_sach"] == title:
            print(f"{book['Ten_sach']}, {book['Ten_tac_gia']}, {book['Nha_xuat_ban']}")
            found = True
    if not found:
        print("Khong tim thay cuon sach nao!")

# Function to search book by author
def search_by_author(author):
    books = read_books_info("FU.txt")
    author_count = {}
    for book in books:
        if book["Ten_tac_gia"] == author:
            if author_count.get(book["Ten_tac_gia"]) is None:
                author_count[book["Ten_tac_gia"]] = 1
            else:
                author_count[book["Ten_tac_gia"]] += 1
    if author_count:
        for author, count in author_count.items():
            print(f"{author}, {count}")
    else:
        print("Khong tim thay tac gia tren!")

# Main menu function
def main_menu():
    while True:
        print("=" * 40)
        print("1. Nhap thong tin cua n cuon sach cua FU")
        print("2. In ra man hinh thong tin vua nhap")
        print("3. Sap xep thong tin giam dan theo nam xuat ban va hien thi")
        print("4. Tim kiem theo ten sach")
        print("5. Tim kiem theo ten tac gia")
        print("6. Thoat")
        print("=" * 40)

        choice = input("Chon chuc nang (1-6): ")
        if choice == "1":
            add_books()
        elif choice == "2":
            display_books_info()
        elif choice == "3":
            sort_books_info()
        elif choice == "4":
            title = input("Nhap ten sach can tim: ")
            search_by_title(title)
        elif choice == "5":
            author = input("Nhap ten tac gia can tim: ")
            search_by_author(author)
        elif choice == "6":
            print("Thoat chuong trinh. Cam on ban!")
            break
        else:
            print("Lua chon khong hop le. Vui long chon lai.")

if __name__ == "__main__":
    main_menu()
