from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Carga la base de datos desde el archivo CSV
data = pd.read_csv('resultado_union_actualizado.csv')

# Ruta para obtener el top 3 de juegos MENOS recomendados por usuarios para un año dado
@app.route('/UsersNotRecommend/<int:ano>', methods=['GET'])
def users_not_recommend(ano):
    # Filtrar los datos para el año especificado
    filtered_data = data[data['fecha_convertida'].str.contains(str(ano))]

    if filtered_data.empty:
        return jsonify({"message": "No se encontraron datos para el año especificado."}, 404)

    # Filtrar solo los juegos con recomendaciones negativas y comentarios negativos
    negative_reviews = filtered_data[(filtered_data['recommend'] == False)]

    # Contar la cantidad de juegos menos recomendados
    game_not_recommend_counts = negative_reviews['item_id'].value_counts().reset_index()
    game_not_recommend_counts.columns = ['item_id', 'NotRecommend_Count']

    # Ordenar los juegos por cantidad de juegos menos recomendados en orden descendente
    top_not_recommend_games = game_not_recommend_counts.sort_values(by='NotRecommend_Count', ascending=False).head(3)

    # Obtener los títulos de los juegos
    game_titles = data[['item_id', 'title']].drop_duplicates()
    top_not_recommend_games = pd.merge(top_not_recommend_games, game_titles, on='item_id')

    # Formatear el resultado en el formato requerido
    resultado = [{"Puesto " + str(i + 1): juego['title']} for i, juego in top_not_recommend_games.iterrows()]

    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
