# Pairs of Sum
  
# Find all pairs of number in a list that adds upto k. 	
# Example : 
# Input: [2, 4, 6, 5, -1, 0, 1, 8, 7], k = 6
# Output: [[2,4], [6,0], [5, 1], [-1, 7]]

def sum_of_pairs(numbers, k):
    count = 0
    result = []
    for x in range(0, len(numbers)): 
        for y in range(x + 1, len(numbers)): 
            if numbers[x] + numbers[y] == k: 
                result.append([numbers[x], numbers[y]])
    return(result)


if __name__ == "__main__":
    numbers = [2, 4, 6, 5, -1, 0, 1, 8, 7]
    k=6
    sum_of_pairs(numbers, k)




    