#https://www.hackerrank.com/challenges/symmetric-difference/problem

m = input()
A = set(map(int,input().split()))
n = input()
B = set(map(int,input().split()))


print(*sorted(A.union(B)-A.intersection(B)),sep='\n')