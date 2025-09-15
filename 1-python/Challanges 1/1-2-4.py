shopping_list = {}
while True:
    item = input("Enter a grocery item: ")
    if item == "quit":
        break
    quantity_item = int(input("Enter the quantity of the item: "))
    if item in shopping_list:
        shopping_list[item] += quantity_item
    else:
        shopping_list[item] = quantity_item
print(shopping_list)