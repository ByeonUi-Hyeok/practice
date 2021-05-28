# 21.05.28 Python exercises_indexing, slicing, formatting
# make 2021 05 28 > 2021-05-28

test_filename_Str = '2021 05 28'

'''
                                    Test_filename_str = 2021 05 28
                                    INDEX             = 0123456789
'''

indexing_test_Year  = test_filename_Str [0:4] # 2021
indexing_test_Month = test_filename_Str [5:7] # 05
indexing_test_Day   = test_filename_Str [8: ] # 28

print ( indexing_test_Year  ) # 2021
print ( indexing_test_Month ) # 05
print ( indexing_test_Day   ) # 28
print ( indexing_test_Year + ' - ' + indexing_test_Month + ' - ' + indexing_test_Day ) # indexing + '-' indexing + '-' + indexing
print ( '%s - %s - %s' % ( indexing_test_Year, indexing_test_Month, indexing_test_Day ) ) # formatting (1)
print ( '{0} - {1} - {2}'.format(indexing_test_Year, indexing_test_Month, indexing_test_Day)) # formatting (2)
print ( f'{indexing_test_Year} - {indexing_test_Month} - {indexing_test_Day}' ) # formatting (3)
print ( test_filename_Str.replace(' ', ' - ') ) # function
print ( indexing_test_Year, indexing_test_Month, indexing_test_Day, sep = ' - ')