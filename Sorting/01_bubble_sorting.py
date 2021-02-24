# The simplest sorting variant.
# Pairwise comparison of elements in an array, where, provided that one element is larger than the other, the elements are swapped.
# The largest, as it were, floats up, like a bubble.

sourceArray = [0, 5, 7, 7, 1, 3, 6]             # Source array
aLength = len(sourceArray)                      # Length of source array
trace = False                                   # If we need step by step tracing of our sorting

print("Source array:", sourceArray)
print("Array length:", len(sourceArray))
print("===========================")

for i in range(aLength - 1):
    for j in range(aLength - 1 - i):
        if trace:
            print("Step ", i, '.', j, ': ', sourceArray, sep='')
        if sourceArray[j] > sourceArray[j+1]:
            sourceArray[j], sourceArray[j+1] = sourceArray[j+1], sourceArray[j]
            # temp = sourceArray[j]
            # sourceArray[j] = sourceArray[j+1]
            # sourceArray[j+1] = temp
            
print("Bubble sorting: ", sourceArray)