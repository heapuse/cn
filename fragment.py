class fragment:
    def __init__(self,size,off,id):
        self.size = size
        self.off = off
        self.id = id
        
    def disp(self):
        print("Size = ",self.size)
        print("Offset = ",self.off)
        print("Id = ",self.id,end = "\n\n")
        
AC = 1500
AD = 3500
BC = 1000
CD = 2000
CF = 1000
DE = 1500
FE = 1400

client = {1:'A', 2:'B', 3:'E', 4:'F'}
A = {'B':'C', 'C':'C', 'D':'D', 'E':'C', 'F':'C'}
B = {'A':'C', 'C':'C', 'D':'C', 'E':'C', 'F':'C'}
C = {'A':'A', 'B':'B', 'D':'D', 'E':'F', 'F':'F'}
D = {'A':'A', 'B':'C', 'C':'C', 'E':'E', 'F':'E'}
E = {'A':'D', 'B':'F', 'C':'F', 'D':'D', 'F':'F'}
F = {'A':'C', 'B':'C', 'C':'C', 'D':'E', 'E':'E'}

s = int(input("Enter the source client number : "))
d = int(input("Enter the destination client number : "))
p_s = int(input("Enter the packet size : "))

p1 = client[s]
p2 = client[d]

frag_list = list()

frag_list.append(fragment(p_s,0,'P1'))

while p1 != p2:
    for i in frag_list:
        i.disp()
    print(p1, end = ' -> ')
    temp = p1
    p1 = eval(p1)[p2]
    
    try:
        mtu = eval(temp + p1)
    except NameError:
        mtu = eval(p1 + temp)
        
    i = 0
    tf = list()
    while i < len(frag_list):
        t = frag_list[i]
        
        if t.size - 20 > mtu - 20:
            s = mtu - 20 
            while s % 8 != 0:
                s -= 1
                
            del frag_list[i]
            
            j = 0
            while t.size - 20 - s >= 0:
                tf.append(fragment(s+20,t.off+(j*s),'P1'))
                j += 1
                t.size -= s
                
            if t.size - 20 != 0:
                tf.append(fragment(t.size,t.off+(j*s),'P1'))
            i -= 1
        i += 1
        
    frag_list.extend(tf)
    del tf
                
print(p2)

for i in frag_list:
    i.disp()
