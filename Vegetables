import  random

class Food:

    def __init__(self,name):

        self.name = name

class Vegetables(Food):

    def veg(self):

        vl = ['artichoke','asparagus','beetroot','broccoli','leek','cabbage','lettuce','carrot',
              'cauliflower','celery','radish','aubergine','onion','garlic','kale','spinach']

        calories = [64, 17, 22, 3.5, 38, 17, 16, 16, 132, 6.8, 0.7, 198, 41, 4.5, 36, 41]

        protein = [3.5, 1.8, 0.8, 0.2, 1, 1, 1.2, 0.4, 11, 0.3, 0, 4.7, 1.3, 0.2, 2.5, 5.3]

        rv = random.choice(vl)

        cal = calories[vl.index(rv)]

        prot = protein[vl.index(rv)]

        return rv,cal,prot


class Legumes(Food):

    def lgm(self):

        lg = ['beans','lentils','red lentils','chickpeas','kidney beans','peas','green beans',
              'soy bean','edamame','fava beans']

        calories = [239, 230, 226, 269, 225, 134, 44, 296, 94, 94]

        protein = [12, 18, 18, 15, 15, 8.6, 2.4, 31, 9.2, 6.5]

        lv = random.choice(lg)

        cal = calories[lg.index(lv)]

        prot = protein[lg.index(lv)]
        
        return lv,cal,prot


v = Vegetables(name="vegetables").veg()

lg = Legumes(name="legumes").lgm()

vgp = f'{v[0]}, calories : {v[1]}, protein : {v[2]}'

lgp = f'{lg[0]}, calories : {lg[1]}, protein : {lg[2]}'

print(Vegetables(name="vegetables").name, vgp)

print(Legumes(name="legumes").name, lgp)
