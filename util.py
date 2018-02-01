def get_file(argv, default):
    result = default
    for x in argv:
        if x.startswith("./"):
            result = x
            break
    
    return ([x for x in argv if x != result and x != "-exp"], result)