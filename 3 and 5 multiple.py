def multiple_of_3_and_5(start, stop):
    total_sum = 0
    for numbers in range(start, stop):
        if numbers % 3 ==0 or numbers % 5 == 0:
            total_sum = total_sum + numbers

    print(total_sum)


multiple_of_3_and_5(1,1000)
