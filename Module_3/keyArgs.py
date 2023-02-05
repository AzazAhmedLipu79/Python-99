
def all_types (first, *args, **kargs):
    print(first)
    for word in args:
        print(word)
    print(kargs)
    for key, value in kargs.items(): # kargs.items() for kargs
        print(key, value)


all_types('abd', 'ddd', 'kjk', 'lll', 'pp', name='Abul', father='babul')


""" 
default values -> *args 
values with key -? **key_args

 """