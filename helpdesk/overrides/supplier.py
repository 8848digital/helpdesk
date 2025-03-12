from erpnext.buying.doctype.supplier.supplier import Supplier

#Added Supplier Side Bar
class CustomSupplier(Supplier):
    @staticmethod
    def default_list_data():
        columns = [
            {
                "label": "Supplier Name",
                "type": "Data",
                "key": "supplier_name",
                "width": "17rem",
            },
            {
                "label": "Supplier Group",
                "type": "Data",
                "key": "supplier_group",
                "width": "17rem",
            },
            {
                "label": "Supplier Type",
                "type": "Data",
                "key": "supplier_type",
                "width": "17rem",
            },
            {
                "label": "Created On",
                "type": "Datetime",
                "key": "creation",
                "width": "17rem",
            },
        ]
        rows = [
            "name",
            "supplier_name",
            "supplier_group",
            "supplier_type",
        ]
        return {"columns": columns, "rows": rows}