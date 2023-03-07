# get a b c d int value from user using only one input function and check which one is maximum



# a, b, c, d = input("Enter a b c d value: ").split()
a, b, c, d = map(int, input("Enter a b c d value: ").split())

# if a > b and a > c and a > d:
#     print("a is maximum")
# elif b > a and b > c and b > d:
#     print("b is maximum")
# elif c > a and c > b and c > d:
#     print("c is maximum")
# else:
#     print("d is maximum", d)

print(type(a))