

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

# print(hash('a'))
# print(hash('a') & 15)
