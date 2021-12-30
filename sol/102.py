from math import isqrt
def main():
  N=int(input())
  M=isqrt(N)
  for i in range(M,N+1):
    S=0
    ans=[]
    for j in range(i,0,-1):
      if S+j<=N:
        S+=j
        ans.append(j)
    if S==N:
      print(*ans,sep="\n")
      return
  return

main()
