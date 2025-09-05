import mysql.connector
import webbrowser
import os

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database= "web_kelas"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM murid")

myresult = mycursor.fetchall()

kolom = [desc[0] for desc in mycursor.description]

html = """
<html>
<head>
    <title>Data MySQL</title>
    <style>
        table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
            padding: 6px;
        }
    </style>
</head>
<body>
    <h2>Data dari MySQL</h2>
    <table>
        <tr>
"""

for col in kolom:
    html += f"<th>{col} </th>"
html += "</tr>"


for row in myresult:
    html += "<tr>"
    for val in row:
        html += f"<td> {val}</td>"
    html += "</tr>"

html += """
</table>
</body>
</html>
"""

filename = "output.html"
with open(filename, "w", encoding="utf-8") as f:
    f.write(html)

# Tutup koneksi
mycursor.close()
mydb.close()

print("✅ Data berhasil diexport ke output.html")

# Buka otomatis di browser default
webbrowser.open("file://" + os.path.realpath)
