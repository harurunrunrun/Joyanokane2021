def main():
  N,K=map(int,input().split())
  ans=(N//K)**3
  if K%2==0:
    if K//2<=N%K:
      ans+=((N//K)+1)**3
    else:
      ans+=(N//K)**3
  print(ans)
  return

main()    

