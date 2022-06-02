import json
def write_data():
	data={"Name":"Rozita","Age":22}
	with open('name.json','w') as f:
		json.dump(data,f,indent=4)
def main():
	write_data()
	get_ages()
def get_ages():
    with open('name.json') as f:
        ages=json.load(f)
        age=ages['Name']
        print('Name is '+str(age))

if __name__ == "__main__":
    main()
