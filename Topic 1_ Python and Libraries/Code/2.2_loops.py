# print 'hello' 3 times
# n = 3

## ----- 1. while loop
# i = 0
# while i<3:
#     print('Hello')
#     i += 1 # equals i = i + 1

## ------ 2. for loop
# for i in range(3):
#     print('Hello')

# for i in range(4):
#     if i == 1:
#         continue
#     print(i)
# s = "Hello, Jin! kdjfl yej kj, jfk, 08857"
# # s = s[2:5]
# print (s)
# print (len(s)-1)
# ##                    s[0:2] ==s[:2]
# ##                      s[-1]  => !
# ##                      s[-2:0] => n! 
# ## you can not change the string value
# ##
# y= 'h'+s[1:] # how to change the first
# print (y)

# y.split()
# print(y)
# y.split(',')
# print(y)
# y.split(', ')
# print(y)

# # >>> s[:2]
# # 'He'
# # >>> s[-1]
# # '!'
# # >>> s[-2:]
# # 'n!'
list_1 = [20, 30, 50 ]
list_2 = ['Rutgers', 'NJ', 2, 3]
m = [[2,0], [2,3], 5]
print(m[0][1])
'''
#a = m.append(5) # print(a) shows "none"
## m.add(50) # list cannot use "add"
print(m)
list_1.sort()
print('list_1',list_1)
list_1.sort(reverse = True)
print('list_1 reverse',list_1)
m.extend(list_2)
print('m.extend(list_2)', m)
b = list_1 + list_2
print('b = list_1 + list_2',b)
'''
#------- in ---------------- 'lists' are mulable vs 'string' is not 
s = [1, 2]
print(1 in s)
print(3 in s)

# #-------------- map tranditional for loop ----------------------
n = [ 1, 2, 3 , 4]
# c =[]
# for i in range(len(n)):
#     d = n[i]
#     square = d**2
#     c.append(square)
# print(c)

#-------------------------- MAP fuction ----------------
def square_value(x):
    return x ** 2

square = map(square_value, n)
print(square) # print <map object at 0x0000026FAADDD090>

square = list(square)
print('list(square)',square) 
'''
# lamda function 
square = lambda x: x**3
s = square(2)
print(' 2x2x2 =',s)

#--------------- map + lambda fuction
square = map(lambda x: x** 2, number)
square = list(square)
print(square)
'''
#------------- filter ---------------
num = [1, -2, 3, -4]
positive_num = filter(lambda x: x>0, num)
print('postitive',positive_num)
positive_num = list(positive_num)
print('postitive',positive_num)

#------------- list comprehension
p = [1,2,2,3,-4]
squares = [i**2 for i in p if i>0]

print(squares)