def count_num(list):
  count = 0
  for n in list:
    if n==4:
      count += 1
  return count

print(count_num([1,2,3,4,5,4,4]))
