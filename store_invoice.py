product=[]
price=[]
name=input("Customer Name:")
number=input("Customer's Phone Number:")
while True:
    user=input("Item Purchased:")
    user1=int(input("Price:"))
    while user1<0:
        print("Price cannot be negative.")
        user1=int(input("Enter price again: "))
    product.append(user)
    price.append(user1)
    choice = input("Enter 'stop' if finished, otherwise press Enter: ").lower()
    if(choice=="stop"):
        break
print("\n========== GENERAL STORE ==========")
print(f"Customer Name: {name}")
print(f"Phone Number: {number}")

print("\n---------- PURCHASED ITEMS --------")

for x in range(len(product)):
    print(f"{product[x]} : Rs. {price[x]}")

print("-----------------------------------")
print(f"Total Bill: Rs. {sum(price)}")
print("========== THANK YOU! =============")
