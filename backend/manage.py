from hyip import app
from hyip.models import db, redis_client
from flask_migrate import Migrate
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    # test db initializations go below here
    # db.create_all()
    redis_client.init_app(app)

    manager.run()