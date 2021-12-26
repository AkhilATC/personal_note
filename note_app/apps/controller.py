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
        print(result)
        result = [{'id': x['id'],
                   'title':x['title'],
                   'content':x['content'],
                   'time_logged':x['time_logged'].strftime("%m/%d/%Y, %H:%M:%S")} for x in result]
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


@note_module.route('/erase_note', methods=['POST'])
def delete_note():
    """

    :return:
    """
    try:
        # user = User.query.get(id)
        payload = request.json
        id = payload.get('id')
        record = Notes.query.filter_by(id=id).delete()
        print(f"Record -- {record}")
        db.session.commit()
        return jsonify({'message': 'sucess'}), 200
    except Exception as e:
        print(e)
        return jsonify({'message': 'failed'}), 400


@note_module.route('/<id>/get_note', methods=['POST'])
def get_note(**kwargs):
    """

    :return:
    """
    try:
        # user = User.query.get(id)

        id = kwargs.get('id')
        record = Notes.query.get(id)
        printf(f"Record -- {record}")
        return jsonify({'message': 'sucess', 'record':record}), 200
    except Exception as e:
        return jsonify({'message': 'failed'}), 400