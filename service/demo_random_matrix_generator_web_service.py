#  Copyright 2016
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED

from flask import (Flask,
                   render_template,
                   flash,
                   redirect,
                   url_for,
                   jsonify)
from os import urandom

app = Flask(__name__)
app.secret_key = urandom(32)


@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')


@app.route('/database_initialization')
def database_initialization():
  try:
    from demo_random_matrix_generator.database_initialization \
        import (create_database,
                create_tables)
    flash('Attempting to create matrix database.')
    create_database()
    flash('Successfully created matrix database.')
    flash('Attempting to create matrix database tables.')
    create_tables()
    flash('Successfully created matrix database tables.')
  except Exception as e:
    raise flash('Error in initializing databases: {}'.format(e))
  return redirect(url_for('index'))


@app.route('/create_matrix_database', methods=['GET'])
def create_matrix_database():
  try:
    from demo_random_matrix_generator.database_initialization \
        import (create_database)
    create_database()
    return jsonify({'status': 'Successfully created matrix database.'}), 201
  except Exception as e:
    return jsonify({'status': 'Error in creating matrix database: {}'
                   .format(e)}), 500


@app.route('/create_matrix_tables', methods=['GET'])
def create_matrix_tables():
  try:
    from demo_random_matrix_generator.database_initialization \
        import (create_tables)
    create_tables()
    return jsonify({'status': 'Successfully created matrix tables.'}), 201
  except Exception as e:
    return jsonify({'status': 'Error in creating matrix tables: {}'
                   .format(e)}), 500


@app.route('/database_tear_down')
def database_tear_down():
  try:
    from demo_random_matrix_generator.database_tear_down \
        import (drop_database,
                drop_tables)
    flash('Attempting to drop matrix database tables.')
    drop_tables()
    flash('Successfully dropped matrix database tables.')
    flash('Attempting to drop matrix database.')
    drop_database()
    flash('Successfully dropped matrix database.')
  except Exception as e:
    raise flash('Error in tearing down databases: {}'.format(e))
  return redirect(url_for('index'))


@app.route('/drop_matrix_database', methods=['GET'])
def drop_matrix_database():
  try:
    from demo_random_matrix_generator.database_tear_down \
        import (drop_database)
    drop_database()
    return jsonify({'status': 'Successfully dropped matrix database.'}), 201
  except Exception as e:
    return jsonify({'status': 'Error in dropping matrix database: {}'
                   .format(e)}), 500


@app.route('/drop_matrix_tables', methods=['GET'])
def drop_matrix_tables():
  try:
    from demo_random_matrix_generator.database_tear_down \
        import (drop_tables)
    drop_tables()
    return jsonify({'status': 'Successfully dropped matrix tables.'}), 201
  except Exception as e:
    return jsonify({'status': 'Error in dropping matrix tables: {}'
                   .format(e)}), 500
