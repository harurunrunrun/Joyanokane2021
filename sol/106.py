def main():
  A,B=map(int,input().split())
  c=1
  A=max(0,A-1)
  ans=0
  for i in range(50):
    cntB=(B+1)//(2*c)*c+max(0,(B+1)%(2*c)-c)
    cntA=(A+1)//(2*c)*c+max(0,(A+1)%(2*c)-c)
    ans+=(cntB-cntA)%2*c
    #print(cntB,cntA)
    c*=2
    if c>B:
      break
  print(ans)
  return

main()
