"""Function to check if a queue is empty or not"""
def is_empty(my_queue):
    
    if len(my_queue) == 0:
        is_empty = True
    else:
        is_empty = False
    
    return is_empty

"""Create an empty queue."""
customers = []

"""Call the is_empty function to check if the queue is empty."""
print(is_empty(customers)) #Result should be True

"""Add a customer to the queue."""
customers.append("Joe Black")
customers.append("Sally Smith")
customers.append("Bob Baker")

"""Call the is_empty function to check if the queue is empty."""
print(is_empty(customers)) #Result should be False
