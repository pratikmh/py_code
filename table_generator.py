def table(n):
  for i in range(1,11):
    yield n*i
for i in table(15):
    print(i)
