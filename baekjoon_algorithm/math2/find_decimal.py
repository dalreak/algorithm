def prime_list(num_min,num_max):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * num_max

    # n의 최대 약수가 sqrt(num_max) 이하이므로 i=sqrt(num_max)까지 검사
    m = int(num_max ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, num_max, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(num_min, num_max) if sieve[i] == True]

reference_prime_list = prime_list(2,10000+1)
for i in range(int(input())):
    test_num = int(input())
    result = [test_num//2,test_num//2]
    while result[0] not in reference_prime_list or result[1] not in reference_prime_list:
        result[0] = result[0] - 1
        result[1] = result[1] + 1
    print(result[0],end=" ")
    print(result[1])

