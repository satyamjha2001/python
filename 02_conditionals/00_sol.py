def main():
    age = int(input("Enter age : "))
    if age > 0:
        if age < 13:
            print("Child")
        elif age < 20:
            print("Teenager")
        elif age < 60:
            print("Adult")
        else:
            print("Senior")
    else:
        print("Please enter valid age.")
if __name__ == "__main__":
    main()