## SUBMITTED SOLUTION ## 

"""
Constraints:
  IDs will be between 0 and 2,000,000,000 inclusive
Args:
  start = the ID of the first worker
  length = the length of 1 iteration of the line

Returns:
  checksum = XOR'd value of all worker IDs

0 1 2 /
3 4 / 5
6 / 7 8

Test Cases:
  Input: (0,3)
  Output: 2

  Input: (17,4)
  Output: 14
"""

start = 1999999999
line_length = 2
checksum = 0
i = line_length

import functools

# num_list = [0,1] # 1
# num_list = [0,1,2] # 3
# num_list = [0,1,2,3] # 0
# num_list = [0,1,2,3,4] # 4

# num_list = [0,1,2,3,4,5] # 1
# num_list = [0,1,2,3,4,5,6] # 7
# num_list = [0,1,2,3,4,5,6,7] # 0
# num_list = [0,1,2,3,4,5,6,7,8] # 8

def get_result(x):
    if x % 4 == 0:
        return x
    elif x % 4 == 1:
        return 1
    elif x % 4 == 2:
        return x + 1
    elif x % 4 == 3:
        return 0

while i > 0:
    # line = list(range(start, start+i))
    end = (start+i) - 1
    checksum = checksum ^ (get_result(end) ^ get_result(start - 1))
    start = start + line_length
    i -= 1
    # print('Current checksum is {}'.format(checksum))
    # print('\n')

print(checksum)