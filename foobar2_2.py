""" Google Foobar Level 2, Round 2 - Hey I Already Did That!

Given a minion ID as a string n representing a nonnegative integer of length k
in base b, where 2 <= k <= 9 and 2 <= b <= 10, write a function solution(n, b) 
which returns the length of the ending cycle of the algorithm above starting 
with n. For instance, in the example above, solution(210022, 3) would return 3,
since iterating on 102212 would return to 210111 when done in base 3. If the 
algorithm reaches a constant, such as 0, then the length is 1.
"""

__author__ = 'Patrick Marlow'
__version__ = '1.0'
__email__ = 'kmaphoenix@gmail.com'

def solution(n, b):

    ###### HELPER FUNCTIONS ######
    def convert_to_strings(n):
        """Simple function to handle int to str manipulation.

        Args:
          n: Integer input
        Returns:
          x: A string representation of a list sorted in descending order
          y: A string representation of a list sorted in ascending order
        """

        # list comp to convert int to individual digits
        num_list = [int(x) for x in str(n)]
        # print('The number list is: {}'.format(num_list))

        # sort num_list, list comp back to str, join back to int
        x = ''.join([str(x) for x in sorted(num_list, reverse=True)])
        y = ''.join([str(y) for y in sorted(num_list)])

        # print('The number list (X) descending is: {}'.format(x))
        # print('The number list (Y) ascending is: {}'.format(y))

        return x, y


    def convert_to_base_N(n,b,acc='',b_out=None):
        """Convert int(n) to str(r) given base b.

        Args:
          n: Input integer to convert
          b: Input base that the integer n is currently in
          acc: Accumulator for recursion
          b_out: Optional: Output base to convert the final integer to

        Returns:
          A string representing the converted input string after arithmetic 
          computation and base conversion, if necessary.s
        """
        if b_out:
            digits = [int(i,b) for i in str(n)]
            digits = digits[::-1]
            r = 0

            for i in range(len(digits)):
                r += digits[i]*b**i

            return str(r)

        else:
            while n:
                # quotient
                q = n // b
                # print('Q is: {}'.format(q))

                # remainder
                r = n % b
                # print('R is: {}'.format(r))

                # base case
                if n == 0:
                    return '0'

                elif q == 0:
                    return acc + str(r)
                
                else:
                    # recursion!
                    (n,b,acc,_) = (q, b, acc + str(r), None)
        
        return acc


    def rev_string(x):
        return ''.join([i for i in x][::-1])


    def single_pass(n,b,acc=1):
        """Main recursion loop for integer conversion and logic checks.

        Each pass through the recursion will examine the current integer n,
        perform the necessary conversions given the base b, and then check
        to see if the resulting number is part of a known pattern already.
        Once we have identified the beginning of a pattern, we will continue
        to log the longest pattern structure until we see a repeat of this 
        pattern, at which point we will return out of the function.

        Args:
          n: Input integer that is unknown to the user.
          b: Input base that is unknown to the user.
          acc: Accumulator for recursion

        Returns:
          An integer representing the length of the final list pattern
          identified during recursion.
        """
        num_list = []
        final_list = []
        final_list_stop = ''
        while acc <= 100:
            x,y = convert_to_strings(n)

            x = convert_to_base_N(int(x),b,b_out=10)
            # print('X is now: {}'.format(x))

            y = convert_to_base_N(int(y),b,b_out=10)
            # print('Y is now: {}'.format(y))

            z = int(x) - int(y) # calc z in base 10
            z = convert_to_base_N(z,b) # convert Z back to base N
            z = rev_string(z) # Reverse the string using list comp

            # adjust len(z) as necessary with padded zeros
            if len(str(z)) < len(str(n)):
                z = str(z).rjust(len(str(n)),'0')
                print('new z is: {}'.format(z))

            if z in num_list:
                print('\nwe have a match on pass {}'.format(acc))
                if z == final_list_stop:
                    return len(final_list)
                elif z not in final_list:
                    final_list_stop = z
                    final_list.append(z)
                
                print('Final List is currently {}'.format(final_list))

            num_list.append(z)
            (n,b,acc) = (z,b,acc+1)

        return num_list

    num_list = single_pass(n,b)
    print('Final Length is {}:'.format(num_list))
    return num_list

if __name__ == "__main__":
    n = 210022 # // 210022 = 711 base 10 // 1211 in base 10
    b = 3
    print('============== START HERE ==============')
    solution(n,b)