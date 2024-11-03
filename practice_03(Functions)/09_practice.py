def even_generator(limit):
    for i in range(0,limit+1,2):
       yield i


for num in even_generator(10):
    print(num)