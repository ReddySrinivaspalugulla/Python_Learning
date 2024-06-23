def main_prog():
    print('Is this the main program?')

def return10():
    return 10

def return20():
    return 20

def main_notmain():
    if __name__ == '__main__':
        print('Original is the main program.')
        x = return10()
        print(x)
    else:
        print(f'Original is not the main program. {__name__}')
        x = return20()
        print(x)

main_notmain()
print({__name__})



#original_main = __name__ = __main__

#print(__name__)

        
        
        
