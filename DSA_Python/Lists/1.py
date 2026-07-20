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

    
        




l= MyList()
print(len(l))
l.append("hello")
l.append("hello")
l.append("hello")

l.append("hello")
l.append("hello")
l.append("hello")
l.append("hello")
l.append("hello")
print(len(l))


