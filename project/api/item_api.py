from project.item_model import Item, db
from flask import request, jsonify
from project.api import api_blueprint 

@api_blueprint.route('/', methods=['POST'])
def post():

	"""
	Creates an item.
	"""		
	if request.method == 'POST' :
	# Retrieve the payload
		item_id = request.json.get('item_id')
		item_name = request.json.get('item_name')
		item_description = request.json.get('item_description')

		kwargs = {"item_id": item_id, "item_name": item_name, "item_description": item_description}

		new_item = Item(**kwargs)

		# Add the new Item model object and commit.
		db.create_all()
		db.session.add(new_item)
		db.session.commit()

		# Return the response with status and result.
		return jsonify({"status": "success"})

@api_blueprint.route('/<string:item_id>/', methods=['GET'])
def get(item_id):
	"""
	Retrieves an item.
	"""
	if request.method == 'GET' :
		# Queries the Item table and filter by item_id provided from the API.
		query_item = Item.query.filter(Item.item_id == item_id).first()
		# Create a dictionary structure to include it in response.
		result = {"id": query_item.id,
		"item_id": query_item.item_id,
		"item_name": query_item.item_name,
		"item_description": query_item.item_description}
		# Return the response with status and result.
		return jsonify({"status": "success", "result": result})

@api_blueprint.route("/<string:item_id>", methods=['PUT'])
def put(item_id):
	"""
	Updates an item.
	"""
	if request.method == 'PUT' :
		# Receives item_name and item_description from form.
		item_name = request.json.get('item_name')
		item_description = request.json.get('item_description')
		# Queries the Item table and filter by item_id provided from the API.
		query_item = Item.query.filter(Item.item_id == item_id).first()
		# Updates the query_item object with new value.
		query_item.item_name = item_name
		query_item.item_description = item_description
		# Saving the changes to the database.
		db.session.commit()

		# Create a dictionary structure to include it in response with updated
		# values.
		result = {	"id": query_item.id,
 				"item_id": query_item.item_id,
				"item_name": query_item.item_name,
 				"item_description": query_item.item_description}


 	# Return the response with status and result.
	return jsonify({"status": "sucesss", "result": result})

@api_blueprint.route("/<string:item_id>", methods=['DELETE'])
def delete(item_id):
	# Queries the Item table and filter by item_id provided from the API.
	query_item = Item.query.filter(Item.item_id == item_id).first()
	# Check whether query_item is not None (meaning the record exists in Item
	# table), then delete and commit.
	if query_item:
		db.session.delete(query_item)
		db.session.commit()

	# Return the response with status and result.
	return jsonify({"status": "sucesss"})
