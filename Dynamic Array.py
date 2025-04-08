class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity > 0:
            self.capacity = capacity
            self.len = 0
            self.array = [0] * self.capacity
        else:
            print("The array cannot be of size less than zero.")

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.len == self.capacity:
            self.resize()
        
        self.array[self.len] = n
        self.len += 1

    def popback(self) -> int:
        if self.len > 0:
            self.len -= 1
        return self.array[self.len]

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        newArray = [0] * self.capacity 
        
        for i in range(self.len):
            newArray[i] = self.array[i]
        self.array = newArray

    def getSize(self) -> int:
        return self.len
    
    def getCapacity(self) -> int:
        return self.capacity
    
    def main(self):
        print("--------Dynamic Array--------")
        
        try:
            initial_capacity = int(input("Enter initial capacity of the array: "))
            arr = initial_capacity
        except ValueError:
            print("Please enter a valid integer for capacity.")
            return

        while True:
            print("\n--- Menu ---")
            print("1. Get element at index")
            print("2. Set element at index")
            print("3. Push back element")
            print("4. Pop back element")
            print("5. Get current size")
            print("6. Get current capacity")
            print("7. Exit")
            
            choice = input("Choose an option: ")

            if choice == '1':
                try:
                    idx = int(input("Enter index: "))
                    if 0 <= idx < self.getSize(self):
                        print(f"Element at index {idx} is {self.get(idx)}")
                    else:
                        print("Index out of bounds.")
                except ValueError:
                    print("Please enter a valid integer.")
            
            elif choice == '2':
                try:
                    idx = int(input("Enter index: "))
                    val = int(input("Enter value to set: "))
                    if 0 <= idx < self.getSize(self):
                        self.set(idx, val)
                        print(f"Element at index {idx} set to {val}")
                    else:
                        print("Index out of bounds.")
                except ValueError:
                    print("Please enter valid integers.")
            
            elif choice == '3':
                try:
                    val = int(input("Enter value to push: "))
                    self.pushback(val)
                    print(f"Pushed {val} into array.")
                except ValueError:
                    print("Please enter a valid integer.")
            
            elif choice == '4':
                if self.getSize() > 0:
                    popped = self.popback()
                    print(f"Popped value: {popped}")
                else:
                    print("Array is empty.")
            
            elif choice == '5':
                print(f"Current size: {self.getSize()}")
            
            elif choice == '6':
                print(f"Current capacity: {self.getCapacity()}")
            
            elif choice == '7':
                print("Exiting program.")
                break
            
            else:
                print("Invalid choice. Please try again.")

    if __name__ == "__main__":
        main('self')

#Main function is not currently working correctly. Bugs are located in the getSize calls within the main method.
