def f(x,y):
    if x==y:
        return 1
    if x>y:
        return 0
    else:
        return f(x+100, y)+f(x+200, y)
print(f(1000, 3000)*f(3000, 3500))
