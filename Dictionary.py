Age={"Nikhil":19,"Neha":20,"Sahil":19}
def check_key():
    key=input("Enter The Key To Check Its Presence: ")
    if key in Age.keys():
        print("Key is present")
    else:
        print("Not Present")
def Value_Sum():
    print("Sum Of Values Is: ",sum(Age.values()))
def main():
    check_key()
    Value_Sum()
if __name__ == '__main__':
    main()