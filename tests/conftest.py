import pytest
from project import create_app, db
from project.item_model import Item


@pytest.fixture(scope='module')
def new_item():
    data = {'item_id':'item_id1', 'item_name':'item_name1', 'item_description':'item_description1'}
    item = Item(**data)
    return item


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('flask_test.cfg')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!


@pytest.fixture(scope='module')
def init_database(test_client):
    # Create the database and the database table
    db.create_all()

    # Insert item data
    item1 = Item(item_id='item_id1', item_name='FlaskIsAwesome', item_description='hgjgbk')
    item2 = Item(item_id='item_id2', item_name='FlaskIsAwesome2', item_description='hgjgbk2')
    db.session.add(item1)
    db.session.add(item2)

    # Commit the changes for the items
    db.session.commit()

    yield  # this is where the testing happens!

    db.drop_all()
