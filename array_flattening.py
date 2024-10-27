def flatten(nested_list):
    # Temporary list to hold the flattened elements
    flat_list = []
    
    # Iterate over each element in the nested list
    for element in nested_list:
        # Check if the element is a list
        if isinstance(element, list):
            # If it's a list, recursively flatten it
            flat_list.extend(flatten(element))
        else:
            # If it's not a list, append it to the flat_list
            flat_list.append(element)
    
    return flat_list

# Example input
input_list = eval(input("Enter a nested list: "))

# Call the flatten function and print the result
output = flatten(input_list)
print(output)  # Expected Output: [1, 2, 3, 4, 5, 6, 7]
