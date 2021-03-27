class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def add_element(self, new_element):
        current_element = self.head
        if self.head:
            while current_element.next:
                current_element = current_element.next
            current_element.next = new_element
        else:
            self.head = new_element


    def show_elements(self):
        current_element = self.head
        res = []
        if self.head:
            while current_element:
                print(current_element.value)
                res.append(current_element.value)
                current_element = current_element.next
            return res
            # print(current_element.value)
        else:
            print('no element at head')
        


    def get_position_of_that_value(self, value_lookingfor):
        counter = 1
        current_val = self.head
        if self.head:
            while current_val:
                if current_val.value == value_lookingfor:
                    return counter
                else:
                    counter +=1 
                    current_val = current_val.next
            # return counter
        else:
            print('no data available')
        
    
    def get_value_at_position(self, position):
        counter = 1
        current_val = self.head
        if position == 0:
            return None
        else:
            while current_val and counter <= position:
                if position == counter:
                    return current_val.value
                else:
                    counter += 1
                    current_val = current_val.next
            return None

    def insert_value(self,new_value, position):
        counter = 1
        current_val = self.head
        if position == 1:
            new_value.next = current_val
            self.head = new_value
        elif position > 1:
            while current_val and counter < position:
                if counter == position - 1:
                    new_value.next = current_val.next
                    current_val.next = new_value
                current_val = current_val.next
                counter += 1
        else:
            return None

    def delete_node(self, value):
        ## node ---> node ---> node --> node
        current_val = self.head
        previous = None

        while current_val:
            if current_val.value == value:
                if previous == None:
                    self.head = current_val.next
                    break
                else:
                    previous.next = current_val.next
                    current_val.next = None
                    
            else:
                previous = current_val
                current_val = current_val.next    

        return self.head


    def delete(self, value):
    # """Delete the first node with a given value."""
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next
        pass

    def middle_element(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            fast = fast.next
        return slow.value

# ll = LinkedList()
# n1 = Node(11)
# n2 = Node(22)
# n3 = Node(33)
# n4 = Node(44)
# n5 = Node(44)

# ll.add_element(n1)
# ll.add_element(n2)
# ll.add_element(n3)
# ll.add_element(n4)
# ll.add_element(n5)


# ll.show_elements()
# print(ll.middle_element())

#here if you see the output, this method does not change the main value
a = '10'
print(a.lstrip('0')) #10200
print(a)  #010200

print(type(str(int(a))))


from itertools import combinations
c = combinations(a,3)
for val in c:
    print(val)

#count the length without storing the iterable.
l = sum(1 for i in c)
print(l)

print(str(0))