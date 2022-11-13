def f(a, b):
    print(f"({a**2+b**2}, {abs(a**2-b**2)}, {abs(2*a*b)})")

def main():
    run = True
    while run:
        x = int(input("enter an integer.\n> "))
        y = int(input("enter another integer.\n> "))
        print("here's a pythogrean triple:")
        f(x, y)
        if input("\nwanna retry? (y/n)\n> ") in ("n", "N", "no", "No", "NO", "nO"):
            run = False
        else:
            run = True

if __name__ == '__main__':
    main()
