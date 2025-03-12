from erpnext.selling.doctype.customer.customer import Customer

class CustomCustomer(Customer):
    @staticmethod
    def default_list_data():
        columns = [
            {
                "label": "Customer Name",
                "type": "Data",
                "key": "customer_name",
                "width": "17rem",
            },
            {
                "label": "Customer Group",
                "type": "Data",
                "key": "customer_group",
                "width": "17rem",
            },
            {
                "label": "Customer Type",
                "type": "Data",
                "key": "customer_type",
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
            "customer_name",
            "customer_group",
            "customer_type",
        ]
        return {"columns": columns, "rows": rows}