# Sorting Algorithms
Contact:  "jasvinderahuja@gmail.com"

## Types of sorting algorithms
_Note: We are assuming an ascending sort_

1. Monkey Sort also called Bogo Sort

>#Pseudocode  
>While not sorted(array):  
>&emsp;    shuffle(array)   
>return array  

Time Complexity = $ \theta((n-1)*n!) $
_Just don't try it!_

2. Selection Sort

>#Pseudocode   
>for an array of length = n
>select the minimum element put it in position-1  
>select the 2<sup>nd</sup> min element for position-2  
>select the 3<sup>rd</sup> min element for position-3  
>.   
>.    
>select the n<sup>th</sup> min (or max) element for position-n    
>return array  
  
Time Complexity = Asymptotic complexity = O(n<sup>2</sup>)  
Stable: NO   
  
3. Bubble Sort  

>#pseudocode  
>n=length(array)  
>repeat n times  
>&emsp; go from index = 0 to index = n  
>&emsp; &emsp; if array[index-1] > array[index] - swap them  
>return array  
  
Asymptotic Complexity = O(n<sup>2</sup>)  

4. Insert Sort  
  
>#pseudocode  
>n=length(array)   
>for each element in array:    
>&emsp; move left to position where element to its left is smaller than itself   
>return array  
  
_Versions: Recursive (top-down), Shift (not swap), iterative (bottom-up)_  
Time Complexity  
- Worst case = O(n<sup>2</sup>) = average case  
- Best case = O(n)  
Stable: Yes  

5. Merge Sort  

_John von Neumann (1945)_  
  
__Split__ the array in half recursively, till it is split in one element each. __Apply__ sorting and __combine__ left and right halves progressively.  

>#pseudocode   
>__function Split(A):__    
>#recursively split  
>#A=array to sort   
>&emsp; len_a = length(A)    
>&emsp; if len_a <= 1   
>&emsp;&emsp; return A   
>&emsp; Left = MergeSort[left_half(A)]    
>&emsp; Right = MergeSort[right_half(A)]    
>&emsp; return MERGE(Left, Right)   
  
  
>__function Merge(L,R):__   
>#sort and combine  
>While i<=length(L) and j<= length(R)      
>   
>&emsp; if L[i] == R[j]:    
>&emsp;&emsp; new_arr = new_arr.append(L[i])   
>&emsp;&emsp; new_arr = new_arr.append(R(j])   
>&emsp;&emsp; i++; j++   
>   
>&emsp; if L[i] < R[j]:    
>&emsp;&emsp; new_arr = new_arr.append(L[i])    
>&emsp;&emsp; i++   
>   
>&emsp; if L[i] == R[j]:  
>&emsp;&emsp; new_arr = new_arr.append(R[j])  
>&emsp;&emsp; j++  
>  
>&emsp; if i < length(L)  
>&emsp; &emsp; new_arr.append(L elements i and beyond)  
>&emsp; if j < length(R)  
>&emsp; &emsp; new_arr.append(R elements j and beyond)    
>return merged  
>  

Time complexity = O(n log n)  
Memory: MergeSort is not in place and requires extra memory.  
Stable: Yes

_Variant:_ TimSort (named after Tim Peters) combines MergeSort & InsertionSort to give best case O(n) time. 

6. QuickSort  
_Tony Hoare, 1959_  

Identify a pivot (best practice = random element), use it to __split__ the array into - (smaller_than_pivot, equal_to_pivot<sup>*</sup>,larger_than_pivot) - recursively till it reaches leaf elements. Then __combine__ progressively.  


>function QuickSort()  
>if length(unique(Arr))>=1  
>&emsp; return  
>identify random element = X  
>Partition into - Less_than_X, Equal_to_X<sup>*</sup>   Greater_than_X  
>QuickSort(Less_than_X)  
>QuickSort(Greater_than_X)  

<sup>*</sup>_best practice to handle duplicates_  
In-place partitioning methods need no auxillary space and come in two flavours - 
- Lomuto's Partitioning
- Hoare's Partitioning 

Time Complexity: 
- Best-case = O(n log n) = Average Case
- Worst-case = O(n<sup>2</sup>)

Stability: QuickSort is not stable!

7. Tree Sort  
_Calls for Abstract Data Type (ADT) (~binary search tree BST)_-
![Video BST](https://www.youtube.com/watch?v=mtvbVLK5xDQ)  

- Min priority queue
- Max priority queue

>array size = n
>put elements in a max priority queue (max heap)  
>remove n elements from the min priority queue and put from right to left  

Time complexity: n * builing-BST = O(n log n)
Stability: NO

8. Heap Sort

I like heaps but there are some differences from BST
![BST vs Heap](https://www.youtube.com/watch?v=vEMn_qaPXsQ)  

Anyways, heaps are what we will be using. Examples-

- Min Heap  
- Max Heap  


>array size = n, heap height= log n  
>put elements in a max priority queue (max heap)  
>remove n elements from the min priority queue and put from right to left  

Some facts about heaps-
- height of binary tree with n elements = O(log n)  
- Complexity for insertion = O(log n)  
- Complexity to remove max element = O(log n)
- First element that has a child = n/2

Time complexity: n * builing-heap = O(n log n)
Stability: NO

__Other applications for heaps–__
- Emergency priority queue
- Printer printing jobs
- OS process tracking

9. Radix Sort

>#pseudocode
>CountSort on least significant digit
>CountSort on 2<sup>nd</sup> significant digit
>CountSort on 3<sup>rd</sup> significant digit
>.
>.
>CountSort on n<sup>th</sup> significant digit

Time complexity: O(nd), where d is number of digits ~ O(n log n)  
_Variant_: It maybe useful to change from base 10 to base R


10. Counting Sort
>#pseudocode
>create bucket/bin for each element
>count number of each element
>sort bins
>visit the buckets in order and populate the sorted array

11. Bucket Sort
>#pseudocode
>setup empty buckets/bin
>put object in bucket
>sort each non-empty bucket
>visit buckets in order and put all elements into the original array



## Algorithms categories (examples from sorting)
- Brute Force (MonkeySort, SelectionSort, BubbleSort)
- Stepwise decrease (InsertionSort)
- Stepwise divide (MergeSort, QuickSort)
- Transform (TreeSort, HeapSort)
- Linear-time Sorting (RadixSort, CountingSort & BucketSort)

## Applications for Sorting Algorithms
- Faster value search
- Easy identification of duplicates
- Matching items across arrays
- Identify median or K-th value

## Time complexity significance
- At 10<sup>8</sup> operations per second it would take 800 years to sort an array of size 20 by MonkeySort.   
- Difference between n log n and n<sup>2</sup> –
At 10<sup>8</sup> operations per second 320 million elements (US population) would take ~90 seconds to sort at - n log n - and at - n<sup>2</sup> it would take 32.5 years!!


## Some Facts
- Python uses TimSort a version of MergeSort (stable)
- sort (C++) = QuickSort
- stable_sort (C++) = MergeSort.

## Further reading
- Rounding-off errors in matrix processes. A. M. Turing 1947
- [Python function annotations](https://www.youtube.com/watch?v=6eyOQyG6FpE)
- [Linked Lists](https://www.youtube.com/watch?v=qp8u-frRAnU)
- [DS/A Cheatsheet](https://github.com/tsiege/Tech-Interview-Cheat-Sheet)
- [Some useful books](https://github.com/Kikou1998/textbook/blob/master/)




