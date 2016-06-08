from flask import Flask, render_template, g

app = Flask(__name__)

@app.route('/')
def home():
    g.path = '/'
    return render_template('home.html')

@app.route('/omar')
def omar():
    g.path = '/omar'
    friends = [{'name': 'A', 'airport': 'BOS'},
               {'name': 'B', 'airport': 'ORD'},
               {'name': 'C', 'airport': 'LAX'},
               {'name': 'D', 'airport': 'ORD'},
               {'name': 'E', 'airport': 'DFW'}]
    return flight_grid(friends)

@app.route('/daniel')
def daniel():
    g.path = '/daniel'
    friends = [{'name': 'A', 'airport': 'BOS'},
               {'name': 'B', 'airport': 'JFK'},
               {'name': 'C', 'airport': 'LAX'},
               {'name': 'D', 'airport': 'ORD'},
               {'name': 'E', 'airport': 'BOS'}]
    return flight_grid(friends)

def flight_grid(friends):
    airports = list(set(map(lambda x: x['airport'], friends)))
    return render_template('flight_grid.html', friends=friends, airports=airports)

@app.route('/flights')
def flights():
    omars_fundtion()
    return render_template('home.html') 






if __name__ == '__main__':
    app.run()