"""
Input:
1. Start = money have before selling
2. String of b and c = b->big cookie c->normal cookie

Output:
1. Number of total cookies sold
2. Profit (which is calculated as profit = sales - cost of cookie)
Cost of Normal Cookie per cookie → $1.25
Cost of Big cookie per cookie → $2.00
To make a normal cookie → $0.50
To make a big cookie → $0.75
3. Total amount of money after selling cookies
"""
#input:
start = float(input()) # float=real number
cookie_sold = input()

#processing:
big_cookies = cookie_sold.count('b')
normal_cookies = cookie_sold.count('c')

"""
for current_cookie in cookie_sold:
    #gives each letter in the word
    if current_cookie == "c":
        normal_cookies += 1
    elif current_cookie == "b":
        big_cookies += 1
    else:
        print(f"{current_cookie} is not a valie sale item.")
"""

cookies = normal_cookies + big_cookies
profit = (1.25*normal_cookies-0.5*normal_cookies) + (2.00*big_cookies-0.75*big_cookies)
total = start+profit
print(f"{cookies} cookies sold in total. Profit made is ${profit}. Total amount of money made is ${total}.")