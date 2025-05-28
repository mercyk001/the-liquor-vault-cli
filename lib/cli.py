from helpers import (
    display_welcome,
    display_collection,
    login,
    browse_collection,
    view_cart,
    place_order,
    checkout,
)

def main():
    display_welcome()

    while True:
        choice = display_collection()
        
        if choice == "1":
            login()
        elif choice == "2":
            browse_collection()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            place_order()
        elif choice == "5":
            checkout()
            break
        else:
            print("Invalid option! Please select 1-5.")

if __name__ == "__main__":
    main()