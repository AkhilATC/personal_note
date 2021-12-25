from flask import jsonify, request, Blueprint, current_app
import sqlite3
from datetime import datetime

from factory import db
from apps.model import Notes
# blueprint definition
note_module = Blueprint('note_module', __name__, url_prefix='/my_note_space')


@note_module.route('/fetch_notes', methods=['GET'])
def fetch_all_notes():
    """

    :return:
    """
    try:
        all_notes = Notes.query.all()
        result = [d.__dict__ for d in all_notes]
        result = [{'id': x['id'], 'title':x['title'], 'time':x.get('time_logged')} for x in result]
        return jsonify(result), 200
    except Exception as e:
        current_app.logger.info(e)
        return jsonify({'status': 'Failed to fetch'}), 400


@note_module.route('/write_note', methods=['POST'])
def write_notes():
    """

    :return:
    """
    try:
        payload = request.json
        title = payload.get('title')
        content = payload.get('content')
        if not title or not content:
            return jsonify({'message': "mandatory feilds can\'t be empty"})
        note = Notes(title=title, content=content)
        db.session.add(note)
        db.session.commit()
        return jsonify({'message': 'sucess'}), 200
    except Exception as e:
        return jsonify({'message': 'failed'}), 400