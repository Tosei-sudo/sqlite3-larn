# coding: utf-8
#インポート
import sqlite3

#データベースに接続
filepath = "test.db"
conn = sqlite3.connect(filepath) 
#filepathと同名のファイルがなければ，ファイルが作成されます

#テーブルを作成
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS items")

cur.execute("""CREATE TABLE station(
    id TEXT PRIMARY KEY,
    lat REAL,
    long REAL,
    title TEXT,
    stationCode TEXT,
    sameAs TEXT,
    operator TEXT,
    context TEXT,
    date TEXT,
    railway TEXT,
    type TEXT
)""")
conn.commit()

# "id": "urn:ucode:_00001C000000000000010000030C471B"
# "lat": 35.7202,
# "long": 139.714715,
# "title": "\u96d1\u53f8\u304c\u8c37",
# "stationCode": "F10",
# "sameAs": "odpt.Station:TokyoMetro.Fukutoshin.Zoshigaya",
# "operator": "odpt.Operator:TokyoMetro",
# "context": "http://vocab.odpt.org/context_odpt.jsonld",
# "date": "2024-03-27T09:00:00+09:00",
# "railway": "odpt.Railway:TokyoMetro.Fukutoshin",
# "type": "Station",

# #単発でデータを挿入
# cur.execute('INSERT INTO items (name , price) VALUES (?,?)',("Orange", 520))
# conn.commit()

# #連続でデータを挿入
# cur = conn.cursor()
# data = [("Mango",770),("Kiwi", 400), ("Grape",800),("Peach",940),("Persimmon",700), ("Banana",400)]
# cur.executemany(
#     "INSERT INTO items (name, price) VALUES (?,?)", data)
# conn.commit()