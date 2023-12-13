def frequency_analytic(string):
  count = {}
  for c in string:
    if c in count:
      count[c] += 1
    else:
      count[c] = 1

  for key, value in sorted(count.items()):
    print(key, value)
if __name__ == "__main__":
  msg = input("input your message : ")
  frequency_analytic(msg)
