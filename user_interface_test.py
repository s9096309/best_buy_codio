def main():
    while True:
        print("""
Store Menu:
-----------

1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
""")
        try:
            ask_user = int(input("Please choose a number:"))

            if ask_user == 1:
                print(store.get_all_products())

            elif ask_user == 2:
                print(store.get_total_quantity())

            elif ask_user == 3:
                print(store.order())

            elif ask_user == 4:
                print("Thanks for your visit at Best Buy!")
                break

        except Exception as e:
            print("Error!", e)

if __name__ == "__main__":
    main()