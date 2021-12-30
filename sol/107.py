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
  H,W=pin(2)
  N=pin(1)
  a=pin(N,int,1)
  C=[[0]*W for i in range(H)]
  cnt=1
  for i in range(H):
    for j in range(W):
      C[i][j]=cnt
      a[cnt-1]-=1
      if a[cnt-1]==0:
        cnt+=1
  for i in range(H):
    if i%2==1:
      C[i]=C[i][::-1]
    for j in range(W):
      print(C[i][j],end=" ")
    print()
  return

main()
