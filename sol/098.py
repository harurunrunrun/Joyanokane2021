def main():
  S=list(input())
  K=int(input())
  for i in range(len(S)):
    if K==0:
      break
    elif ord("z")+1-ord(S[i])>K:
      pass
    elif S[i]!="a":
      K-=ord("z")+1-ord(S[i])
      S[i]="a"
  if K>0:
    if ord(S[-1])+K%26>ord("z"):
      S[-1]=chr(ord(S[-1])+K%26-26)
    else:
      S[-1]=chr(ord(S[-1])+K%26)
  print("".join(S))
  return

main()
