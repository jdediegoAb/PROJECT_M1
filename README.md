# MADnumentos 🚴🏽‍♀️ 🏛
*Ironhack Data Analytics Module 1 Project*
## Your app to find the closest bicimad stations when you are visting monumental buildings in Madrid.
    The app offers you two options:
        Option 1: for the monument you choose, you can observe the closest bicimad station and the distance (meters)
        Option 2: entering your email you will received an email with all the monumental buildings and the closest bicimad station for each one
### Technology stack 🤓
    Python, Pandas, SQL

### Core technical concepts and inspiration 📸
    The app is perfect when you are planning to visit Madrid monumental buildings, and also good to make your own plan without losing time.
### Configuration 💻
    import argparse
    from shapely.geometry import Point
    import geopandas as gpd 
    import sqlalchemy
    from sqlalchemy import create_engine
    from sqlalchemy import inspect
    import pandas as pd
    import requests
    import fuzzywuzzy
    from fuzzywuzzy import fuzz,process
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders
    import os.path
### Usage 🖥
    Parameters, return values, known issues, thrown errors.

    1.Option One: python main.py -f One
        -Introduce a Monument name
        -result: Monument name, monument adress, closest bicimad station, bicimad address, distance(meters)

    2.Option All: python main.py -f All
        -Introduce your email
        -results: *will be sent to your email*
                1.List of monuments(csv) with all the monuments names, monuments adresses, closest bicimad stations,bicimad adresses, distances.
                2.Map(html)----*Need to download the file to access the interactive map*

### Folder structure 💾
└── PROJECT_M1

    ├── __pycache__
    │      └── geofunctions.cpython-39.pyc
    ├── main.py
    ├── prejectsql.ipynb
    ├── function-module.ipynb
    ├── README.md
    ├── main_script.py
    ├── .ipynb_checkpoints
    │      └── prejectsql-checkpoint.ipynb
    │  
    ├── modules
    │      ├── Modgen.py
    │      ├── sendmail.py
    │      ├── geofunctions.py
    │      ├── __pycache__
    │            ├── geofunction.cpython-39.pyc
    │            ├── Modgen.cypython-39.pyc
    │            └── sendmail.cypython-39-pyc
    ├── monuments_map.html
    ├── bicimad_stations_202207091252.csv
    ├── monument_list.csv
    ├── .gitignore
    ├── .env

## ToDo 👨🏻‍💻
    Develop the app with more information and posibilities: 
        -More monuments or different places of interest. 
        -Insert more sustainable transports.
    facilitate the enter of monuments when your are choosing one (even, suggestions)
        -refactorize the code

## Contact info
    j.dediego.abad@gmail.com