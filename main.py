class Main:
    def __init__(self):
        self.c = int(input("Enter size of pattern ( the number must be odd! ): "))
        self.x = 0
        self.y = 0

    def pick_symbol(self):
        if self.x == self.c // 2 and self.y == self.c // 2:
            print("*", end=" ")
        elif self.y == self.c // 2:
            print("=", end=" ")
        elif self.x == self.c // 2:
            print("@", end=" ")
        elif self.x == self.y or self.x + self.y == self.c - 1:
            print("X", end=" ")
        else:
            print(".", end=" ")
        self.x += 1

    def draw(self):
        for i in range(self.c):
            for j in range(self.c):
                self.pick_symbol()
            self.x = 0
            print()
            self.y += 1


if __name__ == "__main__":
    main = Main()
    if main.c and main.c % 2 != 0:
        main.draw()
    else:
        print("the number must be odd!")
