from db import inventoryDB
from app import app
from flask import request,json,jsonify
from model import Inventory,InventoryStatus
from flask_restful import fields,marshal_with,abort



inventory_fields = {
	'name': fields.String,
	'quantity_ordered': fields.Integer,
	'quantity_remaining': fields.Integer,
	'vendor_name': fields.String,
    'purchase_price':fields.Integer,
    'selling_price':fields.Integer
}
inventory_status_fields={
    'status':fields.Integer,
    'message':fields.String,
    'inventoryobject':fields.Nested(inventory_fields)
}

@app.route("/addInventoryDetails",methods=["POST"])
@marshal_with(inventory_status_fields)
def addInventory():
    output=InventoryStatus(1,"failed adding",None)
    try:
        inputparams=request.json
        print(inputparams)
        inventoryobject_foradding=Inventory(inputparams['name'],inputparams['quantity_ordered'],
                                  inputparams['quantity_remaining'],inputparams['vendor_name'],inputparams['purchase_price'],inputparams['selling_price'])
        output=inventoryDB.addItem(inventoryobject_foradding)
        if output.status==1:
            return output, 201
        else:
            return output, 404
    except (KeyError,TypeError) as input_error:
         output.message="invalid content"
         return output,404



@app.route("/getInventoryDetails",methods=["GET"])
@marshal_with(inventory_fields)
def getInventoryDetailsBasedonQuery():
        inputgot=request.json
        print(inputgot)
        if inputgot['name']:
             output=inventoryDB.find_inventory_for_a_category(inputgot['quantity_ordered'])
        elif inputgot['quantity_ordered']:
            output=inventoryDB.find_inventory_for_a_category(inputgot['quantity_ordered'])
        elif inputgot['quantity_remaining']:
            output=inventoryDB.find_inventory_for_a_category(inputgot['quantity_remaining'])
        elif inputgot['vendor_name']:
            output=inventoryDB.find_inventory_for_a_category(inputgot['vendor_name'])
        elif inputgot['purchase_price']:
            output=inventoryDB.find_inventory_for_a_category(inputgot['purchase_price'])
        elif inputgot['selling_price']:
            output=inventoryDB.find_inventory_for_a_category(inputgot['selling_price'])
        else:
             pass
        return output,200

@app.route("/updateInventoryDetails",methods=["PUT"])
@marshal_with(inventory_status_fields)
def updateInventory():
    print("for updating")
    inputparams=request.json
    print(inputparams)
    updatedobject=Inventory(inputparams['vendor_name'],inputparams['purchase_price'],
                                  inputparams['selling_price'])
    output=inventoryDB.updateInventory(updatedobject)
    if output.status==1:
        return output,200
    else:
        return output,404
#
#