f=open("TweetStream.txt",'r+')
count=1;
for line in f:
  temp=open(str(count)+".txt",'w+')
  temp.write(line)
  temp.close()
  count+=1
f.close()  
