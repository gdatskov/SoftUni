class dictionary_iter:
    def __init__(self, dic):
        self.dic = dic
        self.keys = list(dic.items())
        self.current_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_idx == len(self.dic):
            raise StopIteration
        to_return = self.keys[self.current_idx]
        self.current_idx += 1
        return to_return


result = dictionary_iter({1: "aug_22", 2: "2"})
for x in result:
    print(x)
