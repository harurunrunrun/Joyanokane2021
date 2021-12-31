class INPUT:
  def __init__(self):
    self._l=open(0).read().split()
    self._length=len(self._l)
    self._index=0
    return

  def stream(self,k=1,f=int,f2=False):
    assert(-1<k)
    if self._length==self._index or self._length-self._index<k:
      raise Exception("There is no input!")
    elif f!=str:
      if k==0:
        ret=list(map(f,self._l[self._index:]))
        self._index=self._length
        return ret
      if k==1 and not f2:
        ret=f(self._l[self._index])
        self._index+=1
        return ret
      if k==1 and f2:
        ret=[f(self._l[self._index])]
        self._index+=1
        return ret
      ret=[]
      for _ in [0]*k:
        ret.append(f(self._l[self._index]))
        self._index+=1
      return ret
    else:
      if k==0:
        ret=list(self._l[self._index:])
        self._index=self._length
        return ret
      if k==1 and not f2:
        ret=self._l[self._index]
        self._index+=1
        return ret
      if k==1 and f2:
        ret=[self._l[self._index]]
        self._index+=1
        return ret
      ret=[]
      for _ in [0]*k:
        ret.append(self._l[self._index])
        self._index+=1
      return ret
pin=INPUT().stream

#pin(number[default:1],f[default:int],f2[default:False])
#if number==0 -> return left all
#listを変数で受け取るとき、必ずlistをTrueにすること。


def main():
  N,M=pin(2)
  A=pin(N,int,1)
  Graph=[[]for i in range(N)]
  for i in range(M):
    X,Y=pin(2)
    Graph[X-1].append(Y-1)
  P=[float("inf")]*N
  ans=-float("inf")
  for i in range(N):
    ans=max(ans,A[i]-P[i])
    P[i]=min(P[i],A[i])
    for to in Graph[i]:
      P[to]=min(P[to],P[i])
  print(ans)
  return

main()
