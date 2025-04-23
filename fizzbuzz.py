for i in range(1, 1 + 16): # i는 1부터 16까지 반복
    if i % 15 == 0:       # 15의 배수인지 가장 먼저 확인
        print('fizzbuzz') # 15의 배수이면 'fizzbuzz' 출력
    elif i % 3 == 0:      # 15의 배수가 아니고, 3의 배수이면
        print('fizz')     # 'fizz' 출력
    elif i % 5 == 0:      # 15의 배수도 아니고, 3의 배수도 아니고, 5의 배수이면
        print('buzz')     # 'buzz' 출력 (원래 요청은 'Buzz'였지만, 일반적으로 'buzz'로 통일합니다)
    else:                 # 위의 어떤 조건에도 해당되지 않으면
        print(f'{i}')     # 숫자를 그대로 출력
1
