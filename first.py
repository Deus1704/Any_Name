import time

def bin_search(arr,target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def generate_list(arr):
    for i in range(1,1000000):
        arr.append(i)
    return arr

def main():
    print("Comparing two search approaches. Binary and Linear")
    print("The array to search is generated with 1e6 elements") 
    print("The target is 12345")
    print("First approach: Linear Search")
    arr = generate_list([])
    t1= time.time()
    if (linear_search(arr,12345)) == -1:
        print("Element not found")
    else:
        print("Element found")
    t2 = time.time()
    print("Time taken: ", t2-t1)
    print("Second approach: Binary Search")
    t3= time.time()
    if (bin_search(arr,12345)) == -1:
        print("Element not found")
    else:
        print("Element found")
    t4 = time.time()
    print("Time taken: ", t4-t3)


if __name__ == "__main__":
    main()