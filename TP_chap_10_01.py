def nested_sum(t):
    """
    takes in a nested list and gives out the sum
    """
    total = 0
    for i in t:
            total+=sum(i)
    return total
t=[[1,2],[3],[4,5,6]]
print(nested_sum(t))
