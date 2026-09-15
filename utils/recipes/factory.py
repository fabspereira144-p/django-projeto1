from random import choice, randint

from faker import Faker

fake = Faker('pt_BR')


FOOD_IMAGES = [
    'https://images.unsplash.com/photo-1546069901-ba9599a7e63c',
    'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38',
    'https://images.unsplash.com/photo-1551183053-bf91a1d81141',
    'https://images.unsplash.com/photo-1565958011703-44f9829ba187',
    'https://images.unsplash.com/photo-1540189549336-e6e99c3679fe',
    'https://images.unsplash.com/photo-1512621776951-a57141f2eefd',
    'https://images.unsplash.com/photo-1563379926898-05f4575a45d8',
    'https://images.unsplash.com/photo-1504674900247-0877df9cc836',
]


def rand_ratio():
    return randint(840, 900), randint(473, 573)


def get_random_food_image():
    image = choice(FOOD_IMAGES)
    width, height = rand_ratio()

    return f'{image}?auto=format&fit=crop&w={width}&h={height}'


def make_recipe():
    return {
        'id': fake.random_number(digits=2, fix_len=True),
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=12),
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutos',
        'servings': fake.random_number(digits=2, fix_len=True),
        'servings_unit': 'Porções',
        'preparation_steps': fake.text(3000),
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': fake.word()
        },
        'cover': {
            'url': get_random_food_image(),
        }
    }


if __name__ == '__main__':
    from pprint import pprint

    pprint(make_recipe())