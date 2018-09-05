import os
from dotenv import load_dotenv
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_script.commands import ShowUrls, Clean

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

from app import create_app, db

app = create_app(os.getenv('FLASK_CONFIG', 'default'))
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('show-urls', ShowUrls())
manager.add_command('clean', Clean())
manager.add_command('db', MigrateCommand)

def init_db():
    import sqlalchemy

    fe_db_uri = app.config['SQLALCHEMY_DATABASE_URI']
    server_uri, database = fe_db_uri.rsplit('/', maxsplit=1)
    engine = sqlalchemy.create_engine(server_uri, echo=True)
    engine.execute("CREATE DATABASE IF NOT EXISTS {} CHAR SET 'utf8mb4'".format(database))

    db.create_all()


if __name__ == '__main__':
    try:
        manager.run()
    except KeyboardInterrupt:
        print('Shutting down')
