# This code takes a deeply nested list as input and returns a flat list as output.

def flatten(nested_list):
    flat_list = []  # Creating a temporary list to store the flattened elements
    
    for element in nested_list:
        # Checking if the element is a list
        if isinstance(element, list):
            flat_list.extend(flatten(element))  # If it's a list, recursively flatten it
        else:
            flat_list.append(element)  # If it's not a list, append it to the temporary list
    
    return flat_list

input_list = eval(input("Enter a nested list: "))  # Taking input from the user
output = flatten(input_list)  # Calling the flatten function and printing the result
print(output)
