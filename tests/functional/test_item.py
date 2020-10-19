from project import create_app
"""
This file (test_item_api.py) contains the functional tests for the `items` blueprint.

These tests use GETs and POSTs to different URLs to check for the proper behavior
of the `items` blueprint.
"""
def test_validate_crud(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/'  is posted to (POST)
    GET the  item and update the item and delete it.
    THEN check the response is valid
    """
    response = test_client.post('/',
                                json={'item_id':'1', 'item_name':'FlaskIsAwesome', 'item_description':"Flask-SQLAlchemy"},
                                follow_redirects=True)
    #Expected
    assert response.status_code == 200
    assert response.get_json()['status'] == "success" 

    #validate Get

    response = test_client.get('/1', follow_redirects=True)
    assert response.status_code == 200

    assert 'id' in response.get_json()['result']
    assert response.get_json()['result']['item_id'] == "1"
    assert response.get_json()['result']['item_name'] == "FlaskIsAwesome"
    assert response.get_json()['result']['item_description'] == "Flask-SQLAlchemy"

    #validate Put

    response = test_client.put('/1', json={'item_name':'FlaskIsSuper', 'item_description':"Flask-SQLAlchemy-extension"}, 
                                            follow_redirects=True)
    assert response.status_code == 200

    assert 'id' in response.get_json()['result']
    assert response.get_json()['result']['item_id'] == "1"
    assert response.get_json()['result']['item_name'] == "FlaskIsSuper"
    assert response.get_json()['result']['item_description'] == "Flask-SQLAlchemy-extension"

    #Delete
    response = test_client.delete('/1', follow_redirects=True)
    assert response.status_code == 200

def test_post_with_item_id_big_alphanumericstring(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/'  is posted to (GET)
    THEN check the response is valid 
    """
    response = test_client.post('/',
                                json={'item_id':'Flask#$%^&199080980909-', 'item_name':'FlaskIsSuper','item_description':"Flask-SQLAlchemy"},
                                follow_redirects=True)
    #Expected
    assert response.status_code == 200

def test_delete_non_existing_item_id(test_client, init_database):
    ##### BUG##### This test will fail
    """
    GIVEN a Flask application configured for testing
    WHEN the '/'  is posted to (DELETE)
    THEN check the response is valid 
    """
    response = test_client.delete('/67', follow_redirects=True)
    #Expected 404 , Actual 200
    assert response.status_code == 404

def test_get_non_existing_item_id(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/'  is posted to (GET)
    THEN check the response is valid 
    """
    response = test_client.get('/Nonexistingid',
                                follow_redirects=True)
    #Expected 404 
    assert response.status_code == 404
