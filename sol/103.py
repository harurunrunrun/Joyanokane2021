def main():
  S=input()
  T=input()
  d=[i for i in range(26)]
  changed=[0]*26
  for i in range(len(S)):
    if d[ord(S[i])-97]==ord(T[i])-97:
      changed[ord(T[i])-97]=1
      continue
    A=d[ord(S[i])-97]
    B=ord(T[i])-97
    for j in range(26):
      if d[j]==A:
        if changed[d[j]]:
          #print(i,chr(j+97),chr(d[j]+97))
          print("No")
          return
        d[j]=B
      elif d[j]==B:
        if changed[d[j]]:
          #print(i,chr(j+97),chr(d[j]+97))
          print("No")
          return
        d[j]=A
    changed[B]=1
  print("Yes")
  return
      
main()
