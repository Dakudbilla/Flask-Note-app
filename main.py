from venv import create
from website import create__app

app = create__app()

if __name__ == '__main__' :
    app.run(debug=True)