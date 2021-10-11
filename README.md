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
12. Final Historgram created.
