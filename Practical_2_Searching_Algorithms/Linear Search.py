def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [10, 25, 30, 45, 50, 65]
target = 45

result = linear_search(arr, target)

print("Array:", arr)
print("Searching Element:", target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")