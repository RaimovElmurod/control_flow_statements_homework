def main(a):
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    n=0
    if a>0 and n%2 == 0:
        print("two-digit odd number")
    if a>0 and n%2 == 1:
        print("two-digit even number")
    if a<0 and n%2 == 1:
        print("three-digit odd number")
    if a<0 and n%2 == 0:
        print("three-digit even number")
    if a == 0:
        return n
print(main(57))
print(main(-242))