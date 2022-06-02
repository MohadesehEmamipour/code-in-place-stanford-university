import json
def main():
    my_file=open('results.json','w')
    data=json.load(my_file)
    print(data)
    if __name__=='__main__':
        main()
