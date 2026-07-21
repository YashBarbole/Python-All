#dynamic array 
# pythoon list is also dynamic arr
import ctypes

class MyList:
    def __init__(self):
        self.size=1
        self.n=0
        #create c type arr with size =self.size
        self.A=self.make_arr(self.size)

    def make_arr(self,capacity):
        return (capacity*ctypes.py_object)()
# this code creates c type arr with size capacity

    def __len__(self):
        return self.n
    
    def append(self,item):
        if self.n==self.size:
            #resize
            self.resize(self.size*2)
    
        self.A[self.n]=item
        self.n=self.n+1

    def resize (self,new_capacity):
        #create new arr with new capacity
        B= self.make_arr(new_capacity)
        self.size= new_capacity

        #copy A to B
        for i in range(self.n):
            B[i]= self.A[i]

        #reassign A
        self.A= B
    
    def __str__(self):
        result=''
        for i in range(self.n):
            result+=str(self.A[i]) +','

        return '[' + result[:-1]+']'
    
    def __getitem__(self, index):
        if 0<=index <self.n:
         return self.A[index]
        else :
            return "index out of range my boi"
        
    def pop(self):
        if self.n==0:
            return "empty list"
        
       
        self.n= self.n-1

    def clear(self):
        self.size=1
        self.n=0

    def find(self,item):

        for i in range(self.n):
            if self.A[i]== item:
                return i
          
        return"not in list"
    
    def insert(self,pos,item):
        if self.n==self.size:
            self.resize(self.size*2)
        
        for i in range (self.n,pos,-1):
            self.A[i]=self.A[i-1]
        
        self.A[pos]=item
        self.n+=1
    
    def __delitem__(self, pos):
        if 0<=pos<self.n:
         for i in range (pos,self.n-1):
            self.A[i]=self.A[i+1]
        
        self.n=self.n-1

    def remove(self,item):
       pos= self.find(item)

       if type(pos)== int:
           self.__delitem__(pos)
           
       else:
           return pos
           


        
 
        
    


        

l= MyList()
print(len(l))
l.append("hello 1")
l.append("hello 2")
l.append("hello 3")
l.append(4)

print(l)
l.pop()
print(l)


print(l)

l.find("hello 6")

l.insert(0,0)
print(l)

del l[3]
print(l)

l.remove(0)
print(l)