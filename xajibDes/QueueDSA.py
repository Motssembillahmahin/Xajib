class Queue:

    def __init__(self):

        self.items = []

    def enqueue(self, item):

        self.items.append(item)

    def dequeue(self):

        if not self.isEmpty():

            return self.items.pop(0)

        else:

            print("Queue is empty. Cannot dequeue.")

    def isEmpty(self):

        return len(self.items) == 0

    def size(self):

        return len(self.items)


my_queue = Queue()

while True:

    user_input = input("Enter an item to enqueue (press 'q' to stop): ")

    if user_input.lower() == 'q':
        break

    try:

        item = int(user_input)

        my_queue.enqueue(item)

    except ValueError:

        print("Invalid input. Please enter an integer.")

print("Size of the queue:", my_queue.size())

while not my_queue.isEmpty():
    print("Dequeued item:", my_queue.dequeue())

print("Size of the queue after dequeue:", my_queue.size())