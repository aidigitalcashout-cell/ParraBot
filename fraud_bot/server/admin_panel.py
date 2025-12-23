# admin_panel.py

from flask_admin import Admin
from flask_admin.form import SecureForm
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.menu import MenuLink
from flask import redirect, url_for, request, jsonify
from werkzeug.utils import secure_filename
import os
from routes import admin_routes
from app import app
from card_manager import upload_card_details
from purchase_automation import automate_purchase

# Ensure the upload directory exists
upload_dir = 'uploads'
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)

    class CustomFileAdmin(FileAdmin):
        def is_accessible(self):
                return True

                    def is_visible(self):
                            return True

                                def handle_file_upload(self, file):
                                        filename = secure_filename(file.filename)
                                                file_path = os.path.join(upload_dir, filename)
                                                        file.save(file_path)
                                                                return filename

                                                                admin = Admin(app, name='Fraud Bot Admin', template_mode='bootstrap3')

                                                                # Add a custom link to the admin menu for file upload
                                                                admin.add_link(MenuLink(name='Upload Card Details', endpoint='admin.upload_cards'))

                                                                # Add a custom link to the admin menu for starting the bot
                                                                admin.add_link(MenuLink(name='Start Bot', endpoint='admin.start_bot'))

                                                                # Register the file admin view
                                                                admin.add_view(CustomFileAdmin(upload_dir, '/admin/files/', name='File Manager'))

                                                                @app.route('/admin/upload', methods=['POST'])
                                                                def upload_cards():
                                                                    if 'file' not in request.files:
                                                                            return jsonify({'error': 'No file part'}), 400
                                                                                file = request.files['file']
                                                                                    if file.filename == '':
                                                                                            return jsonify({'error': 'No selected file'}), 400
                                                                                                if file:
                                                                                                        filename = secure_filename(file.filename)
                                                                                                                file_path = os.path.join(upload_dir, filename)
                                                                                                                        file.save(file_path)
                                                                                                                                card_details = upload_card_details(file_path)
                                                                                                                                        return jsonify({'message': 'File successfully uploaded', 'card_count': len(card_details)}), 200

                                                                                                                                        @app.route('/admin/start', methods=['POST'])
                                                                                                                                        def start_bot():
                                                                                                                                            # Call the bot function with the uploaded card details
                                                                                                                                                file_path = os.path.join(upload_dir, 'uploaded_cards.csv')  # Assuming the uploaded file is named this way
                                                                                                                                                    card_details = upload_card_details(file_path)
                                                                                                                                                        automate_purchase(card_details)
                                                                                                                                                            return jsonify({'message': 'Bot started'}), 200
                                                                                                                                                            