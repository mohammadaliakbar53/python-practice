numbers=[]
for x in range(5):
  num=int(input("Enter a number: "))
  numbers.append(num)
largest=numbers[0]
smallest=numbers[0]
for i in numbers:
  if(i>largest):
    largest=i
  if(i<smallest):
    smallest=i
print(f"Smallest: {smallest}")
print(f"Largest: {largest}")
