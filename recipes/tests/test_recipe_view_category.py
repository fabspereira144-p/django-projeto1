from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeCategoryViewTests(RecipeTestBase):
    def test_recipe_category_view_function_is_correct(self):
        #Checa se a função de view correta é chamada para a URL da categoria
        view = resolve(reverse('category', kwargs={'category_id': 1000}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        #Checa se a view da categoria retorna status code 404 caso não haja receitas na categoria
        response = self.client.get(reverse('category', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_loads_recipes(self):
        #Checa se a view da categoria carrega as receitas corretamente
        title = 'This is a category test'
        self.make_recipe(title=title)

        response = self.client.get(reverse('category', kwargs={'category_id': 1}))
        content = response.content.decode('utf-8')

        self.assertIn(title, content)
    
    def test_recipe_category_template_dont_load_recipes_not_published(self):
        #Checa se a view da categoria não carrega receitas que não estão publicadas
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(reverse('category', kwargs={'category_id': recipe.category.id}))

        self.assertEqual(response.status_code, 404)