"""Function to check if a queue is empty or not"""
def is_empty(my_queue):
    
    if len(customer_queue) == 0:
        is_empty = True
    else:
        is_empty = False
    
    return is_empty

"""Create an empty queue."""
customer_queue = []

"""Call the is_empty function to check if the queue is empty."""
print(is_empty(customer_queue)) #Result should be True

"""Add a customer to the queue."""
customer_queue.append("Joe Black")
customer_queue.append("Sally Smith")
customer_queue.append("Bob Baker")

"""Call the is_empty function to check if the queue is empty."""
print(is_empty(customer_queue)) #Result should be False
