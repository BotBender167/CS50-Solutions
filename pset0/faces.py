def convert(n):
    return n.replace(':)', '🙂').replace(':(', '🙁')

def main():
    x = input("Say something ?")
    print(convert(x))
    
main()
