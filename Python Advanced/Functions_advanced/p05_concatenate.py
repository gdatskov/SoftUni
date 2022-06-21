def concatenate(*args, **kwargs):
    arg_text = "".join(args)
    for k, v in kwargs.items():
        if k in arg_text:
            arg_text = arg_text.replace(k, v)
    return arg_text


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))

print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
