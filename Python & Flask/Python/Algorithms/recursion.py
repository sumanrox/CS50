# Recursion to print a pyramid

def draw(height):
    if height==0:
        return
    draw(height-1)
    for i in range(height):
        i=i+1
        print("#"),
    print("\n")

draw(int(input("[*] Enter Height : ")))