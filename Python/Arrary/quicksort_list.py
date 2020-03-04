# Method 1 - general way
def quicksort(A, low, high):
    if left >= right:
        return
    left, right = low, high   # move left/ right pointer
    pivot = A[low]
    while left < right:
        print(2)
        while left < right and A[right] > pivot:
            right -= 1
        A[left] = A[right]
        while left < right and A[left] <= pivot:
            left += 1
        A[right] = A[left]
    A[right] = pivot
    quicksort(A, low, left - 1)
    quicksort(A, left + 1, high)

# Method 2 - From Introduction to Algorithms
# https://blog.csdn.net/razor87/article/details/71155518
def quick_sort(A, l, r):
    if l < r:
        q = partition(A, l, r)
        quick_sort(A, l, q - 1)
        quick_sort(A, q + 1, r)
def partition(A, l, r):
    pivot = A[r]
    i = l - 1
    for j in range(l, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

if __name__ == "__main__":
    A = [1,6,3,2,9,10,4,1]
    quick_sort(A, 0, len(A) - 1)
    print(A)
