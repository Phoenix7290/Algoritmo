def greatestNumber(array):
    if not array:
        return None
    
    max_value = array[0]
    
    for num in array[1:]:
        if num > max_value:
            max_value = num
            
    return max_value