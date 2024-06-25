from flask import render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from app import db
from app.main import bp
from app.main.forms import EntryForm
from app.models import JournalEntry
import os
from werkzeug.utils import secure_filename
import base64
from app.utils import create_image_variation

@bp.route('/camera')
@login_required
def camera():
    return render_template('camera.html')

@bp.route('/upload_image', methods=['POST'])
def upload_image():
    data = request.get_json()
    image_data = data['image'].split(",")[1]
    image_data = base64.b64decode(image_data)
    filename = secure_filename(f"{current_user.id}_image.png")
    image_dir = os.path.join('app', 'static', 'images')
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    image_path = os.path.join(image_dir, filename)
    with open(image_path, 'wb') as f:
        f.write(image_data)

    # Use the new AI service for transformation
    api_key = "sk-proj-dTQQZkaoTFRiAbW9txo9T3BlbkFJRIl6Ybrj9drGL4sxnBex"
    cartoon_image_url = create_image_variation(api_key)
    if cartoon_image_url is None:
        return jsonify({'error': 'Failed to transform image'}), 500

    return jsonify({'cartoon_image_url': cartoon_image_url})

@bp.route('/new_entry', methods=['GET', 'POST'])
@login_required
def new_entry():
    form = EntryForm()
    image_url = request.args.get('image_url')
    if image_url:
        form.image_url.data = image_url  # Prefill the image URL field
    if form.validate_on_submit():
        entry = JournalEntry(text=form.text.data, image_url=form.image_url.data, user_id=current_user.id)
        db.session.add(entry)
        db.session.commit()
        flash('Your entry has been added.')
        return redirect(url_for('main.entries'))
    return render_template('new_entry.html', title='New Entry', form=form)

@bp.route('/entries')
@login_required
def entries():
    entries = JournalEntry.query.filter_by(user_id=current_user.id).order_by(JournalEntry.date.desc()).all()
    return render_template('entries.html', title='Your Entries', entries=entries)

@bp.route('/')
def index():
    return render_template('index.html', title='Home')