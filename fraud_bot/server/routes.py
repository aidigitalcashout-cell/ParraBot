# routes.py

from flask import Blueprint, request, jsonify
from card_manager import upload_card_details

admin_routes = Blueprint('admin', __name__)

@admin_routes.route('/upload', methods=['POST'])
def upload_cards():
    if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
                file = request.files['file']
                    if file.filename == '':
                            return jsonify({'error': 'No selected file'}), 400
                                if file:
                                        file_path = f'./uploads/{file.filename}'
                                                file.save(file_path)
                                                        card_details = upload_card_details(file_path)
                                                                return jsonify({'message': 'File successfully uploaded', 'card_count': len(card_details)}), 200

                                                                @admin_routes.route('/start', methods=['POST'])
                                                                def start_bot():
                                                                    # Call the bot function with the uploaded card details
                                                                        automate_purchase(card_details)
                                                                            return jsonify({'message': 'Bot started'}), 200
                                        