
from preguntas import Preguntas
from utils import randomize, verify_option


class banco:
    def __init__(self) -> object:

        self.categorias = ["musica", "deportes", "Ciencia",
                           "Historia", "geografia"]
        self.rank1 = {
            0: Preguntas(self.categorias[0],
                        "¿en que año nacio la cantante colombiana shakira?",
                        "1977", "2001","1989","1907"),
            1: Preguntas(self.categorias[1],
                        "¿Cuántos balones de oro tiene lionel messi?", "5", "6", "7",
                        "4"),
            2: Preguntas(self.categorias[2],
                        "¿En qué año comenzo la primera guerra mundial?","1935","1914","1918","1976"),
            3: Preguntas(self.categorias[3],
                         "¿cual de los siguientes animales es considerado el rey de la selva?","leon", "pantera", "elefante","tigre"),
            4: Preguntas(self.categorias[4],
                        "¿en que continente se encuetra la ciudad de angola ?", "africano", "asiatico", "antartico", "europeo")
        }
        self.rank2 = {
            0: Preguntas(self.categorias[0],
                        "¿cuantos años tiene luis miguel?",
                     "51", "75", "60",
                        "49"),
            1: Preguntas(self.categorias[1],
                        "¿cual es el actual tenista numero uno en el ranking mundial?", "novak djokovic",
                        "dominic tiem", "roger federer", "rafael nadal"),
            2: Preguntas(self.categorias[2],
                         "¿de que nacionalidad era juana de arco?","francesa","italiana","japonesa","argentina"),
            3: Preguntas(self.categorias[3],
                        "¿como se denomina la parte del cuerpo donde se juntan dos o mas huesos ?", "articulaciones",
                        "tendones", "cartilago", "extremidades"),
            4: Preguntas(self.categorias[4],
                        "¿cual es el nombre del desierto de mexico",
                        "sonora", "saara", "ankara", "salinas")
        }
        self.rank3 = {
            0: Preguntas(self.categorias[0],
                        "¿cual era la nacionalidad de carlos gardel?",
                        "uruguayo","chileno","argentino","paraguayo"),
            1: Preguntas(self.categorias[1],
                        "¿cuanto dura un partido de futbol?","90 min","60 min","2 hs","30 min"),
            2: Preguntas(self.categorias[2],
                         "¿en que año finalizo la segunda guerra mundial?","1945","2011","1975","1810"),
            3: Preguntas(self.categorias[3],
                        "¿que planeta es el mas cercano al sol?","mercurio","tierra","pluton","venus"),
            4: Preguntas(self.categorias[4],
                       "¿cuantas provincias tiene la republica argentina?","23","26","30","28"),
        }
        self.rank4 = {
            0: Preguntas(self.categorias[0],
                        "¿cual era la nacionalidad del cautantor victor jara?","chileno","frances","boliviano","español"),
            1: Preguntas(self.categorias[1],
                       "¿en que año debuto Diego Armando Maradona en primera division?","1976","1960","1953","1963"),
            2: Preguntas(self.categorias[2],
                        "¿a que monstruo mitico vencio teseo?","minotauro","hefesto","hades","poseidon"),
            3: Preguntas(self.categorias[3],
                        "¿en que año se creo la primer computadora?","1941","1970","1914","1969"),
            4: Preguntas(self.categorias[4],
                        "¿cuantos son los planetas reconocidos del sistema solar?","8","6","12","7"),
        }
        self.rank5 = {
            0: Preguntas(self.categorias[0],
                        "¿como se denomina al subgenero musical del rap que mezcla rap,hip hop y dubstep?","trap","reggueaton","reggue","chamame"),
            1: Preguntas(self.categorias[1],
                         "¿cuantas perdonas conforman un equipo de basquet?", "cinco", "once", "seis", "ocho"),
            2: Preguntas(self.categorias[2],
                         "¿en que año sucedio el atentado a las torres gemelas?","2011","2012","2001","2016"),
            3: Preguntas(self.categorias[3],
                        "¿cuantos elementos componen la tabla periodica?","118","116","200","198"),
            4: Preguntas(self.categorias[4],
                        "¿donde deberia visitar el taj mahal?","la india","california","machu pichu","antigua y barbuda"),
        }

    def randomize_categories(self):

        random_categorias = randomize(self.categorias)
        return random_categorias

    def select_question(self, categoria, actual_round):

        def __check_category(rank, categoria):

            for key in rank:
                if rank[key].category == categoria:
                    return rank[key]

        if actual_round == 1:
            ranking = self.rank1
            selected_category = __check_category(ranking, categoria)
        elif actual_round == 2:
            ranking = self.rank2
            selected_category = __check_category(ranking, categoria)
        elif actual_round == 3:
            ranking = self.rank3
            selected_category = __check_category(ranking, categoria)
        elif actual_round == 4:
            ranking = self.rank4
            selected_category = __check_category(ranking, categoria)
        elif actual_round == 5:
            ranking = self.rank5
            selected_category = __check_category(ranking, categoria)
        return selected_category

    def prompt_option(self):
        valid_options = ["A", "B", "C", "D"]
        user_option = input("¿Qué opción eliges? ").upper()
        while True:
            check = verify_option(valid_options, user_option)
            if not check:
                user_option = input("¡Elige una opción válida! ").upper()
            else:
                print("")
                return user_option

    def prompt_continue(self):
        valid_options = ["S", "N"]
        siguiente_pregunta = input(
            "¿Deseas continuar con la próxima pregunta?(S/N) ").upper()
        while True:
            check = verify_option(valid_options, siguiente_pregunta)
            if not check:
                siguiente_pregunta = input(
                    "Por favor indícanos si deseas continuar(S/N) ").upper()
            else:
                print("")
                return siguiente_pregunta

    def display_result(self, nombre, puntaje, categorias):
        length = len(categorias)
        print(f"{nombre} lograste {puntaje} puntos")
        if length > 0:
            print(f"Acertaste {length} categoría(s):")
            for categorias in categorias:
                print(">", categorias)
        else:
            print("¡Sigue esforzandote para ganar!")
        if length == 5:
            print("\n" + "¡Felicitaciones, completaste el juego!")