num = {2, 3, 4, 5, 6}

sum_even = 0
sum_odd = 0

for n in nmu:
    if n % 2 == 0:
        sum_even += n
    else:
        sum_odd += n

print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)