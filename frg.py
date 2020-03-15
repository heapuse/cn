class fragment:
    def __init__(self,size,offset,id):
        self.size = size
        self.offset = offset
        self.id = id
        
    def __str__(self):
        return 'size : ' + str(self.size) + '\noffset : ' + str(self.offset)
    
    
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

id = int(random.random()*10**9)
header_size = 20

source =client[int(input('Source : '))]
dest = client[int(input('Destination : '))]

fragments = [fragment(int(input('Initial fragment Size : ')),0,id)]
while source != dest:
    print('After',source,' to ',dest,'\n')
    temp = source
    source = eval(source)[dest]
    try:
        mtu = eval(temp+source)
    except:
        mtu = eval(source + temp)
    max_size = mtu - header_size
    index = 0
    list_ = list()
    for z in range(len(fragments)):
        
        curr = fragments[0]
        if curr.size > mtu:
            fragments.pop(0)
            max_size = max_size//8 * 8
            list_ = [fragment(max_size + 20,curr.offset + i*max_size,id) for i in range((curr.size-20)//max_size)]
            if (curr.size-20)//max_size != (curr.size-20)/max_size:
                list_.append(fragment((curr.size-20) % max_size + 20,curr.offset + (curr.size-20)//max_size*max_size,id))    
    
        fragments.extend(list_)
    for i in fragments:
        print(i)
    print("\n\n\n")
