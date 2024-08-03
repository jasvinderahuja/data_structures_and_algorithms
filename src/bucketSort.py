def bucketSort(arr):
    max_item = max(arr)
    len_arr = len(arr)
    size_buckets = max_item/len_arr

    ## create buckets = len_arr
    buckets = [[] for i in range(len_arr)]

    ## Bucket Sort here
    for i in range(len_arr):
        bucket_index = int(arr[i]/size_buckets)
        if bucket_index != len_arr:
            buckets[bucket_index].append(arr[i])
        else:
            buckets[bucket_index-1].append(arr[i])
    ## This is incomplete sort so we get to sort the buckets with our method of choice
    for index in range(len(buckets)):
        sorted(buckets[index])

    ## now flatten
    result = []
    while len(buckets) > 1:
        result.extend(buckets.pop(1))

    return result
