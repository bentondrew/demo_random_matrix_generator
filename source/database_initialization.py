#  Copyright 2017
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED

from drewantech_common.postgres_database \
    import (connect_to_database,
            execute_postgres_command)
from demo_random_matrix_generator.database_objects \
    import (database_name,
            Base,
            Matrix,
            Dimension,
            Point)
from demo_random_matrix_generator.databse_constants \
    import (db_user, db_password, db_host, db_port)


def create_database():
  #  Create database.
  execute_postgres_command(engine=connect_to_database(
                           user_name=db_user,
                           user_password=db_password,
                           database_host=db_host,
                           database_port=db_port,
                           database_name=db_user),
                           command='CREATE DATABASE {}'.format(database_name))
  execute_postgres_command(engine=connect_to_database(
                           user_name=db_user,
                           user_password=db_password,
                           database_host=db_host,
                           database_port=db_port,
                           database_name=db_user),
                           command=('REVOKE connect ON DATABASE {} FROM PUBLIC'
                                    .format(database_name)))


def create_tables():
  Base.metadata.create_all(bind=connect_to_database(
                           user_name=db_user,
                           user_password=db_password,
                           database_host=db_host,
                           database_port=db_port,
                           database_name=database_name))
