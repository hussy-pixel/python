class IRAQ:
    def capital(self):
        print("capital of IRAQ is BAGHDAD")

    def language(self):
        print("the language used in iraq is arabic")

    def type(self):
        print("it is a developed nation")

class INDIA:
    def capital(self):
        print("the capital of INDIA is NEW DELHI")

    def language(self):
        print("hindi is the most famous language spoken in INDIA")

    def type(self):
        print("INDIA is a developing nation")

obj_IRAQ=IRAQ()
obj_INDIA=INDIA()

for i in (obj_IRAQ, obj_INDIA):
    i.capital()
    i.language()
    i.type()

