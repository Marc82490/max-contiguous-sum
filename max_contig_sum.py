def max_contig_sum(L):
    """
    L: a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L
    """
    working_list = []
    max_sum = 0
    n = len(L)
    
    for k in range(n):
        for index in range(k+1):
            integers_to_check = L[index : n-k+index]
            working_sum = 0
            for i in range(len(integers_to_check)):
                working_sum += integers_to_check[i]
            if working_sum > max_sum:
                    max_sum = working_sum
    
    return max_sum
