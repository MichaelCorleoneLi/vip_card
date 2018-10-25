import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

from app import create_app, db, models

app = create_app(os.getenv('FLASK_CONFIG', 'default'))


@app.shell_context_processor
def make_shell_context():
    return dict(models=models, app=app, db=db)


@app.cli.command
def init_db():
    import sqlalchemy

    fe_db_uri = app.config['SQLALCHEMY_DATABASE_URI']
    server_uri, database = fe_db_uri.rsplit('/', maxsplit=1)
    engine = sqlalchemy.create_engine(server_uri, echo=True)
    engine.execute("CREATE DATABASE IF NOT EXISTS {} CHAR SET 'utf8mb4'".format(database))

    db.create_all()
