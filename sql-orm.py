from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData,
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship sessionmaker


# executing the instructions from the "chinook" db
db = create_engine("postgresql:///chinook")
base = declarative_base(db)

# create a class-based model for the "Artist" table
class Artist(base):
    __tablename__ = "Artist"

    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

# create a class-based model for the "Album" table
class Album(base):
    __tablename__ = "Album"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# instead of creating the tables manually, we can use the automap_base
# create a new instance of sessionmaker, then point to our engine (the db)
session = sessionmaker(db)()
# opens an actual session by calling the session() subclass defined above
session = session()

# creating the database using delcarative_base subclass
base.metadata.create_all(db)

# Query 1 - select all records from the "Artist" table
artists = session.query(Artist)
for artist in artists:
    print(artist.ArtistID, artist.Name, sep=" | ")