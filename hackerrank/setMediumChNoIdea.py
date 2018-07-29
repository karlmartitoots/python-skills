# https://www.hackerrank.com/challenges/no-idea/problem

mn = input().split()
m = int(mn[0])
n = int(mn[1])
array = input().split()
A = set(input().split())
B = set(input().split())

print(sum([(el in A) - (el in B) for el in array]))