# sqlalchemy-challenge

CWRU Bootcamp sqlalchemy homework

# the hawaii.squlite file was not working so it was recreated as a Postgres DB for the purposes of this homework.

After a lot of extra data mapping, table creation and importing the following has been completed:

1. Engine was created and connected to the postgres hawaii_db database.
2. The database has been reflected into a new model.
3. The db tables were reflected and the tables mapped to bases
4. Measurement and Station references were completed.
5. Session was created.
6. The earliest and latest (most recent) dates were identified.
7. ORM query and date time was used to identify one year ago.
8. ORM query was used to obtain last 12 months of date and percipitation data.
9. Data from the ORM query in #8 was saved to a pandas dataframe and ordered by date, columns were renamed and index set to the date.
10. Plot of dates and percipitation was created using pandas and Matplotlib
11. Sumamry Statistics of the precipitation data created and saved.
12. Query to determine the total number of stations was created.
13. Query to determine which station by id had the most measurements/rows.
14. Min, Max, Avererage and total count of tempatures were identified.
15. Final Historgram created.
16. Session Closed.

Flask/JSON Activities

1. All Libraries and db config files were imported.
2. Database connection was created and reflected including tables.
3. References to each table were saved.
4. A sesion was started.
5. The initial route was created to welcome the viewer and show all available routes.
6. The station route was created next with a dictionary created and the results displayed using jsonify.
7. The precipation route was created next with a dictionary create and the results displayed using jsonify.
8. The tobs route was create next with a dictionary cretaed and the results displayed using jsonfiy.
9. The start date route was created leveraging numerous suggestion from other online, including using simplejosn.
10.
