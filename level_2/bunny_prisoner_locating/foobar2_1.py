def solution(x,y):
    # num = 1
    start_x = 1
    num = int((((y + 0)*(y - 1))/2)+1)

    def pattern(x, y, start_x, num):
        
        # base case
        while start_x <= x:

            if (start_x,y) == (x,y):
                print(str(num))
                return num
                
            # recursion
            (x, y, start_x, num) = (x, y, start_x+1, num+start_x+y)
        return x

    value = pattern(x, y, start_x, num)

    return str(value)

if __name__ == '__main__':
    # solution(2,3)
    solution(5,10)