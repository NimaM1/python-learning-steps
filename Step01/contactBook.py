def main():
    while True:
        contacts = {"nima": "0912"}
        option = input("""Welcome to your contact book!
    Choose an option:
    1. Add a contact
    2. View all contacts
    3. Search by name
    4. Delete a contact
    5. Exit
    >>>>> """)

        if "2" in option:
            for name in contacts:
                print(name, contacts[name], sep=": ")
            answer = input("wana do something else? ").lower().strip()
            if "y" in answer:
                main()
            elif "n" in answer:
                print("allright have a nice day then!!!")
                break
        if "3" in option:
            option_3 = input(
                "which name you are looking to get: ").lower().strip()
            print(
                f"here is the number of {option_3}, {contacts[option_3]}")
            answer = input("wana do something else? ").lower().strip()
            if "y" in answer:
                main()
            elif "n" in answer:
                print("allright have a nice day then!!!")
                break
        if "4" in option:
            option_4 = input("which name would you like to delete? ")
            print(f"you deleted {option_4} out of your contacs")
            contacts.pop(option_4)
            answer = input("wana do something else? ").lower().strip()
            if "y" in answer:
                main()
            elif "n" in answer:
                print("allright have a nice day then!!!")
                break
        if "5" in option:
            print("allright have a nice day then!!!")
            break


main()
