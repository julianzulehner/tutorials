class MyList(list):

    def __init__(self):
        super().__init__(self)

class MyDict(dict):

    def __init__(self):
        super().__init__(self)

    def __getattr__(self, name:str):
        return self[name]
    
    def __setattr__(self, name:str, value):
        self[name] = value

if __name__ == "__main__":
    my_list = MyList()
    my_dict = MyDict()
    my_dict.test = 3
    print(my_dict)

