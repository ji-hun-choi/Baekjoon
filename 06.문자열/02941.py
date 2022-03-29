st1 = input()

b = st1.count("c=")
c = st1.count("c-")
d = st1.count("dz=")
e = st1.count("d-")
f = st1.count("lj")
g = st1.count("nj")
h = st1.count("s=")
i = st1.count("z=")

print(len(st1)- b-c-d-e-f-g-h-i)