"""
This file (test_item_model.py) contains the unit tests for the models.py file.
"""
from project.item_model import Item


def test_new_item():
    """
    GIVEN a Item model
    WHEN a new Item is created
    THEN check the fields are defined correctly
    """
    data = {'item_id':'item_id1', 'item_name':'item_name1', 'item_description':'item_description1'}
    item = Item(**data)
    print(item)
    assert item.item_id == 'item_id1'
    assert item.item_name == 'item_name1'
    assert item.item_description== 'item_description1'


def test_new_item_with_fixture(new_item):
    """
    GIVEN a Item model
    WHEN a new Item is created
    THEN check the fields are defined correctly
    """
    assert new_item.item_id == 'item_id1'
    assert new_item.item_name == 'item_name1'
    assert new_item.item_description== 'item_description1'
