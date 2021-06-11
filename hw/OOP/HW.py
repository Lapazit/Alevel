import copy
# import numpy as np

class Element:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.len_ = 0

    def append(self, value):
        if type(value) == list:
            for i in value:
                self.new = Element(i)
                if self.head is None:
                    self.head = self.new
                else:
                    last = self.head
                    while (last.next):
                        last = last.next
                    last.next = self.new
        else:
            self.new = Element(value)
            if self.head is None:
                self.head = self.new
                return
            last = self.head
            while(last.next):
                last = last.next
            last.next = self.new

    def listprint(self):
        printval = self.head
        if printval is None:
            print('||')
        while printval is not None:
            print(printval.value)
            printval = printval.next

    def __str__(self):
        s = '| '
        printval = self.head
        while printval is not None:
            s += str(printval.value) + ' -> '
            printval = printval.next
        return s+' |'

    def __len__(self):
        lenn = self.head
        count = 0
        while lenn is not None:
            lenn = lenn.next
            count += 1
        return count

    def __getitem__(self, pos):
        elem = self.head
        count = 0
        while count != pos:
            elem = elem.next
            count += 1
        return elem.value

    def __setitem__(self, pos, value):
        elem = self.head
        count = 0
        while elem.next is not None:
            elem = elem.next
            count += 1
            if count == pos:
                elem.value = value
        return

    def __delitem__(self, pos):
        elem = self.head
        count = 1
        if pos == 0:
            self.head = elem.next
        while elem.next is not None:
            elem = elem.next
            if count == pos:
                prev = elem
                elem = elem.next
                prev.next = elem.next
            count += 1

    def __add__(self, other):
        elem=self.head
        while elem.next is not None:
            print(elem.value)
            elem = elem.next
            if elem.next == None:
                elem.next = other.head
                while elem.next is not None:
                    elem = elem.next
                    print(elem.value)

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        elem = self.head
        elem2 = other.head
        if elem.value == elem2.value:
            while elem.next is not None:
                    elem = elem.next
                    elem2 = elem2.next
                    if elem.value == elem2.value:
                        pass
                    else:
                        return False
        return True

    def __bool__(self):
        if self.head is None: return True
        else:
            return False

    def __iter__(self):
        elem = self.head
        if elem == self.head:
            return LinkedListIterator(elem)
        while elem.next is not None:
            elem = elem.next
            return LinkedListIterator(elem)


class LinkedListIterator:

    def __init__(self, head):
        self.current = head

    def __next__(self):
        if self.current == None:
            raise StopIteration
        else:
            item = self.current.value
            self.current = self.current.next
            return item

ll = LinkedList()
ll2 = LinkedList()
ll3 = LinkedList()
ll4 = LinkedList()
ll2.append(1)
ll2.append(2)
ll2.append(3)
ll2.append('new')
# print(len(ll2))
# print(ll2[2])
ll2[2] = 'changed'
# print(ll2)
del ll2[1]              #i don't know why del not working(((
print(ll2)




# ll3.append(5)
# ll3.append(6)
#
# ll4.append(1)
# ll4.append('changed')
# ll4.append('new')

# print('equal' if ll2 == ll4 else 'not equal')
# print('not equal' if ll2 != ll3 else 'equal')
# print(ll2)
# for i in ll2:
#     print(i)


# print(ll2 + ll3)
# print(ll2)
# print('truthy' if ll else 'falsy')
# print(ll)

