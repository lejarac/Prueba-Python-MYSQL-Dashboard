import mysql.connector
import matplotlib.pyplot as plt
from flask import Flask, render_template
import io
import base64

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='PErumundial123!!',
        database='dashboard_db'
    )

def get_colaboradores():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM colaboradores")
    colaboradores = cursor.fetchall()
    cursor.close()
    connection.close()
    return colaboradores

def generate_bar_chart(colaboradores):
    edades = [e[2] for e in colaboradores]
    salarios = [e[4] for e in colaboradores]
    plt.figure(figsize=(10,5))
    plt.bar(edades, salarios)
    plt.xlabel('Edad')
    plt.ylabel('Salario')
    plt.title('Relación entre Edad y Salario')
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode()

def generate_pie_chart(colaboradores):
    ciudades = [e[3] for e in colaboradores]
    ciudad_count = {ciudad: ciudades.count(ciudad) for ciudad in set(ciudades)}
    plt.figure(figsize=(8,8))
    plt.pie(ciudad_count.values(), labels=ciudad_count.keys(), autopct='%1.1f%%')
    plt.title('Distribución de Colaboradores por Ciudad')
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode()

@app.route('/')
def dashboard():
    colaboradores = get_colaboradores()
    bar_chart = generate_bar_chart(colaboradores)
    pie_chart = generate_pie_chart(colaboradores)
    return render_template('01.dashboard.html', colaboradores=colaboradores, bar_chart=bar_chart, pie_chart=pie_chart)

if __name__ == '__main__':
    app.run(debug=True)