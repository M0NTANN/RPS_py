
import SmallInteger



messX = lambda: input("Enter x: ")
messY = lambda: input("Enter y: ")

def main():
    c = input("Enter command: ")
    if c == "sum":
        print("res: " + str(SmallInteger.sum(messX(), messY())))
        main()
    elif c == "sub":
        print("res: " + str(SmallInteger.sub(messX(), messY())))
        main()
    elif c == "mul":
        print("res: " + str(SmallInteger.mul(messX(), messY())))
        main()
    elif c == "div":
        print("res: " + str(SmallInteger.div(messX(), messY())))
        main()
    elif c == "exit":
        exit()
    else:
        "Command noy found"
        main()



if __name__ == "__main__":
    main()

