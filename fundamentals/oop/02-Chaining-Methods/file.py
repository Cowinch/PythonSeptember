

from operator import truediv


class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.age=age
        self.is_rewards_member=False
        self.gold_card_points=0

    def display_info(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        if self.is_rewards_member!=True:
            print("Rewards Member: No")
            print("Gold Card Points: NA")
        else:
            print("Rewards Member: Yes")
            print(f"Gold Card Points: {self.gold_card_points}")
        print('')
        return self

    def enroll(self):
        if self.is_rewards_member==False:
            self.is_rewards_member=True
            self.gold_card_points+=200
        else:
            print("Already a rewards member")
            print('')
        return self

    def spend_points(self,amount):
        if self.gold_card_points>=amount:
            self.gold_card_points=self.gold_card_points-amount
            print(f"You this many Gold Card Points left: {self.gold_card_points}")
            print('')
        else:
            print("Insufficient funds")
            print('')
        return self

user1=User('Cole', 'Winchester', 'AnEmail@email.com', '26')
user2=User('Desmond', 'Miles', 'TheEmail@gmail.com', '31')
user3=User('Bob', 'Terry', 'bobsemail@gmail.com', '45')

# user1.display_info()
# user1.enroll()
# user1.display_info()



user2.enroll().spend_points(175).display_info()
user2.spend_points(500).enroll()
