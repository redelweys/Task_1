from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient

from praktikum.ingredient_types import (
    INGREDIENT_TYPE_SAUCE,
    INGREDIENT_TYPE_FILLING,
)

import pytest

class TestBurger:

    def test_init_creates_burger_without_bun_and_ingredients(self):
        burger = Burger()

        assert burger.bun is None and burger.ingredients == []

    def test_set_buns_sets_selected_bun(self):
        burger = Burger()
        bun = Mock(spec=Bun)

        burger.set_buns(bun)

        assert burger.bun is bun

    def test_add_ingredient_adds_ingredient_to_list(self):
        burger = Burger()
        ingredient = Mock(spec=Ingredient)

        burger.add_ingredient(ingredient)

        assert burger.ingredients == [ingredient]

    @pytest.mark.parametrize('index', [0, 1, 2])
    def test_remove_ingredient_removes_selected_ingredient(self, index):
        burger = Burger()
        ingredients = [Mock(spec=Ingredient) for _ in range(3)]
        burger.ingredients = ingredients.copy()
        expected_ingredients = ingredients[:index] + ingredients[index + 1:]

        burger.remove_ingredient(index)

        assert burger.ingredients == expected_ingredients

    @pytest.mark.parametrize('index, new_index, expected_order', [
        (0, 2, [1, 2, 0]),
        (2, 0, [2, 0, 1]),
        (1, 1, [0, 1, 2]),
    ])
    def test_move_ingredient_changes_ingredient_position(
        self, index, new_index, expected_order
    ):
        burger = Burger()
        ingredients = [Mock(spec=Ingredient) for _ in range(3)]
        burger.ingredients = ingredients.copy()
        expected_ingredients = [ingredients[i] for i in expected_order]

        burger.move_ingredient(index, new_index)

        assert burger.ingredients == expected_ingredients

    @pytest.mark.parametrize('bun_price, ingredient_prices, expected_price', [
        (100, [], 200),
        (100, [50], 250),
        (100, [50, 25.5], 275.5),
        (0, [50], 50),
        (100, [0], 200),
    ])
        
    def test_get_price_returns_total_price(
        self, bun_price, ingredient_prices, expected_price
    ):
        burger = Burger()
        bun = Mock(spec=Bun)
        bun.get_price.return_value = bun_price
        burger.bun = bun

        for price in ingredient_prices:
            ingredient = Mock(spec=Ingredient)
            ingredient.get_price.return_value = price
            burger.ingredients.append(ingredient)

        assert burger.get_price() == expected_price

    def test_get_receipt_returns_formatted_receipt(self):
        burger = Burger()

        bun = Mock(spec=Bun)
        bun.get_name.return_value = 'Краторная булка'
        burger.bun = bun

        sauce = Mock(spec=Ingredient)
        sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        sauce.get_name.return_value = 'Соус фирменный'

        filling = Mock(spec=Ingredient)
        filling.get_type.return_value = INGREDIENT_TYPE_FILLING
        filling.get_name.return_value = 'Мясо моллюсков'

        burger.ingredients = [sauce, filling]
        burger.get_price = Mock(return_value=350)

        expected_receipt = (
            '(==== Краторная булка ====)\n'
            '= sauce Соус фирменный =\n'
            '= filling Мясо моллюсков =\n'
            '(==== Краторная булка ====)\n'
            '\n'
            'Price: 350'
        )

        assert burger.get_receipt() == expected_receipt