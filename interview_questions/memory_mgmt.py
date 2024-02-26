import sys

# Function to demonstrate memory management
def memory_management_example():
    # Create a list containing integers
    my_list = [1, 2, 3, 4, 5]
    
    # Print the memory address of the list
    print("Memory address of the list:", id(my_list))
    
    # Print the size of the list in bytes
    print("Size of the list (in bytes):", sys.getsizeof(my_list))
    
    # Add some more integers to the list
    my_list.extend([6, 7, 8, 9, 10])
    
    # Print the new memory address of the list
    print("Memory address of the modified list:", id(my_list))
    
    # Print the new size of the list in bytes
    print("Size of the modified list (in bytes):", sys.getsizeof(my_list))

# Call the function to demonstrate memory management
memory_management_example()
