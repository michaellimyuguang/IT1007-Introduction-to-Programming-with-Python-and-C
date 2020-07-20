'''
Full Name:
Matric No.:
Email:
Tutorial Group Number:
Your Tutor Name:
'''

#Given code
def factorial_iterative(n):
    ans = 1
    for i in range(2,n+1):
        ans *= i
    return ans

def factorial_recursion(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursion(n-1)
    
#Complete Q1a below
def nChooseK(n,k):
    return 0 #change the code here

#Complete Q1b below
def nChooseK_recursive(n,k):
    return 0 #change the code here

#Complete Q2a below
def fib_recursive(n):
    return 0 #change the code here

'''
What is the biggest number you can compute for fib_recursive() and why?
Submit your answer HERE



'''

    
#Complete Q2b below
def fib_sum(n):
    return 0 #change the code here
    




