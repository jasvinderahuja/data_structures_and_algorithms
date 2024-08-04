## get the Kth largest element in sorted order
## sort and find the Kth element, 
## result = Arr[n-k]
## Selection Problem
## there has to be a Kth value!!!
## BruteForce Sort + K th = O(n log n)
## Now O(logn) may not be possible as it will involve not looking at some elements!

## One way - Sort only till Kth element is identified!

### SelectionSort/BubbleSort to Kth: T(n) = O(nk) --> worst case = O(n^2)
### Insertion sort needs to be performed to the end to get the Kth element
### MergeSort also needs to be performed to the end to get the Kth element

### Use Heaps - Max heaps - extract max, K times!
### To build a heap of n elements = T(n) = O(n)
### Extract K th element T(n) = K log n
### So total T(n) = O(n + k log n)
### So max heap is a good attempt but it isnt better than BruteForce! O(n log n)

### Maybe use the Kth variable in new_array of length = k
### Not new_array (O(n log n)) but a min_heap (O(log k))
### so with min heap also it is o(n log n)

### try QuickSort
### pivot is the hard wall kth element is either on left or right
### this is decrease and conquer! work on the bucket which has our index  
### This will improve from n log n to linear O(n)
