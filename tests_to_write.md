
## Functional Tests for item_api.py
- Add Item: (included below in 'test_validate_crud')
    - Test Post by adding a new item, and validate response
    - Test Get for the newly created item
    - Test Update name and description for the newly created item and validate response
    - Test Delete the Updated  item 
    
    - (POST)Test adding a item with existing item id -- 500 server error(sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) 	UNIQUE constraint failed: item.item_id)
    - (GET)Test getting a non existing item id --  404
    - (DELETE)Test Deleting a nonexisting item id -- giving 200(##Bug##)

## Unit Tests for item_model.py
- Test creating a new Item for the model with fixture

 
 ###What are some of the things that code snippet is missing and how can it be improved?###

 Fixed Post and Put methods and now I am getting 200 (Updated Post request body with dictionary, and Put with request.json instead of request.form)
 Updated the methods with routes (__Used Flask Blueprint__)


 ## Results -- out of 7 tests(functional and unit), 2 functional tests failed.


##(venv_3.8.5) sujala@Sujalas-MBP Rady_SDET_Technical % pytest
```
(venv_3.8.5) sujala@Sujalas-MBP Rady_SDET_Technical % pytest
===================================== test session starts =====================================
platform darwin -- Python 3.8.5, pytest-6.1.1, py-1.9.0, pluggy-0.13.1
rootdir: /Users/sujala/Rady_SDET_Technical
collected 6 items                                                                             

tests/functional/test_item.py ..FF                                                      [ 66%]

tests/unit/test_item_model.py ..                                                        [100%]

========================================== FAILURES ===========================================

==================================== short test summary info ===================================
FAILED tests/functional/test_item.py::test_delete_non_existing_item_id - assert 200 == 404
FAILED tests/functional/test_item.py::test_get_non_existing_item_id - AttributeError: 'NoneT...
================================= 2 failed, 4 passed in 0.36s =================================
```
