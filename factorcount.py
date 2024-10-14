def factor_count(number):
    counter = 0
    for divider in range(1,number+1):
        if number%divider==0:
            counter+=1
    return counter

upperlimit = int(input('Enter the number N: '))
for dividend in range(1,upperlimit+1):
    num = factor_count(dividend)
    print(f'{dividend} has {num} factors.')