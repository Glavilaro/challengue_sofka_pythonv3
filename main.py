from jugador import jugador
from pregunta_banco import banco
from utils import welcome, save_score, display_top_scores

preguntas_db = banco()
categories_list = preguntas_db.randomize_categories()

actual_jugador = jugador(welcome(), 0)
actual_ronda = 1
succeded = []

for category in categories_list:
    print(f"Ronda {actual_ronda}: {category}")
    actual_pregunta = preguntas_db.select_question(category, actual_ronda)
    actual_pregunta.display_question()
    opciones = actual_pregunta.randomize_answers()
    actual_pregunta.display_options(opciones)
    user_opcion = preguntas_db.prompt_option()
    if actual_pregunta.verify_answer(opciones[user_opcion]):
        print("¡excelente! continuas en la siguente ronda.")
        succeded.append(category)
        round_puntos = actual_ronda * 10
        actual_jugador.update_score(round_puntos)
        print(f"Ganaste {round_puntos} puntos.", "\n")
        actual_ronda += 1
        if actual_ronda < 5:
            siguiente_pregunta = preguntas_db.prompt_continue()
            if siguiente_pregunta == "N":
                break
    else:
        print("¡perdiste! Esa no era la respuesta correcta.", "\n")
        actual_jugador.clear_score()
        break

preguntas_db.display_result(actual_jugador.name, actual_jugador.score, succeded)
save_score(actual_jugador.name, actual_ronda - 1, actual_jugador.score)
display_top_scores()
