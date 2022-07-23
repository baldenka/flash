def f(x,y):
    if x==y:
        return 1
    if x>y or x == 3000:
        return 0
    else:
        return f(x+100, y)+f(x+200, y)
print(f(1000, 3500))

