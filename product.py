
products = []

n = int(input("Enter number of products: "))

for i in range(n):
    print("\nProduct", i + 1)

    product_id = input("Enter product ID: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter stock quantity: "))

    product = (product_id, price, stock)
    products.append(product)

print("\n----- PRODUCT CATALOGUE -----")

total_value = 0

for product in products:

    product_id, price, stock = product

    value = price * stock
    total_value = total_value + value

    print("\nProduct ID:", product_id)
    print("Price:", price)
    print("Stock:", stock)
    print("Inventory value:", value)

    if price < 0 or stock < 0:
        print("Invalid product record")

    elif stock < 5:
        print("Low stock - Replenishment required")

    else:
        print("Stock available")

print("\nTotal inventory value:", total_value)
