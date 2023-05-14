import SmallInteger
#import switch
#x = input()
#print(SmallInteger.SmallInteger.check(int(x)))

class Switch:
    def __init__(self, value):
        self.value = value

    def case(self, value, code):
        if self.value == value:
            code()
        return self





def main():
    c = input("Enter command: ")
    if c == "sum":
        x = input("Enter x: ")
        y = input("Enter y: ")
        print("res: " + str(SmallInteger.sum(x, y)))
        main()
    elif c == "sub":
        x = input("Enter x: ")
        y = input("Enter y: ")
        print("res: " + str(SmallInteger.sub(x, y)))
        main()
    elif c == "mul":
        x = input("Enter x: ")
        y = input("Enter y: ")
        print("res: " + str(SmallInteger.mul(x, y)))
        main()
    elif c == "div":
        x = input("Enter x: ")
        y = input("Enter y: ")
        print("res: " + str(SmallInteger.div(x, y)))
        main()
    elif c == "exit":
        exit()
    else:
        "Command noy found"



if __name__ == "__main__":
    main()

