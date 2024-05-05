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

# Create tables
python manage.py makemigrations
python manage.py migrate

# Create superuser (admin)
python3 manage.py createsuperuser
 
# Start the application (development mode)
python manage.py runserver # default port 8000

# Access the web app in browser: http://127.0.0.1:8000/ 
```

> Note: To use the app, use the credentials while creating superuser. After authentication, the app will unlock the private pages and you can access the Admin panel at `http:127.0.0.1:8000/admin/`
