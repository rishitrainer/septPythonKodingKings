import queue

fifo = queue.Queue()
lifo = queue.LifoQueue()
simple = queue.SimpleQueue()
priority = queue.PriorityQueue()

# Put
message = "This is Just a Test Message "
fifo.put(message)
lifo.put(message)
simple.put(message)
priority.put(message)

print(fifo.qsize())
print(lifo.qsize())
print(simple.qsize())
print(priority.qsize())



for i in range(10):
    test_msg = message + str(i)
    fifo.put(test_msg)
    lifo.put(test_msg)
    simple.put(test_msg)
    priority.put(test_msg)


print(fifo.get())
print(lifo.get())
print(simple.get())
print(priority.get())

# Checking if queue is full
fifo_size5 = queue.Queue(5)
fifo_size5.put("message1")
fifo_size5.put("message2")
fifo_size5.put("message3")
fifo_size5.put("message4")
fifo_size5.put("message5")
if fifo_size5.full():
    print("queue is full")
else:
    print("you can add more messages")
