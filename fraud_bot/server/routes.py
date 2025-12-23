# routes.py

from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from card_manager import upload_card_details
from purchase_automation import automate_purchase
import os

admin_routes = Blueprint('admin', __name__)


@admin_routes.route('/upload', methods=['POST'])
def upload_cards():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    uploads_dir = os.path.join(os.path.dirname(__file__), '..', 'uploads')
    uploads_dir = os.path.normpath(uploads_dir)
    os.makedirs(uploads_dir, exist_ok=True)

    filename = secure_filename(file.filename)
    file_path = os.path.join(uploads_dir, filename)
    file.save(file_path)
    card_details = upload_card_details(file_path)
    return jsonify({'message': 'File successfully uploaded', 'card_count': len(card_details), 'filename': filename}), 200


@admin_routes.route('/start', methods=['POST'])
def start_bot():
    data = request.get_json(silent=True) or {}
    filename = data.get('filename')
    uploads_dir = os.path.join(os.path.dirname(__file__), '..', 'uploads')
    uploads_dir = os.path.normpath(uploads_dir)
    if not filename:
        filename = 'uploaded_cards.csv'
    file_path = os.path.join(uploads_dir, filename)
    if not os.path.exists(file_path):
        return jsonify({'error': f'File not found: {filename}'}), 404
    card_details = upload_card_details(file_path)
    automate_purchase(card_details)
    return jsonify({'message': 'Bot started', 'processed_cards': len(card_details)}), 200
