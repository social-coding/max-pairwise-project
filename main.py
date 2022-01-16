import random


def num_array(size,start,end):
    numArray=[]
    for i in range(size):
        num=random.randint(start,end)
        numArray.append(num)
    print(numArray)
    return numArray

def max_pair_product(numArrayArg):
    count=0
    largest_num=0
    second_largest=0
    while count < len(numArrayArg)-1:
        print('Counter - ' + str(count))
        if numArrayArg[count] >= largest_num:
            second_largest = largest_num
            largest_num = numArrayArg[count]
            #print("Largest - " + str(largest_num))
            #print("Second - " + str(second_largest))
        count=count + 1
    result = largest_num*second_largest
    return result

print(max_pair_product(num_array(8,1,9)))

