def pair_sum_sorted_array(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    if not numbers:
        return[-1,-1]
        
    left_pointer = 0
    right_pointer = len(numbers) - 1
    
    while left_pointer < right_pointer:
        _current_sum = numbers[left_pointer] + numbers[right_pointer]
        if _current_sum == target:
            return [left_pointer,right_pointer]
        elif _current_sum > target:
            right_pointer -= 1
        elif _current_sum < target:
            left_pointer += 1
            
    return [-1,-1]