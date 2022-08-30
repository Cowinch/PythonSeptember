#OOP
#Objects - things, tiems, they can do things, they have properties / attributes that describe
# emphasizez grouping data and functionality together in entities known as objects

cat = [
    {'name': 'Scar',
    'color': 'dark brown',
    'age':3,
    'breed':'lion',},
    {'name': 'Garfield',
    'color': 'orange/striped',
    'age':30,
    'breed':'lasanga'}
]
class Cat():
    all_cats=[]
    def __init__(self, cat_data):
        self.name = cat_data['name']
        self.color = cat_data['color']
        self.age=cat_data['age']
        self.breed=cat_data['breed']
        Cat.all_cats.append(self)

    def print_info(self):
        print(f"Name: {self.name}  Color: {self.color}  Age: {self.age}  Breed: {self.breed}")
        return self
    def meow(self):
        print(F"{self.name} lets out a cry!")
        return self

cat1=Cat(cat[0])
cat2=Cat(cat[1])

# print(cat1.name)
# print(cat1.color)

cat1.print_info().meow()