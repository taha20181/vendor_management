# Vendor Management

<br />

## How to use it

```bash
# Get the code
git clone https://github.com/taha20181/vendor_management.git
cd vendor_management

# Virtualenv modules installation (Unix based systems)
python3 -m venv myvenv
source venv/bin/activate

# Install python modules
pip3 install -r requirements.txt

# run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (admin)
python3 manage.py createsuperuser
 
# Start the application
python manage.py runserver # default port 8000

# Access the web app in browser: http://127.0.0.1:8000/

# Create auth token for API authentication

python manage.py shell

from django.contrib.auth.models import
from rest_framework.authtoken.models import Token

user = User.objects.get(username='username')
token = Token.objects.create(user=user)

# Use this token in the request header 
Authorization : Token {token}

```

## API Endpoints

---

## Vendor Endpoints

### Get All Vendors
- **URL:** `/vendors/`
- **Method:** GET
- **Description:** Retrieves a list of all vendors.
- **Parameters:** None
- **Returns:**
  - List of vendor objects.

### Create a Vendor
- **URL:** `/vendors/`
- **Method:** POST
- **Description:** Creates a vendor.
- **Parameters:** None
- **Returns:**
  - Created vendor object.
- **Payload:**
    ```json
    {
		"name": "Vendor X",
		"contact_details": "9999999990, vendorx@email.com",
		"address": "Plot ABC, \nOpp. XYZ Street",
		"vendor_code": "VNDRX"
    }
    ```

### Get Vendor by ID
- **URL:** `/vendors/<vendor_id>/`
- **Method:** GET
- **Description:** Retrieves details of a specific vendor by ID.
- **Parameters:**
  - `vendor_id`: Integer (required) - ID of the vendor.
- **Returns:**
  - Vendor object.

### Update a Vendor
- **URL:** `/vendors/<vendor_id>/`
- **Method:** PUT
- **Description:** Updates a vendor.
- **Parameters:** None
- **Returns:**
  - Vendor object with changes.
- **Payload:**
  ```json
    {
            "name": "Vendor X",
            "contact_details": "9999999990, vendorx@email.com",
            "address": "Plot ABC, \nOpp. XYZ Street",
            "vendor_code": "VNDRX"
    }
    ```

### Delete Vendor
- **URL:** `/vendors/<vendor_id>/`
- **Method:** DELETE
- **Description:** Deletes a vendor.
- **Parameters:**
  - `vendor_id`: Integer (required) - ID of the vendor.


### Get Vendor Performance
- **URL:** `/vendors/<vendor_id>/performance`
- **Method:** GET
- **Description:** Retrieves performance metrics of a specific vendor by ID.
- **Parameters:**
  - `vendor_id`: Integer (required) - ID of the vendor.
- **Returns:**
  - Performance metrics for the vendor.


## Purchase Order Endpoints

### Get All Purchase Orders
- **URL:** `/purchase_orders/`
- **Method:** GET
- **Description:** Retrieves a list of all purchase orders.
- **Parameters:** None
- **Returns:**
  - List of purchase order objects.

### Create a Purchase Order
- **URL:** `/purchase_orders/`
- **Method:** POST
- **Description:** Creates a purchase order.
- **Parameters:** None
- **Returns:**
  - Created purchase order object.
- **Payload:**
  ```json
    {
            "po_number": "PO101",
            "vendor": 1,
            "expected_delivery_date": "2024-05-07T06:00:00Z",
            "items": ["item1", "item3"],
            "quantity": 2
    }
    ```

### Update a Purchase Order Details
- **URL:** `/purchase_orders/<po_id>/`
- **Method:** PUT
- **Description:** Creates a purchase order.
- **Parameters:** None
- **Returns:**
  - Created purchase order object.
- **Payload:**
  ```json
    {
            "id": 2,
            "po_number": "PO101",
            "vendor": 1,
            "order_date": "2024-05-05T11:13:14.769880Z",
            "expected_delivery_date": "2024-05-07T06:00:00Z",
            "items": [
                "item1",
                "item3"
            ],
            "quantity": 2,
            "status": "COMPLETED",
            "quality_rating": 4.2,
            "issue_date": "2024-05-05T11:13:14.769938Z"
    }
    ```

### Get Purchase Order by ID
- **URL:** `/purchase_orders/<po_id>/`
- **Method:** GET
- **Description:** Retrieves details of a specific purchase order by ID.
- **Parameters:**
  - `po_id`: Integer (required) - ID of the purchase order.
- **Returns:**
  - Purchase order object.

### Delete Purchase Order
- **URL:** `/purchase_orders/<po_id>/`
- **Method:** DELETE
- **Description:** Deletes a PO.
- **Parameters:**
  - `po_id`: Integer (required) - ID of the PO.

### Acknowledge Purchase Order
- **URL:** `/purchase_orders/<po_id>/acknowledge`
- **Method:** POST
- **Description:** Acknowledges a specific purchase order by ID.
- **Parameters:**
  - `po_id`: Integer (required) - ID of the purchase order.



> Note: To use the app, use the credentials while creating superuser. After authentication, the app will unlock the private pages and you can access the Admin panel at `http:127.0.0.1:8000/admin/`
