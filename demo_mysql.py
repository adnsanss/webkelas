# export_murid.py
import mysql.connector
import webbrowser
import os
import html

try:
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="web_kelas",
      charset='utf8mb4'
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM murid")
    myresult = mycursor.fetchall()

    # kolom
    kolom = [desc[0] for desc in mycursor.description]

    # mulai buat HTML
    html_content = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Data Murid</title>
<style>
    body { font-family: Arial, sans-serif; padding: 20px; }
    table { border-collapse: collapse; width: 100%; }
    th, td { border: 1px solid #333; padding: 6px; text-align: left; }
    th { background: #f2f2f2; }
</style>
</head>
<body>
<h2>Data murid (dari MySQL)</h2>
<table>
    <thead>
        <tr>"""

    for col in kolom:
        html_content += f"<th>{html.escape(str(col))}</th>"
    html_content += "</tr>\n</thead>\n<tbody>\n"

    for row in myresult:
        html_content += "<tr>"
        for val in row:
            html_content += f"<td>{html.escape(str(val))}</td>"
        html_content += "</tr>\n"

    html_content += """
</tbody>
</table>
</body>
</html>
"""

    filename = "output.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"✅ Data berhasil diexport ke {filename}")

    # buka otomatis di browser default
    path = os.path.realpath(filename)
    webbrowser.open("file://" + path)

except mysql.connector.Error as e:
    print("Error koneksi atau query:", e)


