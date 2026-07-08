for i in range (1,101):
   if (i % 3== 0 or i % 5 == 0) and not (i % 3 == 0 and i % 5 == 0):
        print(i)