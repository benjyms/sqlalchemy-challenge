# importing all libraries and configs needed for creating routes to noted items
import numpy as np
import datetime

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import simplejson as json
from sqlalchemy.sql.expression import join

from config import user,password

#################################################
# Database Setup
#################################################
engine = create_engine(f'postgresql://{user}:{password}@localhost:5432/hawaii_db')
conn = engine.connect()

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
Base.classes.keys()

# # Save reference to the table
Measurement = Base.classes.measurements
Station = Base.classes.stations

# # Start a session to query the database
session = Session(engine)

# #################################################
# # Flask Setup
# #################################################
app = Flask(__name__)

# #################################################
# # Flask Routes
# #################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to Benjy's flask page<br/>"
        f"Please explore some Hawaii Weather Data I have collected from a database.<br/>"
        f"I find copy and paste in this page of the available routes works best.<br/>"
        f"For the start & start/end routes, please play with the dates to see more or different data.<br/>"
        f"  <br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/stations<br/>Returns a JSON list of the weather stations<br/><br/>"
        f"/api/v1.0/precipitation<br/>Returns a JSON list of precipitation data for the dates between 8/23/16 and 8/23/17<br/><br/>"
        f"/ap/v1.0/tobs<br/>Returns a JSON list of the Temperature Observations (tobs) for each station for the dates between 8/23/16 and 8/23/17<br/><br/>"
        f"/api/v1.0/<start>Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for the dates between the given start date and 8/23/17.<br/>"
        f" <br/>"
        f"Example: -------> http://127.0.0.1:5000/api/v1.0/2016-08-23<br/>"
        f" <br/>"
        f"/api/v1.0/<start>/<end><br/>Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for the dates between the given start date and end date<br/><br/>."
        f"/api/v1.0/<start>Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for the dates between the given start date and 8/23/17.<br/>"
        f" <br/>"
        f"Example: -------> http://127.0.0.1:5000/api/v1.0/2016-08-23/2016-08-27<br/>"
        f" <br/>"
    )

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(Station.station, Station.name).all()

    session.close()

   

# Convert list of tuples into normal list
    station_js = []
    for station, name in results:
        station_dict = {}
        station_dict["station id"] = station
        station_dict["station name"] = name
        station_js.append(station_dict)
  
    return jsonify(station_js)


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date > '2016-08-22').all()

    session.close()

    # Convert list of tuples into normal list
    precipitation_js = []
    for date, prcp in results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["inches"] = str(prcp)
        precipitation_js.append(precipitation_dict)

    return jsonify(precipitation_js)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.date > '2016-08-22').\
    filter(Measurement.station == "USC00519281").\
    order_by(Measurement.date).all()


    session.close()

    # Convert list of tuples into normal list
    # tobs = list(np.ravel(results))

    tobs_js = []
    for date, tobs in results:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["temperature"] = tobs
        tobs_js.append(tobs_dict)

    return jsonify(tobs_js)

# Flask route for daily normals with given start date
@app.route("/api/v1.0/<start>")
def daily_normals(start):
	"""Returns a json list of daily normals when given a start date"""

	# Calculate the daily normals. Normals are the averages for min, avg, and max temperatures.
	daily_calc = [func.min(Measurement.tobs),\
					func.avg(Measurement.tobs),\
					func.max(Measurement.tobs)]
	daily_query = session.query(Measurement.date,*daily_calc).\
                filter((Measurement.date) >= start).\
                order_by(Measurement.date).\
				group_by(Measurement.date)


	# Convert query results into a dictionary
	daily_data = []
	for daily_normals in daily_query:
		(t_date, t_min, t_avg, t_max) = daily_normals
		norms_dict = {}
		norms_dict["Date"] = t_date
		norms_dict["Temp Min"] = t_min
		norms_dict["Temp Avg"] = t_avg
		norms_dict["Temp Max"] = t_max
		daily_data.append(norms_dict)

	# Return a json list of daily normals
	return jsonify(daily_data)			

@app.route("/api/v1.0/<start>/<end>")
def daily_normals2(start,end):
	"""Returns a json list of daily normals within a given range"""

	# Calculate the daily normals. Normals are the averages for min, avg, and max temperatures
	daily_calc2 = [func.min(Measurement.tobs),\
					func.avg(Measurement.tobs),\
					func.max(Measurement.tobs)]
	daily_query2 = session.query(Measurement.date,*daily_calc2).\
				filter((Measurement.date) >= start).\
				filter((Measurement.date) <= end).\
                order_by(Measurement.date).\
				group_by(Measurement.date)

	# Convert query results into a json dictionary
	daily_data2 = []
	for daily_normals2 in daily_query2:
		(t_date2, t_min2, t_avg2, t_max2) = daily_normals2
		norms_dict2 = {}
		norms_dict2["Date"] = t_date2
		norms_dict2["Temp Min"] = t_min2
		norms_dict2["Temp Avg"] = t_avg2
		norms_dict2["Temp Max"] = t_max2
		daily_data2.append(norms_dict2)

	# Return a json list of dialy normals
	return jsonify(daily_data2)

if __name__ == '__main__':
    app.run(debug=True)