def find_class(p):
    r=p[0]
   
    if r>=1 and r<=127:
        c='A'
    elif r>=128 and r<=191:
        c='B'
    elif r>=192 and r<=254:
        c='C'
    return c
   
n_m=input('Enter the network ID in CIDR notation:')
s=n_m.split('/')
g_ip=s[0]
mask=s[1]
mask=int(mask)

g_ip=g_ip.split('.')
g_ip=[int(i) for i in g_ip]

print(g_ip)
print(mask)

clas=find_class(g_ip)

print(clas)

q=mask//8
r=mask%8

net_mask=[]
for i in range(q):
    net_mask.append(255)
   
l=7    
sum1=0
for j in range(r):
    sum1=sum1+2 ** l
    l=l-1
net_mask.append(sum1)

if len(net_mask)<4:
    while len(net_mask)<4:
        net_mask.append(0)
       

print(net_mask)

net_id=[]
for j in range(len(net_mask)):
    net_id.append(net_mask[j] & g_ip[j])
   
b_net=[]
for j in range(len(net_mask)):
    b_net.append(bin(net_id[j]).replace("0b",""))
   
clas=find_class(net_id)
print('The network id is :',net_id)
print('The class is:',clas)

h_max=[]
#maximum
for j in range(q):
    h_max.append(net_id[j])

sum2=0
k=(8-r-1)
for j in range(k,-1,-1):
    sum2=sum2+(2 **j)

if len(h_max)==3:
    sum2=sum2-1
    h_max.append(sum2)
elif len(h_max)<3:
    h_max.append(sum2)
    while len(h_max)<3:
        h_max.append(255)
    h_max.append(254)

#print('The maximum host is :',h_max)
    
#minimum
h_min=[]

for i in range(q):
    h_min.append(net_id[i])


if len(h_min)==3:
    h_min.append(1)
elif len(h_min)<3:
    while len(h_min)<3:
        h_min.append(0)
    h_min.append(1)

#print('The minimum host is:',h_min)
        
#broadcast
broad=[]

for j in range(q):
    broad.append(net_id[j])

sum3=0
k=(8-r-1)

for j in range(k,-1,-1):
    sum3=sum3+(2 ** j)

if len(broad)==3:
    broad.append(sum3)
elif len(broad)<3:
    while (len(broad)<3):
        broad.append(255)
    broad.append(sum3)        
    
#print('The broadcast is:',broad)
host_max=[str(i) for i in h_max]
host_max='.'.join(host_max)
host_min=[str(i) for i in h_min]
host_min='.'.join(host_min)
broadcast=[str(i) for i in broad]
broadcast='.'.join(broadcast)

print('Broadcast IP:',broadcast)
print('Minimum Host IP:',host_min)
print('Maximum Host IP:',host_max)