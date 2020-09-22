"""
# num_list = [0,1] # 1
# num_list = [0,1,2] # 3
# num_list = [0,1,2,3] # 0
# num_list = [0,1,2,3,4] # 4

# num_list = [0,1,2,3,4,5] # 1
# num_list = [0,1,2,3,4,5,6] # 7
# num_list = [0,1,2,3,4,5,6,7] # 0
# num_list = [0,1,2,3,4,5,6,7,8] # 8
"""

def get_result(x):
    if x % 4 == 0:
        return x
    elif x % 4 == 1:
        return 1
    elif x % 4 == 2:
        return x + 1
    elif x % 4 == 3:
        return 0

def solution(start,length):
  checksum = 0
  i = length

  while i > 0:
      end = (start+i) - 1
      checksum = checksum ^ (get_result(end) ^ get_result(start - 1))
      start = start + length
      i -= 1

  print(checksum)

if __name__ == '__main__':
  start = 17
  length = 4
  solution(start,length)