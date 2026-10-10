from .test_recipe_base import RecipeTestBase


class RecipeCategoryTest(RecipeTestBase):
    def setUp(self) -> None:
        self.category = self.make_category()
        return super().setUp()

    def test_recipe_category_string_representation(self):
        self.category.name = 'Test Category Name'
        self.category.full_clean()
        self.category.save()
        self.assertEqual(str(self.category), self.category.name)