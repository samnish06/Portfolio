def sum_divisors(x):
  sum = 0
# for each i in list
  for i in range(1, x ):
       if x % i == 0:
           sum+=i

  # Return the sum of all divisors of n, not including n
  return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114
for x in range(6):
  print (x)
for x in range(1,30,5):
  print (x)
  def retry(operation, attempts):
   for n in range(attempts):
    if operation():
      print("Attempt " + str(n) + " succeeded")
    
    else:
        print("Attempt " + str(n) + " failed")

retry(create_user, 3)
retry(stop_service, 5)