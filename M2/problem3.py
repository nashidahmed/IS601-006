a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]


def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nPositive Output:\n")
    # TODO add new code here to print the desired result
    # nn379 Feb 2 2023
    # Loop through the array range using len to catch a hold of the index so we can modify the array values if needed
    for i in range(len(arr)):
        # Check if the element is negative else leave the element as is
        if float(arr[i]) < 0:
            # If the element is of string type, convert it to positive and store as string, else simply convert the number to postive 
            arr[i] = f"{-int(arr[i])}" if isinstance(arr[i], str) else -arr[i]
    print(arr)


print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)