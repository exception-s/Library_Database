from faker import Faker
import random

fake = Faker()


def generate_users(num_users=100):
    users = []
    for _ in range(num_users):
        user = {
            'name': fake.name(),
            'email': fake.email()
        }
        users.append(user)
    return users


users_data = generate_users()
for user in users_data:
    print(user)
