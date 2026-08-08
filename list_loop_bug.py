num=[1,2,3,4,5]
for i in num:
    if i <3 :
        num.remove(i)
print(num)

##in this case index value are taken after removeing the 1 list updated that 2 in 0th indext here 1 on index in 3,
because i in 1 so i<3 is false.know answer is [2,3,4,5].

names=['ram','krisha','arjun']
names.insert(1,names.pop())
print(names)

in this case single line run two ways  pop() removes the laste emlemt and retrive it than inset place the value in 
1 index of names list so out put is ['ram','arjun','krishna']

words=['apple','ant','bat','ball']
count=0
for i in  words:
    for j in i:
        if i.count('a')==1:
            count+=i.count('a')
print(count)

in ever word check for 'a' in a count is equal to 1 ,count the lenth of word

                                     
                                     
