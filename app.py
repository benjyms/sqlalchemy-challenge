# importing all libraries and configs needed for creating routes to noted items
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
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
        f"  <br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/tobs<br/>"
        
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

if __name__ == '__main__':
    app.run(debug=True)