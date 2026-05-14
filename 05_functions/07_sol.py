# 8. Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def print_key_value_args(name, power):
    print('name =',name ,'power =', power)
    
# print_key_value_args(name = 'Shaktiman', power = 'Laser')
# print_key_value_args(power = 'Learner', name = 'Satyam Jha')

#take any number of args

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}' , end = ' ')
    print('\n')

print_kwargs(name = 'Shaktiman', power = 'Laser')
print_kwargs(name = 'Shaktiman', power = 'Laser', enemy = 'Dr. Jackaal')
