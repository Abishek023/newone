with open('red.txt','w') as f:
    f.write("hi buddy 9 \n hii bro")
def search():
    c=0
    with open('red.txt','r') as fb:
        data=fb.readlines()
        for i in data:
            i=i.strip()
            if not i[-1].isdigit():
                c+=1
                print(i)
                print(c)
search()                
        



    
def Add():
    with open('red.txt','r') as fb:
        for line in fb:
            c=0
            if not line.strip().endswith(tuple(str(i) for i in range(10))):
                c+=1
                print(line.strip())
                print(c)
                
