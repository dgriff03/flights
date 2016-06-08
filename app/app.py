from flask import Flask, render_template, g, request

from datetime import date, timedelta
import json

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
    friends = [{'name': 'Keven', 'airport': 'BOS'},
               {'name': 'Matt', 'airport': 'JFK'},
               {'name': 'Mark', 'airport': 'LAX'},
               {'name': 'Stephen', 'airport': 'DCA'},
               {'name': 'Nick', 'airport': 'DCA'}]
    return flight_grid(friends)

def flight_grid(friends):
    airports = list(set(map(lambda x: x['airport'], friends)))
    date_pairs = []
    def date_formater(d):
      return d.strftime("%b %d")

    return render_template('flight_grid.html',
      friends=friends, 
      airports=airports,
      date_pairs=build_date_pairs(date_formater))

@app.route('/flights.json')
def flights():
    origin = request.args.get('origin', '')
    destination = request.args.get('destination', '')
    offset = request.args.get('offset', '')
    return json.dumps(flight_info(origin, destination, offset))


############################################
#             Helper Functions             #
############################################

def flight_info(origin, destination, offset):
  price_data = {
    'BOS': '77',
    'DCA': '152',
    'ORD': '88',
    'JFK': '300',
    'LAX': '143',
  }
  price = int(price_data.get(destination, '204'))
  price -= int(offset) * 20
  return {'price': str(price), 'link':  'http://google.com', 'airline': 'AA'}

def build_date_pairs(date_formater):
  pairs = []
  friday = get_closest_friday()
  for i in range(3):
    friday_offset = timedelta(7 * i)
    sunday_offset = timedelta(2 + (7 * i))
    pairs.append(
      (date_formater(friday + friday_offset),
       date_formater(friday + sunday_offset))
    ) 
  return pairs

def get_closest_friday():
  today = date.today()
  day_of_week  = today.weekday()
  FRIDAY = 4
  if day_of_week < FRIDAY:
    day_of_week += 7
  delta = day_of_week - FRIDAY
  return today + timedelta(days=delta)

if __name__ == '__main__':
    app.run(debug=True)