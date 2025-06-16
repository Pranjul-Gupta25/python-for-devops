#function for findall


import re




result ="pranjul Gupta is devops engineer and working in high paying job"

pattern = r"working in high"

search = re.search(pattern, result)


print("pattern found:" , search.group())







#function for findall


import re




result ="pranjul Gupta is devops engineer and working in high paying job"

pattern = r"workgin in high"

search = re.search(pattern, result)

if search:
    print("pattern found:" , search.group())


else:
    print("pattern not found")




#function for regex-match

import re 



text = "pranjul Gupta is devops engineer and working in high paying job"
pattern = r"Gupta is devops"

match =re.match(pattern, text)

if match:
    print("match found:" , match.group())

else:
    print("no match")



#for regex-replace



import re 


text = "pranjul Gupta is devops engineer and working in high paying job"

pattern = r"devops"

replacement = "cloud"

newtxt = re.sub(pattern , replacement, text)

print("modified text is :" , newtxt)





# regex-search 


import re



text = "pranjul Gupta is devops engineer and working in high paying job"
pattern = r"Gupta is devops"

search =re.search(pattern, text)

if search:
    print("search found:" , search.group())

else:
    print("no match")




text = "pranjul Gupta is devops engineer and working in high paying job"
pattern = r"Gupta is cloud"

search =re.search(pattern, text)

if search:
    print("search found:" , search.group())

else:
    print("no match")







#regex-split


text = "pranjul , Gupta , is , devops , engineer , and , working in high paying job"
pattern = r","


split = re.split(pattern, text)

print("split result:" , split)























