from sys import stdin

a = stdin.readline().rstrip()

a = a.replace('c=', '_').replace('c-', '_').replace('dz=', '_').replace('d-', '_').replace('lj', '_').replace('nj', '_').replace('s=', '_').replace('z=', '_')
print(len(a))
