list1 = []
list2 = []
n = int(input())
for x in range(n*2):
    num = int(input())
    if x >= n :
        list2.append(num)
    else:
        list1.append(num)
      
def summation(list1,list2):
    updated_list = []
    for x in range(len(list1)):
        for y in range(len(list2)):
            if x == y :
                newlist = list1[x]+list2[y]
                updated_list.append(newlist)
    return updated_list
  
def find_min_max(yay):
    small = min(yay)
    big = max(yay)
    return small,big
  
print(summation(list1,list2))
print(find_min_max(summation(list1,list2)))
