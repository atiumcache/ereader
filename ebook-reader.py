"""A simple representation of an eBook reader that works with Project Gutenberg."""
from time import sleep # used throughout to create natural transitions for the user
import webbrowser

def main(): 
    kindleLoad()

    startupMessage = "\nHello! Welcome to your Kindle e-Reader."
    print(startupMessage)
    option = ""
    userKindle = Kindle()

    username = input("What is your name? ").strip()

    while option != "4":
        print("\n***** ", username.upper(), "'S KINDLE *****", sep="")
        print("MAIN MENU:\n1) View books. \n2) Buy books. \n3) Read a book. \n4) Quit.")
        option = input("Input a number and press enter: ").strip()
        if option not in "1234":
            print("Invalid input. Try again.\n")
            continue

        match option:
            case "1":
                userKindle.view_purchased()
            case "2":
                userKindle.buy_books()
            case "3":
                userKindle.read_book()
            case "4":
                break


class Kindle:
    def __init__(self):
        self.ownedBooks = []

    def view_purchased(self):
        print("\nMY BOOKS:")
        counter = 1
        for book in self.ownedBooks:
            sleep(0.7)
            print(counter, ") ", book.title, " by ", book.author, sep="")
            sleep(1.0)

    def buy_books(self):
        counter = 1
        print("\nAvailable books: ")
        for book in CATALOG:
            sleep(0.7)
            print(counter, ") ", book.title, " by ", book.author, sep="")
            counter += 1
        sleep(0.5)
        
        choice = int(input("\nWhich book would you like to purchase?\nInput a number: ").strip())

        if choice not in range(counter + 1):
            print("\nInvalid option. Purchase failed.")
        elif CATALOG[choice - 1] in self.ownedBooks:
            print("\nYou already own that book! Don't waste your money.")
        else: 
            self.ownedBooks.append(CATALOG[choice - 1])
            print("\nSuccess! You purchased ", CATALOG[choice - 1].title, "! Your account has been charged.\nTime to get readin'...", sep="")
        
        sleep(1)

    def read_book(self):
        self.view_purchased()
        choice = int(input("Which book would you like to read?\nInput a number: ").strip())
        if choice not in range(len(self.ownedBooks) + 1):
            print("\nInvalid option. Try again.")
            self.read_book()
        else:
            print("Opening book in web browser...")
            sleep(1)
            webbrowser.open(self.ownedBooks[choice - 1].url, new=2)


class Book:
    def __init__(self, title, author, url):
        self.title = title
        self.author = author
        self.url = url


"""Initialize a few books into the catalog."""
alice_in_wonderland = Book("Alice's Adventures in Wonderland", "Lewis Carroll", "https://www.gutenberg.org/cache/epub/11/pg11-images.html")
romeo_and_juliet = Book("Romeo and Juliet", "William Shakespeare", "https://www.gutenberg.org/cache/epub/1513/pg1513-images.html")
dracula = Book("Dracula", "Bram Stoker", "https://www.gutenberg.org/cache/epub/345/pg345-images.html")
CATALOG = [alice_in_wonderland, romeo_and_juliet, dracula]


def kindleLoad():
    print("KINDLE LOADING")
    print(" .............\n")
    sleep(1)
    print("  ALMOST THERE...")
    print("   ..............\n")
    sleep(1)
    print("    Kindle initialized...\n     Entering a world of books...")
    sleep(1.5)

main()