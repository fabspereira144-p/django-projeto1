from unittest import skip

from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeHomeViewTests(RecipeTestBase):
    def test_recipe_home_view_function_is_correct(self):
        #Checa se a função de view correta é chamada para a URL da home
        view = resolve(reverse('recipes-home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_ok(self):
        #Checa se a view da home retorna status code 200
        response = self.client.get(reverse('recipes-home'))
        self.assertEqual(response.status_code, 200)
    
    def test_recipe_home_view_loads_correct_template(self):
        #Checa se a view da home carrega o template correto
        response = self.client.get(reverse('recipes-home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    @skip('Teste de template não implementado')
    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        #Checa se a view da home mostra a mensagem "No recipes found" caso não haja receitas cadastradas
        response = self.client.get(reverse('recipes-home'))
        self.assertIn('Receitas não encontradas', response.content.decode('utf-8'))

    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe(category_data = {
            'name': 'Category Test'
        }, author_data = {
            'first_name': 'user',
        })

        response = self.client.get(reverse('recipes-home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']

        #Checa se o conteúdo da página contém o título da receita, nome da categoria e nome do autor passados como parâmetro na função make_recipe
        self.assertIn('Recipe Title', content)
        self.assertIn('Category Test', content)
        self.assertIn('user', content)
        self.assertEqual(len(response_context_recipes), 1)

    def test_recipe_home_template_dont_load_recipes_not_published(self):
        #Checa se a view da home não carrega receitas que não estão publicadas
        self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes-home'))
        content = response.content.decode('utf-8')

        self.assertIn('Receitas não encontradas', content)
    
    def test_recipe_home_paginates_recipes_correctly(self):
        for i in range(10):
            self.make_recipe(
                title=f'Reciple Title{i}',
                slug=f'recipe-slug-{i}',
                category_data={
                    'name': f'Category{i}'
                },
                author_data={
                    'username': f'user{i}',
                    'email': f'user{i}@email.com'
                },
            )

        response = self.client.get(reverse('recipes-home'))
        recipes = response.context['recipes']

        self.assertEqual(len(recipes), 9)

        # Segunda página
        response = self.client.get(
            reverse('recipes-home') + '?page=2'
        )
        recipes = response.context['recipes']

        self.assertEqual(len(recipes), 1)