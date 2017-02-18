#  Copyright 2016
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED

from flask import (Flask,
                   render_template,
                   flash,
                   redirect,
                   url_for)
from os import urandom
from demo_random_matrix_generator.matrix_database_operations \
    import (create_database as matrix_create_database,
            drop_database as matrix_drop_database,
            create_tables as matrix_create_tables,
            drop_tables as matrix_drop_tables)

app = Flask(__name__)
app.secret_key = urandom(32)


@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')


@app.route('/database_initialization')
def databases_initialization():
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


@app.route('/database_tear_down')
def databases_tear_down():
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
