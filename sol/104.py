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

from collections import deque
def main():
  N,Q=pin(2)
  Graph=[[]for i in range(N)]
  for i in range(N-1):
    a,b=pin(2)
    Graph[a-1].append(b-1)
    Graph[b-1].append(a-1)
  P=[0]*N
  for i in range(Q):
    p,x=pin(2)
    P[p-1]+=x
  dq=deque([0])
  check=[0]*N
  while dq:
    q=dq.pop()
    if check[q]:
      continue
    check[q]=1
    for to in Graph[q]:
      if not check[to]:
        P[to]+=P[q]
        dq.append(to)
  print(*P,sep=" ")
  return

main()    
