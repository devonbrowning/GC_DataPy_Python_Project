import user_actions


def main():
    print("Welcome to the Library Terminal!")

    while True:
        # Displaying the menu options
        print('\nMain Menu')
        print('1. Display all books')
        print('2. Search for a book by author')
        print('3. Search for a book by title')
        print('4. Checkout a book')
        print('5. Return a book')
        print('6. Add a new book')
        print('7. Exit')
        choice = input('Please choose which action you would like to take (1-7): ')

        # Handling different choices made by the user
        if choice == '1':
            # Display all books
            user_actions.book_display()
        elif choice == '2':
            # Search for a book by author
            user_actions.search_author()
        elif choice == '3':
            # Search for a book by title
            user_actions.search_title()
        elif choice == '4':
            # Checkout a book
            user_actions.select_book()
        elif choice == "5":
            # Return a book
            user_actions.return_book()
        elif choice == "6":
            user_actions.add_book()
        elif choice == "7":
            print("Thank you for using the library system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        # Prompting user if they want to return to the main menu or exit
        return_to_menu = input("Do you want to return to the main menu? (y/n): ").lower()
        if return_to_menu != 'y':
            print("Thank you for using the library system. Goodbye!")
            break


if __name__ == "__main__":
    main()
