###  python code to find the sum of numbers existing in a given string using Regex #######
################# PYTHON TUTORIAL ##############################

import re
string="ansb10kdjdh90jdkdk100"
pattern='\d+'
result=re.findall(pattern,string)
print(result)
for i in range(0,len(result)):
    result[i]=int(result[i])
print("the modified result is :",result)    
print(sum(result))
