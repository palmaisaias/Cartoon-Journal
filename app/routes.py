from flask import Blueprint
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app import db
from app.models import JournalEntry
from app.main import bp
from app.main.forms import EntryForm
from flask import request, jsonify
from app import app
import os
from werkzeug.utils import secure_filename
from app.utils import transform_image
from app.forms import EntryForm
from app.models import JournalEntry
import base64

bp = Blueprint('main', __name__)

@app.route('/camera')
@login_required
def camera():
    return render_template('camera.html')

@bp.route('/')
def index():
    return "Hello, welcome to Cartoon Journal!"

@bp.route('/test')
def test():
    return "This is a test route!"

@app.route('/new_entry', methods=['GET', 'POST'])
@login_required
def new_entry():
    form = EntryForm()
    if form.validate_on_submit():
        entry = JournalEntry(text=form.text.data, image_url=form.image_url.data, user_id=current_user.id)
        db.session.add(entry)
        db.session.commit()
        flash('Your entry has been added.')
        return redirect(url_for('entries'))
    return render_template('new_entry.html', title='New Entry', form=form)

@app.route('/upload_image', methods=['POST'])
def upload_image():
    data = request.get_json()
    image_data = data['image'].split(",")[1]
    image_data = base64.b64decode(image_data)
    filename = secure_filename(f"{current_user.id}_image.png")
    image_path = os.path.join('static/images', filename)
    with open(image_path, 'wb') as f:
        f.write(image_data)
    cartoon_image_url = transform_image(image_path)
    return jsonify({'cartoon_image_url': cartoon_image_url})

@app.route('/entries')
@login_required
def entries():
    entries = JournalEntry.query.filter_by(user_id=current_user.id).order_by(JournalEntry.date.desc()).all()
    return render_template('entries.html', title='Your Entries', entries=entries)