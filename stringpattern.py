def pattern(number):
    answer = ''
    for i in range(1,number+1):
        if i%2==0:
            answer = answer + '0'
        elif i%2==1:
            answer = answer + '1'
        print(answer)

N = int(input('Enter the number N: '))
print(f'N = {N}: ')
ans = pattern(N)