n = input()
sum = 1
def sum_print(n):
   for i in range(2,n+1):
      sum = sum * i
   return sum

count = 0
def count_print(n):
   for i in range(1,n+1):
      count = count + i
   return count
print(count_print(n))
print(sum_print(n))

