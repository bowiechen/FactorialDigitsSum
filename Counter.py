class Counter:
    digits = []
    count = 0
    overflow = False
    def __init__(self, count, initial_value=0, zeros=True):
        self.count = count
        if initial_value != 0:
            self.digits = list(str(initial_value))
            for counter, value in enumerate(self.digits):
                self.digits[counter] = int(value)

            self.digits.reverse()
            while len(self.digits) < count:
                self.digits.append(0)
            self.digits.reverse()
        else:
            for i in range(count):
                if zeros:
                    self.digits.append(0)
                else:
                    self.digits.append(1)

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

