import zipfile

with zipfile.ZipFile("logs.zip","w") as zipf:
    zipf.write(app.log)
