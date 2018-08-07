class Counter:
    digits = []
    count = 0
    overflow = False
    def __init__(self, count):
        self.count = count
        for i in range(count):
            self.digits.append(0)

    def increment(self):
        self.digits[len(self.digits)-1] += 1
        for i in range(self.count-1, -1, -1):
            if self.digits[i] > 9:
                if i == 0:
                    self.overflow = True
                self.digits[i] = 0
                
                if i-1 >= 0:
                    self.digits[i-1] += 1

    def get_value(self):
        retval = ''
        for i in self.digits:
            retval += str(i)
        return int(retval)

    def get_list(self):
        return self.digits

