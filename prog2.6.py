my_list=input("enter a list of numbers separated by space:")
my_list=list(map(int,my_list.split()))
sum=0
for num in my_list:
    sum+=num
    print("the sum of the number is ",sum)
