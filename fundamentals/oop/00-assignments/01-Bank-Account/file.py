
user=[
    {
        'first_name': 'Cole',
        'last_name': 'Winchester',
        'email': 'AnEmail@email.com',
        'age': '26'
    },
    {
        'first_name': 'Desmond',
        'last_name': 'Miles',
        'email': 'TheEmail@gmail.com',
        'age':'30'
    }
]

class User:
    def __init__(self, user_data):
        self.first_name=user_data['first_name']
        self.last_name=user_data['last_name']
        self.email=user_data['email']
        self.age=user_data['age']
        is_rewards_member=False
        gold_card_points=0

    def display_info(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        return self

    def enroll(self):
        pass

    def spend_points(self,amount):
        pass

User1=User(user[0])
User.display_info()