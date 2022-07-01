from cgitb import html
from website import create_app

app = create_app()
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/route_name')
def method_name():
    return "<h1>Gosho</h1>"

