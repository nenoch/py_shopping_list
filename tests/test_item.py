from src.item import Item

def test_has_price_attr():
    assert hasattr(Item, 'price') == True
