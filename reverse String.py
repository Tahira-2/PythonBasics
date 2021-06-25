def reverseString(s):
  reverse = ''
  for i in range(len(s)-1, -1, -1):
    reverse+= s[i]
  return reverse

reverseString('I love to sleep')
