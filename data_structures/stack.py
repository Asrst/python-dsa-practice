
class Stack:

    def __init__(self) -> None:
        self.list = []

    def push(self, var):
        self.list.append(var)
        return self

    def pop(self):
        return self.list.pop()

    def show(self):
        print(" -> ".join(map(str, self.list)))

    def __len__(self):
        return len(self.list)



if __name__ == "__main__":
    s  = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.show()
    print(s.pop(), len(s))
