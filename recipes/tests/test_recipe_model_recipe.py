from django.core.exceptions import ValidationError
from parameterized import parameterized

from .test_recipe_base import RecipeTestBase


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    @parameterized.expand([ # Isso é um decorador que permite que você execute o mesmo teste com diferentes conjuntos de parâmetros.
            ('title', 65),
            ('description', 165),
            ('preparation_time_unit', 65),
            ('servings_unit', 65)
        ])
    def test_recipe_fields_max_length(self, field, max_length):
        #Isso é um teste que verifica se os campos do modelo Recipe respeitam o limite máximo de caracteres definido no models.py.
        setattr(self.recipe, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_string_representation(self):
        #Isso é um teste que verifica se a representação em string do modelo Recipe é igual ao título da receita.
        self.recipe.title = 'Test Recipe Title'
        self.recipe.full_clean()  # Valida o modelo antes de salvar
        self.recipe.save()
        self.assertEqual(str(self.recipe), 'Test Recipe Title')