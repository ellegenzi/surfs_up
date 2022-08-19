# Import dependencies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Set up the database
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the database into our classes
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create session link from Python to database
session = Session(engine)

# Set up Flask
# Define the Flask app
app = Flask(__name__)

# Define the welcome route
@app.route("/")

# Create the function
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# Create the route for precipitation analysis
@app.route("/api/v1.0/precipitation")

# Create the function
def precipitation():
    # calculate the date one year ago from the most recent date in database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # write a query to get the date and precipitation for the previous year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    # create a dictionary with the date as the key and precipitation as the value
    precip = {date: prcp for date, prcp in precipitation}
    # jsonify the dictionary and return the results
    return jsonify(precip)

# Create the stations route
@app.route("/api/v1.0/stations")

# Create the function
def stations():
    # create a query that will allow us to get all stations into our database
    results = session.query(Station.station).all()
    # unravel the results into a one-dimensional array and convert to a list
    stations = list(np.ravel(results))
    # jsonify the list and return it as JSON
    return jsonify(stations=stations)

# Create the route for temperature observations
@app.route("/api/v1.0/tobs")

# Create the function
def temp_monthly():
    # calculate the date one year ago from the last date in database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # add query statement for the primary station for all temp
    # observations from previous year
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    # unravel the results into a one-dimensional array and convert to a list 
    temps = list(np.ravel(results))
    # jsonify the list and return the results
    return jsonify(temps=temps)

# Create the route to report on minimum, average, and maximum temps
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Create the function (add two parameters and set both to None)
def stats(start=None, end=None):
    # create a list
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    # add an if-not statement to query our database using the list,
    # unravel the results into a one-dimensional array,
    # and convert to a list
    if not end:
        # the *sel indicates there will be multiple results: min, avg, and max temps
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        # jsonify the list and return the results
        return jsonify(temps)

    # calculate the temp min, avg, and max with start and end dates
    # use the sel list, which are the data points we need to collect
    # create the next query
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    # unravel the results into a one-dimensional array and convert to a list
    temps = list(np.ravel(results))
    # jsonify the list and return the results
    return jsonify(temps)

# to run the app, use flask run
# do this after navigating to the directory where app.py is saved.