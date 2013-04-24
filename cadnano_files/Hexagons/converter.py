name = "save_file_test.json"

fin = open(name,'r')
fout= open(name+"_readable2.txt", 'w')
line= fin.readline()

n=0
secondQuote=0
temporaryString=""
while n <len(line):
  #  print s[n]
    temporaryString=temporaryString+line[n]
    
    if line[n]=='}':
     temporaryString=temporaryString+" \n"
     fout.write(temporaryString)
     temporaryString=""
     
    else:
     if line[n]=='"' :
      if secondQuote==0:
          temporaryString="\n "+temporaryString
          fout.write(temporaryString)
          temporaryString=""
          secondQuote=1
     else:
          secondQuote=0
     
    n=n+1
print "complete"
