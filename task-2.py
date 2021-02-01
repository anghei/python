class Road:

    _length = 0
    _width = 0
    weight = 0
    thick = 0

    def __init__(self, length, width, weight=25, thick=5):
        self._length = length
        self._width = width
        self.weight = weight
        self.thick = thick

    def calc_weight(self):
        return 'Масса асфальта равна ' + str(round(((self._length*self.weight*self._width*self.thick)/1000)))


a = Road(20, 5000)
b = a.calc_weight()
print(b)
