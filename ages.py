agess={}
agess["ages"]={
    "Mehran":18,
    "Julie":18,
    "Brahm":24,
    "chris":33
    }
print(ages)
import json
s=json.dumps(agess)
print(s)
print(type(s))
with open ('D:\\ages.json','w') as f:
    f.write(s)
def get_ages():
    with open('ages.json') as f:
        ages=json.load(f)
        age=ages['Brahm']
        print('Brahm is '+str(age))
def main():
    get_ages()
if __name__=='__main__':
    main()
