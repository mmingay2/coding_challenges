# Write a function to sort unsigned 16-bit integers 
# that is linear complexity, O(n)
# Since python is not strongly typed, you should ensure 
# that the integer values are all in the range 0-65535

def sort_16bit_integers(num_list):
    mv = 65535
    if max(num_list) > mv:
        raise ValueError("integers must be in range 0-65535")
    else:    
        count = [0] * mv
        for x in num_list:
        # count occurences
            count[x] += 1             
        i = 0
        for x in range(mv):            
            for c in range(count[x]):  
                num_list[i] = x
                i += 1
        return num_list

if __name__ == "__main__":
    test_list_1 = [5676,32,1,19,65000,0]
    true_sorted_1 = [0,1,19,32,5676,65000]
    sorted_list_1 = sort_16bit_integers(test_list_1)
    assert(sorted_list_1 == true_sorted_1)

   
    test_list_2 = [300,200,65536]
    # This should raise a ValueError
    sorted_list_2 = sort_16bit_integers(test_list_2)
