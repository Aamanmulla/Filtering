def even_odd(lst):
    even_list=[]
    odd_list=[]
    for i in lst:
        if (i % 2 == 0):
            even_list.append(i)
        else:
            odd_list.append(i)
    print("Even numbers from the said list:\n","\n",even_list,"\n")
    print("Odd numbers from the said list:\n","\n",odd_list,"\n")


lst=[]
n=int(input("Enter the numbers in a list: "))
for i in range(0, n):
    ele = int(input())
  
    lst.append(ele)
print("\nOriginal List of Integers:\n","\n",lst,"\n")
even_odd(lst)

