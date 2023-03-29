from model import Inventory,InventoryStatus
from sqlalchemy.exc import IntegrityError
from app import db

class inventoryDB():
    def getinventoryDetails(self,inventory):
        Inventorystatus=InventoryStatus(0,"add failed",None)
        try:
            db.session.add(Inventory)
            db.session.commit()
            Inventorystatus.status=1
            Inventorystatus.message="added successfully"
            Inventorystatus.Inventoryobject=Inventory
        except IntegrityError:
            Inventorystatus.message="Integrity error"
            db.session.rollback()
        return Inventorystatus

    def updateinventory(self, inventory):
        Inventorystatus = InventoryStatus(0, "update failed", None)
        dbobject = Inventory.query.filter_by(name=Inventory.vendor_name).first()
        if dbobject is not None:
            dbobject.vendor_name=inventory.vendor_name
            dbobject.purchase_price=inventory.purchase_price
            dbobject.selling_price= inventory.selling_price
            db.session.commit()
            Inventorystatus.status = 1
            Inventorystatus.message = "updated successfully"
            Inventorystatus.Inventoryobject = inventory
        return Inventorystatus
