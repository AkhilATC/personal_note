from flask import jsonify, request, Blueprint, current_app
import sqlite3
from datetime import datetime

from factory import db
from apps.model import Notes
# blueprint definition
note_module = Blueprint('note_module', __name__, url_prefix='/my_note_space')

# http://192.168.18.9:7001/apidocs/#/


@note_module.route('/fetch_notes', methods=['GET'])
def fetch_all_notes():
    """Example endpoint for get list of notes
       This is using docstrings for specifications.
       ---
       tags:
            - my_note_space
       responses:
         200:
           description: A list of objects
           examples:
             application/json:
                [{"content": "NB- Buy veggies","id": 1,"time_logged": "12/26/2021","title": "do some"}]

         400:
           description: A empty list
           examples:
                []
       """
    try:
        all_notes = Notes.query.all()
        result = [d.__dict__ for d in all_notes]
        print(result)
        result = [{'id': x['id'],
                   'title':x['title'],
                   'content':x['content'],
                   'time_logged':x['time_logged'].strftime("%m/%d/%Y")} for x in result]
        return jsonify(result), 200
    except Exception as e:
        current_app.logger.info(e)
        return jsonify([]), 400


@note_module.route('/write_note', methods=['POST'])
def write_notes():
    """Example endpoint for write notes
           This is using docstrings for specifications.
           ---
           parameters:
                - name: title
                  in : payload
                  required: true
                  type: String
                  description: title name
                - name: content
                  in : payload
                  required: true
                  type: String
                  description: content of notes
           tags:
                - my_note_space
           responses:
             200:
               description: Sucessfully write notes
               examples:
                 application/json:
                    {'message': 'success'}

             400:
               description: fail response
               examples:
                    {'message': 'failed'}
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
        return jsonify({'message': 'success'}), 200
    except Exception as e:
        return jsonify({'message': 'failed'}), 400


@note_module.route('/<id>/erase_note', methods=['DELETE'])
def delete_note(**kwargs):
    """Example endpoint for delete notes
               This is using docstrings for specifications.
               ---
               parameters:
                    - name: id
                      in : path
                      required: true
                      type: String
                      description: unique id of note

               tags:
                    - my_note_space
               responses:
                 200:
                   description: Successfully delete notes
                   examples:
                     application/json:
                        {'message': 'success'}

                 400:
                   description: fail response
                   examples:
                        {'message': 'failed'}
    """
    try:
        # user = User.query.get(id)


        id = kwargs.get('id')
        record = Notes.query.filter_by(id=id).delete()
        print(f"Record -- {record}")
        db.session.commit()
        return jsonify({'message': 'success'}), 200
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
        return jsonify({'message': 'success', 'record':record}), 200
    except Exception as e:
        return jsonify({'message': 'failed'}), 400