print("--------------Program 1-------------------")
print(" ------Get ODD NUMBERS -----")
print(" ------- 1.a. List Comprehension ------ ")

odd_numbers = [i for i in range(0, 100+1) if i % 2]
print(f"The list of odd numbers using list comprehension are: {odd_numbers}")

print(" ------- 1.b. Normal For Loop -------")

def odd_gen(start, end):
    for i in range(start, end+1):
        if i % 2!=0:
            print(i)
        else:
            pass
print("The list of odd numbers using Normal Loop are:")
odd_gen(0, 100)

print(" ------- 1.c. Generator mechanism ----")

def odd_gen(start, end):
    for i in range(start, end+1):
        if i % 2:
            yield i
        else:
            pass

print(f"The list of odd numbers using generator mechanism are: {list(odd_gen(0, 100))}")



print("  ----------------------------------------------------------------------------------------- ")

print("2. Implement palindrome using iterator(for loop) and generator mechanism.")

print("Using iterator mechanism:")

def isPalindrome(str1):
    for i in range(0, int(len(str1)/2)):
        if str1[i] != str1[len(str1)-i-1]:
            return False
        return True
str1="121"
print("If The given string is palindrome then it return as True Else it return as False:",isPalindrome(str1))

print("Using Generator mechanism:")


print("-----------------------------------------------------------------------------")

''' 2. Sum of 2 digits into output
		n1 = 1234 # int(input("Enter number1 :" ))
		n2 = 9999 # int(input("Enter number2 :" ))
		Output: 9+1 2+9 3+9 4+9 
		         10 + 11 + 12 + 13
				 46
'''

print("*20, 1. Sum of 2 digits into output, * 20")


n1 = int(input("Enter the number: "))
n2 = int(input("Enter the number: "))
n1 = list(str(n1))
n2 = list(str(n2))

n3=list(map(int,n1))
n4=list(map(int,n2))
res=list(map(lambda a,b:a+b,n3,n4))
print(res)

print("Other Method")

def sum_of_two_numbers(n1, n2):
    return int(n1) + int(n2)


x = list(map(sum_of_two_numbers, n1, n2))
print(x)



print(" 3.--------------------------------------------------- ")


st = "ab@#cd!ef"
print("Reverse string considering only alphabets. Symobls should not be reversed")
# Output: fe@#dc!ba

st1 = st[::-1]
st1 = list(st1)
rev = ''
lis = []
for idx, val in enumerate(st1):
    if val.isalpha():
        lis.append(val)
    else:
        lis.insert(idx, st[idx])
rev_str = rev.join(lis)
print(rev_str)


print("4.----------------------------------------------------------")


'''4. some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
   #findout elements duplicate count output in  dict format'''

from collections import Counter
some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
counts = dict(Counter(some_list))
duplicates = {key:value for key, value in counts.items() if value > 1}
print(duplicates)

print("---------------------------------------------------------------------")



'''
5.t1 = (1, 2, 3, "a", "c") 
  t2 = ("b", "d", 9, 8, 7)
Output: (10,10,10,"ab","cd")
'''

print(''*20, "5. ---------------", '' * 20)
t1 = (1, 2, 3, "a", "c")
t2 = ("b", "d", 9, 8, 7)
lis1 = []
lis2 = []
for t in t1:
    if isinstance(t, int):
        for i in t2:
            if i not in lis2 and isinstance(i, int):
                lis2.append(i)
                lis1.append((t + i))
                break
    else:
        for i in t2:
            if i not in lis2 and isinstance(i, str):
                lis2.append(i)
                lis1.append((t + i))
                break
print(lis1)

'''
6  #Write a Python program to remove leading zeros from an IP address.
			  inp = "216.08.094.196"
			# o/p =  216.8.94.196
   
'''

print('' * 20, "6. Write a Python program to remove leading zeros from an IP address.", '' * 20)
inp = "216.08.094.196"
x = inp.replace('0', '')
print(f"IP address after removing zeros is: {x}")

print('' * 20, "7. --------------------------", '' * 20)

l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]

'''
7. l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
   #output= [1,2,3,4,5,6,7,8,9,10]
 '''
def rec(l):
    li = []
    for i in l:
        if isinstance(i, int):
            li.append(i)
        elif isinstance(i, list):
            x = rec(i)
            li.extend(x)
    return li

print(rec(l))


''' 

8. Load sample content in text file.
   Read data and find
    1. No of lines in file
	2. No of words in each line 
	3. No of chars in each line
	4. No of vowels and consonants
	5. No of special chars linewise and total 
	

'''
import os,sys
file=input("Enter the file name:")
if os.path.isfile(file):
    f=open(file,"r")
    cl=cw=cc=cv=cc=0
    vo=["a","e","i","o","u","A","E","I","O","U"]
    for i in f:
        words=i.split()
        cl+=1
        cw+=len(words)
        for j in i:
            if j.isalnum():
                cc+=1
            if j in vo:
                cv+=1

else:
    print("File not Found")
    sys.exit()


print("Number of Lines in File:",cl)
print("Number of Words in File:",cw)
print("Number of Characters in File:",cc)
print("Number of Vowels in File:",cv)
print("Number of Consonants in File:",cc-cv)




































