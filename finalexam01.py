print("i\tm(i)")
for i in range(1,902,100):
    m = 0
    for j in range(1, i+1, 1):
        m = m + ((-1)**(j+1))/(2*j-1)
    m=m*4
    print(j,"\t",m)
