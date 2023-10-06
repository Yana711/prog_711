a=list(map(int,input().split()))
b=[]
c=[]
f=a
L=0
for i in range(len(a)):
	if a[i]>=10:
		b.append(a[i])
	else:
		c.append(a[i])
d=len(b)
s=len(c)
l=[]
k=[]
for i in range(d):
	y=max(b)
	l.append(y)
	o=b.index(y)
	b.pop(o)
for i in range(s):
	u=max(c)
	k.append(u)
	t=c.index(u)
	c.pop(t)
N=[]
R=len(l)
E=len(k)
I=len(a)
print(k)
print(l)
while I!=0:
	v=k[0]
	q=l[0]
	P=l[0]
	while q>9:
		q=q//10
		print(q)
	if v>q:
		N.append(v)
		k.pop(0)
		E-=1

	elif v==q:
		W=P
		V=P
		L=0
		while W>9:
			W=W//10
			L+=1
		F=V%(L*10)
		if F==v:
			while F!=v:
				L-=1
				F=V%(L*10)
		elif F>v:
			N.append(P)
			l.pop(0)
			R-=1
		elif F<v:
			N.append(v)
			k.pop(0)
			E-=1
	elif q>v:
		N.append(P)
		l.pop(0)
		R-=1
	I-=1
	if E==0:
		k.append(0)
	if R==0:
		l.append(0)
D=[]
for i in N:
	D.append(str(i))
print(''.join(D))






