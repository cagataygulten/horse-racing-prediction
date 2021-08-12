=================
Prediction and Data Analysis of Horse Racing in Turkey
=================

- `Introduction`_

- `How to Use`_

  #. `For Ipython`_

  #. `For Python Script`_

- `Getting Help and Contributing`_

============
Introduction
============

This project gives a clue based on statistics, a programming language along with machine learning
algorithms and math to horse racing followers and by analysing horse racing data, makes some inferences to add
cultural knowledge in the horse racing community in Turkey.

|

Source codes and a technical report including data analysis is available in repository.

----
Note
----

In case downloading whole project file as a zip, models.pkl should be downloaded separately.

It is not permitted to publish whole dataset, therefore, a part of the dataset is created, including all horse statistics of races between only 12/04/2021 and 18/04/2021 for demonstration. Date and city can be obtained from The Turkish Jockey Club website.
(https://www.tjk.org/TR/YarisSever/Info/Page/GunlukYarisProgrami)


.. image:: https://github.com/cagataygulten/horse-racing-prediction/blob/master/pics/User_Manual_1.jpg?raw=true
   :align: center

|


===============
How to Use
===============

Run the script named "horce_racing_predicter_demo.py" or  ipython notebook named "Horse_Racing_Regression_Predictions.ipynb".

-------------------
For Ipython
-------------------

.. image:: https://github.com/cagataygulten/horse-racing-prediction/blob/master/pics/User_Manual_2.jpg?raw=true
   :align: center

|
Change date and city to asked race inputs at the 6th cell (above) by keeping the current date format. Unless the date is not between 12-18/04/2021, it only considers jockeys statistics

|

.. image:: https://github.com/cagataygulten/horse-racing-prediction/blob/master/pics/User_Manual_3.jpg?raw=true
   :align: center

|
Then enter desired race number as input to function in 8th cell (above).

After running all cells, prediction table is plotted. To make predictions for other races, change race number input and run just 8th cell again. If another day or city is asked, running all cells is required to scrape new data.

|

.. image:: https://github.com/cagataygulten/horse-racing-prediction/blob/master/pics/User_Manual_4.jpg?raw=true
   :align: center
|
The table represents predicted total times of all horses. But it considers distance as categorical value, that means predicted times are not accurate for that race, just used for comparison. Lower time values means better performance, which are green cells.


-------
For Python Script
-------

.. image:: https://github.com/cagataygulten/horse-racing-prediction/blob/master/pics/User_Manual_5.jpg?raw=true
   :align: center
|

It requires user input. Enter desired date and city. After it scrapes all required data, enter race number.
|

.. image:: https://github.com/cagataygulten/horse-racing-prediction/blob/master/pics/User_Manual_6.jpg?raw=true
   :align: center

|

.. image:: https://github.com/cagataygulten/horse-racing-prediction/blob/master/pics/User_Manual_7.jpg?raw=true
   :align: center
|
After prediction, script keeps asking race number to proceed next races.

============
Getting Help and Contributing
============



Questions and contributions of all kinds are welcome.

Contact: cagataygulten@gmail.com

