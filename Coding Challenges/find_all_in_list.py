
def findAll(search_list, item):
    result = []
    # Enumerate is a function that lets you loop over a sequence and keep track of the index at the same time
    for index, value in enumerate(search_list):
        if value == item:
            result.append([index])
        elif isinstance(search_list[index], list):
            for i in findAll(search_list[index], item):
                result.append([index] + i)
    return result

testlist1 = [1, 3, 1, 5, 66, 11, 1]; testlist2 = [[1,2,3], [3,2,1], [2,2,2], [1,1,1,1,1,2]]
value1 = 1; value2 = 2

print(findAll(testlist1, value1)) ; print(findAll(testlist2,value2))

            