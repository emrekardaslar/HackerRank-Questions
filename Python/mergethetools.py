def unqiue(list1):
    s=set()
    unqiueList=[]

    for i in list1:
        if i not in s:
            s.add(i)
            unqiueList.append(i)
    
    return ''.join(unqiueList)



def merge_the_tools(string, k):
    n=len(string)
    k = int(k)
    list1=[]
    for i in range(0,n,k):
        if i + k <=n:
           list1.append(string[i:i+k])
    
    
    for i in range(len(list1)):
        print(unqiue(list1[i]))
        
        

            

    
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

    