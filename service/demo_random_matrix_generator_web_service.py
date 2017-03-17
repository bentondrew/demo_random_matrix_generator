#  Copyright 2016
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED

from flask import (Flask,
                   jsonify)
from os import urandom

app = Flask(__name__)
app.secret_key = urandom(32)


@app.route('/create_matrix_database', methods=['PUT'])
def create_matrix_database():
  try:
    from demo_random_matrix_generator.database_initialization \
        import (create_database)
    create_database()
    return jsonify({'status': 'Successfully created matrix database.'}), 201
  except Exception as e:
    return jsonify({'status': 'Error in creating matrix database: {}'
                   .format(e)}), 500


@app.route('/create_matrix_tables', methods=['PUT'])
def create_matrix_tables():
  try:
    from demo_random_matrix_generator.database_initialization \
        import (create_tables)
    create_tables()
    return jsonify({'status': 'Successfully created matrix tables.'}), 201
  except Exception as e:
    return jsonify({'status': 'Error in creating matrix tables: {}'
                   .format(e)}), 500


@app.route('/drop_matrix_database', methods=['DELETE'])
def drop_matrix_database():
  try:
    from demo_random_matrix_generator.database_tear_down \
        import (drop_database)
    drop_database()
    return jsonify({'status': 'Successfully dropped matrix database.'}), 201
  except Exception as e:
    return jsonify({'status': 'Error in dropping matrix database: {}'
                   .format(e)}), 500


@app.route('/drop_matrix_tables', methods=['DELETE'])
def drop_matrix_tables():
  try:
    from demo_random_matrix_generator.database_tear_down \
        import (drop_tables)
    drop_tables()
    return jsonify({'status': 'Successfully dropped matrix tables.'}), 201
  except Exception as e:
    return jsonify({'status': 'Error in dropping matrix tables: {}'
                   .format(e)}), 500
