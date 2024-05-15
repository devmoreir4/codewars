def likes(names):
    num_names = len(names)
    
    if num_names == 0:
        return "no one likes this"
    elif num_names == 1:
        return "{} likes this".format(names[0])
    elif num_names == 2:
        return "{} and {} like this".format(names[0], names[1])
    elif num_names == 3:
        return "{}, {} and {} like this".format(names[0], names[1], names[2])
    else:
        return "{}, {} and {} others like this".format(names[0], names[1], num_names - 2)