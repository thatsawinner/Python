#!/usr/bin/python3
import sys

def main():
    next_biggest_number(sys.argv[1])

def next_biggest_number(num):

    # search number digit by digit from right to left.
    # find an occurance where the next digit from the 
    # right is smaller than the current digit.
    num = str(num)
    for i in range(len(num)-1, -1, -1):
        if num[i] > num[i-1]:
            break
             
    # if no smaller digit occurance is found, print -1
    if i == 0:
#        print(-1)
        return -1
    
    # a smaller digit occurance was found.
    # split the number in to what you want to keep and
    # what you want to analyze.
    d_pre = num[:i]
    d_post = num[i:]
#    print("d_pre: " + d_pre)
#    print("d_post: " + d_post)
    
    # test which if the remaining digits is bigger than
    # the digit split on and the smallest of all the 
    # remaining digits.
    s = 0 # start are beginning of remaining digits.
#    print("len(d_post): " + str(len(d_post)))
    for j in range(0, len(d_post), 1):
#        print("d_post[j]: " + d_post[j])
#        print("num[i-1]: " + num[i-1])
#        print("d_post[j]: " + d_post[j])
#        print("d_post[s]: " + d_post[s])
        if d_post[j] > num[i-1] and d_post[j] <= d_post[s]:
#            print("s: " + str(s))
            s = j

    # swap the smallest digit from post that is larger
    # than the digit the number was split on.
    # sort ascending the new post digits, and append
    # back on to the pre digits.
    new_pre = list(d_pre)
    new_post = list(d_post)
#    print(new_post)
#    print(new_post[0])
    
#    print("d_post[s]: " + d_post[s-1])
#    print("num[i]: " + num[i-1])
#    if d_post[s] >= num[i]:
    new_pre[len(d_pre)-1] = d_post[s]
    new_post[s] = d_pre[len(d_pre)-1]
    next_num = ''.join(new_pre) + ''.join(sorted(new_post))
    next = int(next_num)
    print(next)
    return next

if __name__ == "__main__":
    main()