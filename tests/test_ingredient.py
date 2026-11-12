import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_SAUCE,
    INGREDIENT_TYPE_FILLING,
)


class TestIngredient:

    @pytest.mark.parametrize('price', [0, 100, 125.5])
    def test_get_price_returns_ingredient_price(self, price):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус', price)

        assert ingredient.get_price() == price

    @pytest.mark.parametrize('name', [
        'Соус фирменный',
        'Мясо бессмертных моллюсков',
    ])
    def test_get_name_returns_ingredient_name(self, name):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, name, 100)

        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type', [
        INGREDIENT_TYPE_SAUCE,
        INGREDIENT_TYPE_FILLING,
    ])
    def test_get_type_returns_ingredient_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, 'Ингредиент', 100)

        assert ingredient.get_type() == ingredient_type