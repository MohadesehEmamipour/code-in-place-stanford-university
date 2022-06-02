person={}
person['leo']={
    'name':'leo',
    'address':'Tamilnadu'
    }
print(person)
import json
s=json.dumps(person)
print(s)
print(type(s))
with open ('D:\\data.json','w') as f:
    f.write(s)
