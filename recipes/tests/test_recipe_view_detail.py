from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeDetailViewTests(RecipeTestBase):
    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes-recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipes)

    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes-recipe', kwargs={'id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_loads_correct_recipe(self):
        #Checa se a view da receita carrega a receita corretamente
        title = 'This is a detail test'
        self.make_recipe(title=title)

        response = self.client.get(reverse('recipes-recipe', kwargs={'id': 1}))
        content = response.content.decode('utf-8')

        self.assertIn(title, content)

    def test_recipe_detail_template_dont_load_recipes_not_published(self):
        #Checa se a view da receita não carrega receitas que não estão publicadas
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes-recipe', kwargs={'id': recipe.id}))

        self.assertEqual(response.status_code, 404)