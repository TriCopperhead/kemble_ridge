

# --- An srbitrary function ---
def some_function(value):

    # This uses an f-string to print values
    print(f'  we are in a function with {value}')


    
# --- Main function - starts the program ---    
if (__name__ == '__main__'):

    print('hello world')
    
    some_function('abcd')

    some_function(1234)

    print('goodbye world')
    

