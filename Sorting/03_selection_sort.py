# The simplest sorting variant.
# Everything is very simple - we go through the array in search of the maximum element. 
# We swap the found maximum with the last element. 
# The unsorted part of the array has decreased by one element (does not include the last 
# element where we rearranged the found maximum). We apply the same actions to this unsorted part - 
# we find the maximum and put it in the last place in the unsorted part of the array. 
# And so we continue until the unsorted part of the array is reduced to one element.

sourceArray = [0, 5, 7, 7, 1, 3, 6]             # Source array
aLength = len(sourceArray)                      # Length of source array
trace = False                                   # If we need step by step tracing of our sorting

print("Source array:", sourceArray)
print("Array length:", len(sourceArray))
print("===========================")

for i in range(0, aLength):
    min = i
    for j in range(i + 1, aLength):
        if trace:
            print("Step ", i, '.', j, ': ', sourceArray, sep='')

        if sourceArray[j] > sourceArray[min]:
            min = j

        if min != j:
            sourceArray[min], sourceArray[j] = sourceArray[j], sourceArray[min]
            
print("Selection sort result array: ", sourceArray)