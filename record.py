# coding: utf-8
#インポート
import sqlite3

#データベースに接続
filepath = "test.db"
conn = sqlite3.connect(filepath) 
#filepathと同名のファイルがなければ，ファイルが作成されます

# cur.execute("""CREATE TABLE station(
#     id TEXT PRIMARY KEY,
#     lat REAL,
#     long REAL,
#     title TEXT,
#     stationCode TEXT,
#     sameAs TEXT,
#     operator TEXT,
#     context TEXT,
#     date TEXT,
#     railway TEXT,
#     type TEXT
# )""")
# conn.commit()

import json

with open('stations.geojson', 'r') as f:
    station = json.load(f)

features = station['features']

cur = conn.cursor()

for feature in features:
    # print feature['properties']
    id = feature['properties']['id']
    lat = feature['geometry']['coordinates'][1]
    long = feature['geometry']['coordinates'][0]
    title = feature['properties']['title']
    stationCode = feature['properties']['stationCode']
    sameAs = feature['properties']['sameAs']
    operator = feature['properties']['operator']
    context = feature['properties']['context']
    date = feature['properties']['date']
    railway = feature['properties']['railway']
    type = feature['properties']['type']
    cur.execute('INSERT INTO station (id, lat, long, title, stationCode, sameAs, operator, context, date, railway, type) VALUES (?,?,?,?,?,?,?,?,?,?,?)', (id, lat, long, title, stationCode, sameAs, operator, context, date, railway, type))

conn.commit()