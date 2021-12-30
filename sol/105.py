from collections import deque
def main():
  N,K=map(int,input().split())
  S=input()
  A=[]
  A.append([1,int(S[0])])
  for i in range(1,N):
    if A[-1][1]==int(S[i]):
      A[-1][0]+=1
    else:
      A.append([1,int(S[i])])
  dq=deque()
  ans=0
  cnt=0
  S=0
  for i in range(len(A)):
    while A[i][1]==0 and cnt>=K:
      if dq[0][1]==1:
        S-=dq[0][0]
        dq.popleft()
      else:
        S-=dq[0][0]
        cnt-=1
        dq.popleft()
    if A[i][1]==1:
      S+=A[i][0]
      dq.append(A[i])
    else:
      S+=A[i][0]
      dq.append(A[i])
      cnt+=1
    ans=max(ans,S)
  print(ans)
  return

main()
