class dijkstra:
  def __init__(self,V):
    self.INF=float("inf")
    self.G=[[] for _ in [0]*V]
    self.V=V
    return

  def add1(self,s,t,v):
    self.G[s].append([t,v])
    return

  def add2(self,s,t,v):
    self.G[s].append([t,v])
    self.G[t].append([s,v])
    return

  def run(self,s):
    from heapq import heapify,heappop,heappush
    ret=[self.INF]*self.V
    que=[]
    heapify(que)
    ret[s]=0
    heappush(que,(0,s))
    while que:
      p=heappop(que)
      v=p[1]
      if ret[v]<p[0]:
        continue
      for i in range(len(self.G[v])):
        e=self.G[v][i]
        if ret[e[0]]>ret[v]+e[1]:
          ret[e[0]]=ret[v]+e[1]
          heappush(que,(ret[e[0]],e[0]))
    return ret

def main():
  H,W=map(int,input().split())
  S=[]
  white=0
  for i in range(H):
    L=input()
    for j in range(W):
      if L[j]==".":
        white+=1
    S.append(L)
  ijk=dijkstra(H*W)
  for i in range(H):
    for j in range(W):
      if S[i][j]=="#":
        continue
      if i+1<H and S[i+1][j]==".":
        ijk.add2(i*W+j,(i+1)*W+j,1)
      if j+1<W and S[i][j+1]==".":
        ijk.add2(i*W+j,i*W+j+1,1)
  cost=ijk.run(0)[H*W-1]
  if cost==float("inf"):
    print(-1)
  else:
    print(white-cost-1)
  return

main()
