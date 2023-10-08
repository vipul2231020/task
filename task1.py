class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
        # using getter and setter 
    def getn(self):
        return str(self.real)+"+"+str(self.img)+"i"
    def setn(self,r,i):
        self.real=r
        self.img=i
def addcomplex(n1,n2):
        ans_real = n1.real+n2.real
        ans_img = n1.img + n2.img
        return str(ans_real)+"+"+str(ans_img)+"i"    
def subcomplex(n1,n2):
       ans_real = n1.real-n2.real
       ans_img = n1.img - n2.img
       return str(ans_real)+"+"+str(ans_img)+"i"  
def multiplycomplex(n1,n2):  
    ans_real = n1.real*n2.real - n1.img*n2.img 
    ans_img = n1.img * n2.real+ n1.real*n2.img
    return str(ans_real)+"+"+str(ans_img)+"i" 
def dividecomplex(n1,n2):  
    denominator = (n2.real**2) + (n2.img**2)
    ans_real = ((n1.real * n2.real) + (n1.img * n2.img)) / denominator 
    ans_img = ((n1.img * n2.real) - (n1.real * n2.img)) / denominator
    return str(ans_real)+"+"+str(ans_img)+"i"   
    
    
obj1= complex(3,4)
obj2= complex(5,2)
print("complex number c1 is:",obj1.getn())
print("complex number c2 is:",obj2.getn())
print ("Add c1+c2 : ", addcomplex(obj1,obj2))
print ("sub c1-c2 : ", subcomplex(obj1,obj2))
print ("multiply c1*c2 : ", multiplycomplex(obj1,obj2))
print ("divide c1/c2 : ", dividecomplex(obj1,obj2))