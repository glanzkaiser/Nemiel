import random
import sys
from faker import Faker
from basic_table import db, User


def create_fake_users(n):
    """Generate fake stocks."""
    faker = Faker()
    for i in range(n):
        user = User(name=faker.company(),
                    founded=random.randint(1920, 2020),
                    business=faker.catch_phrase(),
                    revenue=random.randint(10, 999),
                    netincome=random.randint(1, 999),
                    equity=random.randint(1, 999),
                    debts=random.randint(10, 999),
                    bookvalue=random.randint(10, 9999))
        db.session.add(user)
    db.session.commit()
    print(f'Added {n} fake stocks to the database.')


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Pass the number of stocks you want to create as an argument.')
        sys.exit(1)
    create_fake_users(int(sys.argv[1]))
