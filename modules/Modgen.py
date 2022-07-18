import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import inspect
import pandas as pd
import requests
import fuzzywuzzy
from fuzzywuzzy import fuzz,process
import geofunctions as geo

conection_string='mysql+pymysql://ironhack_user:%Vq=c>G5@173.201.189.217/BiciMAD'
engine = create_engine(conection_string)
inspector = inspect(engine)
inspector.get_table_names()
df_stations = pd.read_sql_query("SELECT * FROM bicimad_stations", engine)
#df_stations=pd.read_csv('./bicimad_stations_202207091252.csv')

df_stations[["longitude","latitude"]]=df_stations["geometry.coordinates"].str.split(",",expand=True)
df_stations['longitude'] = df_stations['longitude'].str.replace('[','',regex=True)
df_stations["latitude"]=df_stations['latitude'].str.replace(']','',regex=True)
df_stations['latitude'] = pd.to_numeric(df_stations['latitude'])
df_stations['longitude'] = pd.to_numeric(df_stations['longitude'])

url='/catalogo/208844-0-monumentos-edificios.json'
end_point='https://datos.madrid.es/egob'
response = requests.get(end_point+url)
mon_json = response.json()

mon_json['@graph']
#la key donde esta toda la info es @graph
df_monuments = pd.DataFrame(mon_json['@graph'])
df_monuments = pd.json_normalize(mon_json['@graph']).dropna(subset=['location.latitude','location.longitude'])

def one_monument():
    monument=input('Monument name: ')
    match_monument = process.extractOne(monument,df_monuments['title'], score_cutoff=80)
    z = df_monuments.loc[df_monuments['title']== match_monument[0]]
    n=z.iloc[0]['title']
    select_monument = df_monuments.loc[df_monuments['title']== n].reset_index(drop=True)
    df_stations['distance']=df_stations.apply(lambda x: geo.distance_meters(x['latitude'], 
                                                                    x['longitude'],
                                                                    select_monument[('location.latitude')],
                                                                    select_monument[('location.longitude')]),axis=1)
    df_stations_1=df_stations[df_stations['distance']==df_stations['distance'].min()].reset_index(drop=True)

    df_output=select_monument[['title','address.street-address']].join(df_stations_1[['name','address']])
    return df_output


def all_monuments():
    ALL_monuments = df_monuments[['title','address.street-address','location.latitude','location.longitude']].reset_index(drop=True)
    ALL_MONUMENTS=[]
    for index, row in ALL_monuments.iterrows():
        df_stations['distance']=df_stations.apply(lambda x: geo.distance_meters(x['latitude'], 
                                                                    x['longitude'],
                                                                    row[('location.latitude')],
                                                                    row[('location.longitude')]),axis=1)
        df1=df_stations[df_stations['distance']==df_stations['distance'].min()].reset_index(drop=True)
        df1['title']=row['title']
        #display(df1)
        ALL_MONUMENTS.append(df1)
    df_final = pd.concat(ALL_MONUMENTS)
    df_output2= pd.merge(ALL_monuments[['title','address.street-address']], df_final[['name','address','title']], on ='title')
    return(df_output2)