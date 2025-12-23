# admin_panel.py

from flask_admin import Admin
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.menu import MenuLink
from flask import request
from werkzeug.utils import secure_filename
import os
from app import app

# Ensure the upload directory exists
upload_dir = os.path.join(os.path.dirname(__file__), '..', 'uploads')
upload_dir = os.path.normpath(upload_dir)
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir, exist_ok=True)


class CustomFileAdmin(FileAdmin):
    def is_accessible(self):
        return True

    def is_visible(self):
        return True


admin = Admin(app, name='Fraud Bot Admin', template_mode='bootstrap3')

# Add links to the admin menu that point to the blueprint endpoints
admin.add_link(MenuLink(name='Upload Card Details', endpoint='admin.upload_cards'))
admin.add_link(MenuLink(name='Start Bot', endpoint='admin.start_bot'))

# Register a file manager view for the uploads directory
admin.add_view(CustomFileAdmin(upload_dir, '/admin/files/', name='File Manager'))

