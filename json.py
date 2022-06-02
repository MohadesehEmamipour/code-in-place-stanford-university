import json
def get():
    with open ('D:\\data.json') as f:
        data=json.load(f)
        name=name['person']
        print('name is '+str(name))
def main():
    get()
if __name__=='__main__':
    main()
