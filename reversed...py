def reverse(original):
    reversed={}
    for key in original:
        value=original[key]
        if not value in reversed:
            reversed[value]=[]
        reversed[value].append(key)
    return reversed
            
def main():
    reverse(original)
    
    

if __name__=='__main__':
    main()
