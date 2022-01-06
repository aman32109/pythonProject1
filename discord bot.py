add: str = "/add"
main_text = input("enter command with / before the command")

if main_text==add:
    print("enter 2 numbers")
    no_1 = int(input())
    no_2 = int(input())
    print(no_1+no_2)
    