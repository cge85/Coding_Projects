total = 0
ticket_price = 100 
count = 5
while count > 0:
    input_age = int(input())
    if input_age > 3:
        total += ticket_price
    count -= 1
    continue
print(total)