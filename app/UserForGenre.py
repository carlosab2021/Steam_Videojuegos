from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Carga la base de datos desde el archivo CSV
data = pd.read_csv('resultado_union_actualizado.csv')

# Ruta para obtener el usuario con más horas jugadas y la acumulación por año para un género dado
@app.route('/UserForGenre/<genero>', methods=['GET'])
def user_for_genre(genero):
    genero = genero.strip('[]').strip("'")  # Elimina los corchetes para obtener el género real
    filtered_data = data[data['genres'].str.contains(genero, case=False, na=False)]

    if filtered_data.empty:
        return jsonify({"message": "No se encontraron datos para el género especificado."}, 404)

    # Encuentra el usuario con más horas jugadas para el género
    max_horas_usuario = filtered_data[filtered_data['playtime_forever'] == filtered_data['playtime_forever'].max()]['user_id'].values[0]

    # Obtén el año a partir de una cadena de fecha (ejemplo: "2022-05-15")
    filtered_data['Año'] = filtered_data['fecha_convertida'].str.split('-').str[0]
    
    # Convierte la columna 'Año' a tipo numérico (entero)
    filtered_data['Año'] = filtered_data['Año'].astype(int)

    # Agrupa por 'Año' y calcula la suma de 'playtime_forever'
    acumulacion_por_año = filtered_data.groupby('Año')['playtime_forever'].sum().reset_index()

    # Convierte el resultado a un diccionario en el formato requerido
    resultado = {
        "Usuario con más horas jugadas para " + genero: max_horas_usuario,
        "Horas jugadas": acumulacion_por_año.to_dict(orient='records')
    }

    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)


