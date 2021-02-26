class Element:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, values=[]):
        if len(values) > 0:
            values.reverse()
            self.values = values
            self.length = len(values)
            head = Element(values[0])
            self.head = head
            total_length = len(values)+1
            nodes = range(1, total_length)
            for i in nodes:
                curr_element = self.head
                new_element = Element(i)
                new_element.next = curr_element
                self.head = new_element
        else:
            self.head = None
            self.length = 0

    def add(self, new_element):
        if self.head is None:
            self.values = [new_element.value]
            self.head = new_element
            self.length = 1
        else:
            self.values.insert(new_element.value, 0)
            curr_element = self.head
            new_element.next = curr_element
            self.head = new_element
            self.length += 1

    def to_list(self):
        return self.values
    
    def reverse(self):
        self.values.reverse()
        return self
