

import pytest

from src.item import Item


@pytest.fixture
def test_item():
    retirn Item('One', 2, 3)


