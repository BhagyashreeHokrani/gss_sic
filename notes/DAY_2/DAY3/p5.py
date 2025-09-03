def my_range (*var_args):
    if len(var_args)< 1 or len(var_args) > 3 :
        print("Type error")
        return
    if len(var_args)==1 :
          