def f(x,y):
    if x==y:
        return 1
    if x>y or x == 1200:
        return 0
    else:
        return f(x+100, y)+f(x+500, y)+f(x+300, y)
print(f(0, 500)*f(500, 1500))
