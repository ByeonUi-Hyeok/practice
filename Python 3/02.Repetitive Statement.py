# 21.05.28 For
# Use Python to find the sum of each digit of the given number
# The given number is 215179 
filename_No        = 215179                                     # Initial value of filename_No
filename_remainder = 0                                          # store the remainder
filename_sum       = 0                                          # The sum of each digit of the filename_No


filename_remainder = filename_No % 10                           # Save (215179 / 10)'s remainder               = 9    
filename_No        = filename_No // 10                          # Save (215179 / 10)'s Value without remainder = 215179            
filename_sum       = filename_sum + filename_remainder          # 0 + 9 = 9

filename_remainder = filename_No % 10                           # Save (215179 / 10)'s remainder               = 7    
filename_No        = filename_No // 10                          # Save (215179 / 10)'s Value without remainder = 21517            
filename_sum       = filename_sum + filename_remainder          # 0 + 9 + 7 = 16

filename_remainder = filename_No % 10                           # Save (215179 / 10)'s remainder               = 1    
filename_No        = filename_No // 10                          # Save (215179 / 10)'s Value without remainder = 2151            
filename_sum       = filename_sum + filename_remainder          # 0 + 9 + 7 + 1 = 17

filename_remainder = filename_No % 10                           # Save (215179 / 10)'s remainder               = 5    
filename_No        = filename_No // 10                          # Save (215179 / 10)'s Value without remainder = 215            
filename_sum       = filename_sum + filename_remainder          # 0 + 9 + 7 + 1 + 5 = 22

filename_remainder = filename_No % 10                           # Save (215179 / 10)'s remainder               = 1    
filename_No        = filename_No // 10                          # Save (215179 / 10)'s Value without remainder = 21            
filename_sum       = filename_sum + filename_remainder          # 0 + 9 + 7 + 1 + 5 + 1 = 23

filename_remainder = filename_No % 10                           # Save (215179 / 10)'s remainder               = 2    
filename_No        = filename_No // 10                          # Save (215179 / 10)'s Value without remainder = 2            
filename_sum       = filename_sum + filename_remainder          # 0 + 9 + 7 + 1 + 5 + 1 + 2 = 25

print(filename_sum)

# Use Repetitive Statement (1) for

filename_No        = 215179                                     # Initial value of filename_No
filename_sum       = 0                                          # The sum of each digit of the filename_No

for filename_tmp in str ( filename_No ) :                       # Convert numbers to string and put one digit at a time.('2','1','5','1','7','9')
    filename_tmp = int  ( filename_tmp )                         # Convert string to number ('2' > 2, '1' > 1, '5' > 5, '1' > 1, '7' > 7, '9' > 9)
    filename_sum = filename_sum + filename_tmp                  
                                                                ''' 1st round ( 0 + 2 )  = 2
                                                                    2nd round ( 2 + 1 )  = 3
                                                                    3rd round ( 3 + 5 )  = 8
                                                                    4th round ( 8 + 1 )  = 9
                                                                    5th round ( 9 + 7 )  = 16
                                                                    6th round ( 16 + 9 ) = 25 
                                                                    '''

print ( filename_sum )                                          # 25

# Use Repetitive Statement (2) while

filename_No        = 215179                                     # Initial value of filename_No
filename_sum       = 0                                          # The sum of each digit of the filename_No


while(filename_No != 0) :                                       # Repeat if filename_No isn't 0
    filename_remainder = filename_No % 10                       # remainder
    filename_No        = filename_No // 10                      # without remainder                           
    filename_sum       = filename_sum + filename_remainder      # remainer + value without remainder

print (filename_sum)
