def isHappy(n):
  sadlist=[]
  while True:

    sadlist.append(n)
    k=0
    while n!=0:
      k+=(n%10)**2
      n=n//10
    n=k
    if n==1:
      return True
    if n in sadlist:
      return False

  return

if __name__=="__main__":
  sample0_output = isHappy(19)
  sample1_output = isHappy(2)

  with open("/app/bind_mount/output.txt", "w") as f:
    f.write(f"19: {sample0_output}\n")
    f.write(f"2: {sample1_output}\n")
  print("Results saved to /app/bind_mount/output.txt")