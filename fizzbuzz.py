for i in range(1, 1 + 16):
    if i % 15 == 0:
        print('fizzbuzz')
    if i % 5 == 0:
        print('Buzz')
    else:
        print(f'{i}')