#OOP
#Objects - things, tiems, they can do things, they have properties / attributes that describe
# emphasizez grouping data and functionality together in entities known as objects

#instance method -- accesses or alters the actual object
#class method -- accesses or alters on the class level
#static method -- somehow related to the class but doesnt access or alter the class or an instance

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
    def __init__(self, cat_data, fav_toy_type, fav_toy_color, fav_toy_action):
        self.name = cat_data['name']
        self.color = cat_data['color']
        self.age=cat_data['age']
        self.breed=cat_data['breed']
        self.fav_toy=Toy(fav_toy_type, fav_toy_color, fav_toy_action)
        Cat.all_cats.append(self)

    def __repr__(self):
        return f"name: {self.name}  Color: {self.color}  age: {self.age}  breed: {self.breed}"

    def print_info(self):
        print(f"Name: {self.name}  Color: {self.color}  Age: {self.age}  Breed: {self.breed}")
        print(f"My favorite toy is a {self.fav_toy.color} {self.fav_toy.type}")
        return self

    def meow(self):
        print(f"{self.name} lets out a cry!")
        return self
    
    def play(self):
        print(f"{self.name} plays with their {self.fav_toy.color} {self.fav_toy.type} and it {self.fav_toy.action}")
    
    @classmethod
    def print_all_cats(cls):
        for cat in cls.all_cats:
            cat.print_info()
            
    @staticmethod
    def convert_to_cat_years(years):
        return years * 7
    
class Toy():
    def __init__(self, type, color, action):
        self.type=type
        self.color=color
        self.action=action

ball=Toy('ball','red','bounes on the floor')
yarn=Toy('yarn','blue','rolls away')

cat1=Cat(cat[0], 'ball','red','bounces on the floor')
cat2=Cat(cat[1], 'yarn', 'blue', 'rolls away')

cat1.fav_toy=ball
print(cat1.fav_toy)

# print(cat1.name)
# print(cat1.color)

cat1.play()
cat2.play()
# cat1.print_info().meow()
Cat.print_all_cats()

age=20
cat_years=cat1.convert_to_cat_years(age)