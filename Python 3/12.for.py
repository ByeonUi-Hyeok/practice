# 21.06.03
# for문 이용 다양한 모양 만들기

#1. 
'''
*****
****
***
**
*
'''
#1-1.
print('1-1') 
for i in reversed (range(5)):
#     print (i)
    for j in range(5):
        if j <= i :
            print('*', end ='')
    print()

#1-2.
print('1-2')
for i in (range(5,0,-1)):
#    print (i)
    for j in range(1,6):
        if j <= i :
            print('*', end ='')
    print()

#1-3.
print('1-3')
for i in reversed (range(5)):
    #print (i)
    for j in range(5):
        if j <= i :
            print('*', end ='')
    print()

#1-4.
print('1-4')
for i in (range(5,0,-1)):
    print('*' * i)


#2.
'''
*****
 ****
  ***
   **
    *
'''

#2-1.
print('2-1')
for i in (range(5)):
    for j in range(5):
        if j < i :
            print(' ', end ='')
        else:
            print('*', end ='')
    print()


#3.
'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''

#3-1.
print('3-1')
for i in range(1, 6) :
    filename_blank = 5 - i
    print( filename_blank * ' ' + '*' * i,end = '' )
    if i >= 2 : 
        print('*' * (i-1), end = '\n')
        continue
    print()
for i in reversed (range(1, 5)) :
    filename_blank = 5 - i
    print( filename_blank * ' ' + '*' * i,end = '' )
    if i >= 2 : 
        print('*' * (i-1), end = '\n')
        continue
    print()

