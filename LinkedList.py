class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)

        if self.head == None:
            self.head = newNode
        else:
            lastNode = self.head
            while lastNode.next:
                lastNode = lastNode.next
            lastNode.next = newNode
        print()

    def insertAtN(self, data, N):
        newNode = Node(data)
        if N == 0:
            newNode.next = self.head
            self.head = newNode
            return
        
        cNode = self.head
        len = 0

        if cNode is None:
            print(f"{N} is out of bounds, please enter a valid position next time.")

        while cNode is not None and len < N-1:
            cNode = cNode.next
            len += 1

        newNode.next = cNode.next
        cNode.next = newNode
        print()

    def delete(self, N):
        cNode = self.head

        if cNode and cNode.data == N:
            self.head = cNode.next
            cNode = None
            return

        pNode = None
        while cNode and cNode.data != N:
            pNode = cNode
            cNode = cNode.next

        if cNode is None:
            print("Node not found at this position, please try again")
            return
        
        pNode.next = cNode.next
        cNode = None
        print()

    def showList(self):
        cnode = self.head
        count = 0
        print("Start of List")
        while cnode:
            print(str(count) + ": " + cnode.data)
            cnode = cnode.next
            count = count + 1
        print("End of List")
        print()

    def main(self):
        value = input("Enter a value to start the list:")
        self.append(value)

        while True:
            try:
                userchoice = int(input("--------Menu--------\n"
                                       "1) Insert node into the List\n"
                                       "2) Append node into the list\n"
                                       "3) Delete a node\n"
                                       "4) View the list\n"
                                       "5) Exit\n"))
            except ValueError:
                print("Invalid input. Please enter a number corresponding to the menu options.")
                continue
            if userchoice == 1:
                value = input("What would you like to input into the list? ")               
                while True:
                    try:
                        position = int(input("Where would you like to input into the list? (integer position) "))
                        break
                    except ValueError:
                        print("Please enter a valid integer for the position.")               
                self.insertAtN(value, position)    

            elif userchoice == 2:
                value = input("What would you like to append to the list? ")
                self.append(value)

            elif userchoice == 3:
                self.showList()  
                while True:
                    try:
                        index = int(input("Which index would you like to delete? (integer) "))
                        break
                    except ValueError:
                        print("Please enter a valid integer for the index.")
                self.delete(index)

            elif userchoice == 4:
                self.showList()

            elif userchoice == 5:
                print("Exiting the program.")
                break

            else:
                print("Please input a valid menu item")

LinkedList().main()
