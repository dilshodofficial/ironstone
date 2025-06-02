import sqlite3 
import pandas as pd

conn = sqlite3.connect("Chinook_Sqlite.db")
customers = pd.read_sql("SELECT CustomerId, FirstName, LastName FROM Customer", conn)
invoices = pd.read_sql("SELECT CustomerId, Total FROM Invoice", conn)
customer_totals = invoices.groupby("CustomerId")["Total"].sum().reset_index()
full = pd.merge(customer_totals, customers, on="CustomerId")
top5 = full.sort_values(by='Total', ascending=False).head(5)
invoice_lines = pd.read_sql("SELECT * FROM InvoiceLine", conn)
tracks = pd.read_sql("SELECT TrackId, AlbumId FROM Track", conn)
invoices = pd.read_sql("SELECT InvoiceId, CustomerId FROM Invoice", conn)
purchases = pd.merge(invoice_lines, tracks, on="TrackId")
purchases = pd.merge(purchases, invoices, on='InvoiceId')
total_albums = purchases.groupby('AlbumId')['TrackId'].count().reset_index()
total_albums.rename(columns={"TrackId": "TracksPurchased"}, inplace=True)
total_tracks_per_album = tracks.groupby("AlbumId")["TrackId"].count().reset_index()
total_tracks_per_album.rename(columns={"TrackId": "TotalTracks"}, inplace=True) 
total_tracks_per_album
customer_albums = pd.merge(total_albums, total_tracks_per_album, on='AlbumId')
customer_albums["BoughtFullAlbum"] = customer_albums["TracksPurchased"] == customer_albums["TotalTracks"]
customer_preferences = customer_albums.groupby("AlbumId")["BoughtFullAlbum"].any().reset_index()
customer_preferences["Preference"] = customer_preferences["BoughtFullAlbum"].apply(
    lambda x: "Full Album" if x else "Individual Tracks"
)
summary = customer_preferences["Preference"].value_counts(normalize=True) * 100

for category, percent in summary.items():
  print(f'{category}: {percent: 2f}%')




