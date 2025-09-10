pos_num = 0
neg_num = 0
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        print(f"Positive numbers: {pos_num} Negative numbers: {neg_num}")
        break
    if num > 0:
        pos_num = pos_num + 1
    else:
        neg_num = neg_num + 1

