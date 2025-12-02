class Poly(object):
    def sum(self,a=None,b=None,*args):
        s=0
        if a==None and b==None:
            print("provide two numbers : ")
        else:
            s=a+b
            if args:
                for i in args:
                    s+=i             
        return s
p = Poly()
print(p.sum(10,20,30,4,5,6,6,7,7,2))