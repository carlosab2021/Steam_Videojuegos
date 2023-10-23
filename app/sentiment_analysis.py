from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Carga la base de datos con análisis de sentimiento desde el archivo CSV
data = pd.read_csv('base_de_datos_con_sentimiento.csv')

# Ruta para obtener el análisis de sentimiento según el año de lanzamiento
@app.route('/sentiment_analysis/<int:ano>', methods=['GET'])
def sentiment_analysis(ano):
    # Filtra los datos para el año especificado
    filtered_data = data[data['fecha_convertida'].str.contains(str(ano))]

    if filtered_data.empty:
        return jsonify({"message": "No se encontraron datos para el año especificado."}, 404)

    # Realiza el recuento de análisis de sentimiento
    sentiment_counts = filtered_data['sentiment'].value_counts()

    # Convierte el resultado a un diccionario
    result = sentiment_counts.to_dict()

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
