import abc
from typing import Protocol


class Stack(Protocol):
    def push(self, item):
        ...

    def pop(self):
        ...

    def top(self):
        ...


class PersistentStack:
    def __init__(self, value, parent):
        self._value = value
        self._parent = parent

    def pop(self):
        return self._parent

    def top(self):
        return self._value

    def push(self, item):  # -> PersistentStack doesn't work <?>
        return PersistentStack(item, self)


class EmptyStack:
    def __init__(self):
        # self.__value = None
        # self.__parent = None
        self._depth = 0

    # def __str__(self):
    #     return "EmptyStack()"

    @property
    def depth(self):
        return self._depth

    def pop(self):
        raise ValueError("Cannot pop from an empty stack")

    def top(self):
        raise ValueError("An empty stack has no top")

    def push(self, item) -> PersistentStack:
        return PersistentStack(item, self)


def main() -> None:
    stack: EmptyStack = EmptyStack()
    print(stack)
    stack_1: PersistentStack = stack.push(1)
    # print(stack)
    # stack = stack.push(1)
    # print(stack)
    # stack = stack.pop()
    # print(stack)


if __name__ == '__main__':
    main()






