t = [1, 2, 3, 4, 5, 6]
u = 8
#def f(x):
#    x%2

f = lambda x:x>2 and not x%2

a = filter(f, t)

print (list(a))




#map-->[1, 0, 1, 0, 1, 0]
#filter-->[1, 3, 5]
#map-->[False, False, False, True, False, True]

