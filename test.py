i=0
def hi():
    global i
    print i
    i+=1
    print i

def hi2():
    print i

if __name__=='__main__':
    hi()
    hi2()