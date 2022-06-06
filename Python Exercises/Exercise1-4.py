class Arguments:
   
    def print_func(self, para1, para2, a=0, b=0, *args, **kwargs):
        print(f'paramaters received are {para1} and {para2}')
        print(f'positional args are {a} and {b}')
        print(f'args are {[*args]}')
        print(f'kwargs are {kwargs}')

obj = Arguments()
obj.print_func(1,2, 4, 5, "a", "c", 45, m ="d", l=5)