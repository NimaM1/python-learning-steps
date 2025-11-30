print("""Hello and welcome to your TODO app!!!!
to select any option enter its number.
[1] Add a task
[2] View all tasks
[3] Mark task as done
[4] Delete a task
[5] Exit
""")


def main():

    while True:
        option = input(">>>> ")
        if "1" in option:
            add = input("tell me what you wanna add: ")
            with open("todo.csv", "a") as file:
                file.write(f"{add},X\n")
            print(f"you have added {add} to your list")
            again = input(
                "do you wanna make some other changes? ").strip().lower()
            if "y" in again:
                continue
            elif "n" in again:
                print("have a nice day then. ")
                break
        elif "2" in option:
            with open("todo.csv", "r") as file:
                print("here are all your todos")
                print(file.read())
                again = input(
                    "do you wanna make some other changes? ").strip().lower()
            if "y" in again:
                continue
            elif "n" in again:
                print("have a nice day then. ")
                break

        elif "3" in option:
            mark_done1 = input(
                "which task you wanna mark as done? ").strip()
            updated_lines = []
            with open("todo.csv", "r") as file:
                for line in file:
                    task, status = line.strip().split(",")
                    if task.strip() == mark_done1:
                        updated_lines.append(f"{task},done\n")
                    else:
                        updated_lines.append(line)
            with open("todo.csv", "w") as file:
                file.writelines(updated_lines)

            print(f"you have marked '{mark_done1}' as done.")

            again = input(
                "do you wanna make some other changes? ").strip().lower()
            if "y" in again:
                continue
            elif "n" in again:
                print("have a nice day then. ")
                break
        elif "4" in option:
            delete = input("which task you wana delete? ")
            update_list = []
            with open("todo.csv", "r")as file:
                for line in file:
                    task, status = line.strip().split(",")
                    if delete != task:
                        update_list.append(line)
            with open("todo.csv", "w")as file:
                file.writelines(update_list)
            print(f"you have deleted {delete} out of your todos. ")
            again = input(
                "do you wanna make some other changes? ").strip().lower()
            if "y" in again:
                continue
            elif "n" in again:
                print("have a nice day then. ")
                break

        elif "5" in option:
            print("Have a nice day then. ")
            break


main()
