def comb_mod(n,r,mod):
  if n<r:
    return 0
  if n-r<r:
    r=n-r
  N=n
  R=r
  u=1
  d=1
  for i in range(r):
    u*=N
    u%=mod
    N-=1
    d*=R
    d%=mod
    R-=1
  return u*pow(d,mod-2,mod)%mod

def main():
  X,Y=map(int,input().split())
  mod=10**9+7
  if 2*X-Y>=0 and 2*Y-X>=0 and (2*X-Y)%3==0 and (2*Y-X)%3==0:
    m=(2*X-Y)//3
    n=(2*Y-X)//3
    print(comb_mod(n+m,n,mod))
  else:
    print(0)
  return

main()    
