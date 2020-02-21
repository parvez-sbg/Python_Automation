import re
string="ansb10kdjdh90jdkdk100"
pattern='\d+'
result=re.findall(pattern,string)
print(result)
for i in range(0,len(result)):
    result[i]=int(result[i])
print("the modified result is :",result)    
print(sum(result))