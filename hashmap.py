

class HashMap():
    def __init__(self):
        self.array=[]

    def get(self, key):
        for key_value in self.array:
            if key_value[0]==key:
                return key_value[1]

    def put(self, key, value):
        for key_value in self.array:
            if key_value[0]==key:
                key_value[1]=value
        self.array.append([key, value])



class OptimizedHashMap():
    def __init__(self, size=16):
        self.array=[None for _ in range(size)]

    def get(self, key):
        index = hash(key) & 15
        sub_array=self.array[index]
        if sub_array is None:
            return None
        for key_value in sub_array:
            if key_value[0]==key:
                return key_value[1]

    def put(self, key, value):
        index = hash(key) & 15
        sub_array=self.array[index]
        if sub_array is None:
            self.array[index]=[[key, value]]
            return
        found=False
        for key_value in sub_array:
            if key_value[0]==key:
                found=True
                key_value[1]=value
        if not found:
            self.array[index].append([key, value])




class DoubleArrayHashMap():
    def __init__(self):
        self.keys=[]
        self.values=[]

    def __get_index(self, key):
        for i in range(len(self.keys)):
            if self.keys[i]==key:
                return i


    def get(self, key):
        index=self.__get_index(key)
        if index is not None:
            return self.values[index]


    def put(self, key, value):
        index=self.__get_index(key)
        if index is not None:
            self.values[index]=value
        else:
            self.keys.append(key)
            self.values.append(value)


# print(hash('a'))
# print(hash('a') & 15)
