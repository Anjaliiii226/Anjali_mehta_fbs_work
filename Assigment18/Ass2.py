class Distance:
    def __init__(self, km=0, m=0, cm=0):
        self.km = km
        self.m = m
        self.cm = cm
        self.__normalize()
        print(f"Distance object created: {self}")

    def __del__(self):

        print(f"Distance object destroyed: {self}")

    def __normalize(self):

    
        if self.cm >= 100:
            self.m += self.cm // 100
            self.cm = self.cm % 100


        if self.m >= 1000:
            self.km += self.m // 1000
            self.m = self.m % 1000

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km + other.km,
                            self.m + other.m,
                            self.cm + other.cm)
        else:
            raise TypeError("Operand must be Distance")
    def __sub__(self, other):
        if isinstance(other, Distance):
            # Convert all to cm, subtract, then convert back
            total_cm1 = self.km*100000 + self.m*100 + self.cm
            total_cm2 = other.km*100000 + other.m*100 + other.cm
            diff = abs(total_cm1 - total_cm2)   # keep positive distance
            km = diff // 100000
            diff %= 100000
            m = diff // 100
            cm = diff % 100
            return Distance(km, m, cm)
        else:
            raise TypeError("Operand must be Distance")

    def __str__(self):
        return f"{self.km} km {self.m} m {self.cm} cm"
