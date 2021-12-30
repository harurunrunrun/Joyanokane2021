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

from math import gcd
def main():
  N,K=pin(2)
  A=pin(N,int,1)
  A.sort()
  if A[-1]<K:
    print("IMPOSSIBLE")
    return
  B=A[0]
  for i in range(1,N):
    B=gcd(B,A[i])
  if K%B==0:
    print("POSSIBLE")
  else:
    print("IMPOSSIBLE")
  return

main()    
