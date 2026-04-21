import random

class ExecTrace:
    def __init__(self, arg):
        self.arg = arg
    def __call__ (self, *args, **kwargs):
        print(args)
        print(kwargs)
        return self.arg(args, kwargs)

    

@ExecTrace
def generate_random(val, another_val = 5):
    return random.random()
    
generate_random(1, another_val = 5)
generate_random()
generate_random()
print(generate_random())

