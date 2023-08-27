class Vector():
    def __init__(self,data):
        self._data=data
    
    def __str__(self):
        return f'The values are {self._data}'
    
    def __len__(self):
        return len(self._data)

v = Vector([1,2])
len(v)