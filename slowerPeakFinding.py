# The implementation is the same as the pseudocode from the notes

def slowPeakFinding(arr):
    # Returns the index of a peak in the array
    n = len(arr)
    if arr[0] >= arr[1]:
        return 0
    if arr[n-1] >= arr[n-2]:
        return n-1
    for i in range(1, n-1):
        if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
            return i
        
    return -1

# Create some test cases
def test():
    arr1 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr3 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    arr4 = [1, 2, 3, 4, 5, 6, 5, 4, 3]
    
    try:
        assert peakFinding(arr1) == 5,
        assert peakFinding(arr2) == 9, 
        assert peakFinding(arr3) == 9, 
        assert peakFinding(arr4) == 6, 
        print("All tests passed!")
    except AssertionError as e:
        print(e)

    
test()
