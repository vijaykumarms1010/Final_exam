
from app import db

class InventoryStatus:
    def __init__(self,status_code,message,inventoryobject):
        self.status=status_code
        self.message=message
        self.Inventoryobject=inventoryobject

class Inventory(db.Model):
    __tablename__= "inventory"
    name=db.Column("name",db.Integer)
    quantity_ordered=db.Column("quantity_ordered",db.Integer)
    quantity_remaining=db.Column("quantity_remaining",db.Integer)
    vendor_name=db.Column("vendor_name",db.String)
    purchase_price=db.column("purchase_price",db.Integer)
    selling_price=db.column("selling_price",db.Integer)

    def __init__(self,name,quantity_ordered,quantity_remaining,vendor_name,purchase_price,selling_price):
        self.quantity_ordered=quantity_ordered
        self.quantity_remaining=quantity_remaining
        self.vendor_name=vendor_name
        self.purchase_price=purchase_price
        self.selling_price=selling_price

    def __repr__(self):
        return f"{self.quantity_ordered} -- {self.quantity_remaining}  -- {self.vendor_name} --{self.purchase_price} -- {self.selling_price}"
