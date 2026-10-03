from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views


class RecipeViewsTests(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes-home'))
        self.assertIs(view.func, views.home)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes-recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipes)

    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes-home'))
        self.assertEqual(response.status_code, 200)