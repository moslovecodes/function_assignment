import maskpass
if __name__=="__main__":
    user_name=input('Enter Name: ')
    pwd=maskpass.askpass(mask='*')
    print(user_name)
    print(pwd)