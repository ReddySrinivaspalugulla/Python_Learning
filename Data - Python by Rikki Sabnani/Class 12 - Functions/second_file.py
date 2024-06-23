import original_main

print(f'Name variable of second_file in this script is set to : {__name__}.')
print(f'Name variable of original main imported file in this script is set to :\
{original_main.__name__}.')

original_main.main_notmain()


#not_main = __name__ = __main__
#original_main = __name__ = __original_main__

#print(__name__)
#print(original_main.__name__)