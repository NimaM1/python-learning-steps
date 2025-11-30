import API
import storage
import colorama

print(colorama.Fore.YELLOW + """
============================================
       >>> Movie & Series Manager <<<
============================================


[1] Search Movie Series
[2] Show List
[3] Delete Item Out of List
[4] Exit      

""")


def main():
    while True:
        try:
            option = int(input(colorama.Fore.WHITE + ">>>> "))
        except (ValueError, IndexError):
            print(colorama.Fore.RED + "Please Enter a Valid number!! ")

        if option == 1:
            API.pro_Search()
        elif option == 2:
            storage.show_list()
        elif option == 3:
            storage.delete()
        elif option == 4:
            exit = input(colorama.Fore.LIGHTBLACK_EX +
                         "Do you want to close the Program? ").strip().lower()
            if "y" in exit:
                print(colorama.Fore.YELLOW + "Have a good day then :) ")
                break
            elif "n" in exit:
                print(colorama.Fore.YELLOW + "Happy you are not ganna do it :)")
                continue


main()
