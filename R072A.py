N = input().strip() # 24464 => "24464"
even_sum, odd_sum = 0, 0
for index in range(len(N)):
    digit = int(N[index])
    if (index + 1) % 2 == 1:
        odd_sum += digit
    else:
        even_sum += digit
diff = even_sum - odd_sum

print("Yes") if diff == 0 or diff % 11 == 0 else print("No")