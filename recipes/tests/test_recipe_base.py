from django.test import TestCase

from recipes.models import Category, Recipe, User


class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        category = Category.objects.create(name='Category Test')
        user = User.objects.create_user(
            first_name='user', 
            last_name='test', 
            username='user', 
            password='123456',
            email='username@email.com',
            )
        recipe = Recipe.objects.create(  # noqa: F841
            category=category,
            author=user,
            title='Recipe Title',
            description='Recipe Description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_steps='Recipe Preparation Steps',
            preparation_steps_is_html=False,
            created_at='2023-01-01 00:00:00',
            updated_at='2023-01-01 00:00:00',
            is_published=True,
            cover='recipes/covers/2023/01/01/test.jpg'
        )
        return super().setUp()