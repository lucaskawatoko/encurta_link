import pyshorteners

url = "coloque aqui o link que deseja encurtar"
link = pyshorteners.Shortener()
encurta = link.tinyurl.short(url)
print(encurta)
