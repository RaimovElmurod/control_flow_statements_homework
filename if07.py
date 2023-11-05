def main(a):
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"
    n=0
    if a>0 and n%2 == 1:
        print("positive odd number")
    if a>0 and n%2 == 0:
        print("positive odd number")
    if a<0 and n%2 == 1:
        print("negative even number")
    if a<0 and n%2 == 0:
        print("negative even number")
    if a == 0:
        print("a=0")

    return n
print(main(57))
print(main(-24))