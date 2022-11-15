def twosum(numsList, targetInt):
    # Create a hashmap to track all numbers in the initial list
    hashmap = {}
    # Iterate through initial list and add each number in initial list as a key and value is its index
    for i in range(len(numsList)):
        hashmap[numsList[i]] = i
    # Iterate through initial list and find complement
    for i in range(len(numsList)):
        complement = targetInt - numsList[i]
        # Check if complement(key) is in hashmap and also not the same index
        if complement in hashmap and complement != i:
            # Return the indexes
            return [i, hashmap[complement]]


twosum([1, 2, 3, 4, 5], 9)
