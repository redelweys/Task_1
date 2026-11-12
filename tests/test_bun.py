import pytest

from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize('name', [
        'Краторная булка',
        'Флюоресцентная булка',
    ])
    def test_get_name_returns_bun_name(self, name):
        bun = Bun(name, 100)

        assert bun.get_name() == name

    @pytest.mark.parametrize('price', [0, 100, 125.5])
    def test_get_price_returns_bun_price(self, price):
        bun = Bun('Краторная булка', price)

        assert bun.get_price() == price