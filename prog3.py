def f(x,y):
    if x==y:
        return 1
    if x>y or x == 2300:
        return 0
    else:
        return f(x+100, y)+f(x+200, y)+f(x+300, y)
print(f(800, 3500)*f(3500, 4200))

