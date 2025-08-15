from app import create_app, db
from flask_migrate import upgrade

app = create_app()

@app.cli.command()
def deploy():
    """Run deployment tasks."""
    # migrate database to latest revision
    upgrade()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
