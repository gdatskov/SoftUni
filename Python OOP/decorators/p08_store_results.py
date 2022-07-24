class store_results:
    _logfile = "./store_results.txt"

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        log_string = f"Function '{self.func.__name__}' was called." \
                     f"Result: {self.func(*args, **kwargs)}"
        with open(self._logfile, "a") as file:
            file.write(log_string + "\n")
        return self.func(*args, **kwargs)


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
