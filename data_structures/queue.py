
class Queue:

    def __init__(self) -> None:
        self.list = []

    def push(self, var):
        self.list.append(var)

    def get_first(self):
        return self.list.pop(0)

    def pop_last(self):
        return self.list.pop()

    def show(self):
        print(" <- ".join(map(str, self.list)))

    def __len__(self):
        return len(self.list)


if __name__ == "__main__":
    q  = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.show()
    print(q.get_first(), len(q))
    print(q.pop_last(), len(q))



