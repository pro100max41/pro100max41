
def ser(num_list):
    l=len(num_list)
    sum=0
    for x in num_list:
        sum+=x
    ser=sum/l    
    return ser


num_list=[1,2,3,4,5]


print(ser(num_list))
'''
def max1(num1,num2):
    """This func returns max number between 2 numbers"""
    max_num=max(num1,num2)
    return max_num

print(max1(5,10))
print(max1.__doc__)
'''
