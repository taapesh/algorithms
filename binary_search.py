def binary_search(A, x):
    lo = 0
    hi = len(A)-1
    
    while (lo <= hi):
        mid = lo + (hi-lo+1)/2
        
        if (x < A[mid]):
            hi = mid - 1
        elif (x > A[mid]):
            lo = mid + 1
        else:
            return mid
    return -1
            
def test(A, x):
    found = binary_search(A, x)
    
    if (found != -1):
        print(str(x) + " found at index " +  str(found))
    else:
        print(str(x) + " not found")
        
if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(A)
    test(A, 1)
    test(A, 5)
    test(A, 11)