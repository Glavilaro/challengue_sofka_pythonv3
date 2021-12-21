
from utils import randomize


class Preguntas:

    def __init__(self, categoria, pregunta, respuesta, op1, op2, op3):
        self.category = categoria
        self.question = pregunta
        self.answer = respuesta
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3


    @property
    def category(self):
        return self.__categoria

    @category.setter
    def category(self, valor):
        self.__categoria = valor

    @property
    def question(self):
        return self.__preguntas

    @question.setter
    def question(self, valor):
        self.__preguntas = valor

    @property
    def answer(self):
        return self.__respuestas

    @answer.setter
    def answer(self, valor):
        self.__respuestas = valor

    @property
    def op1(self):
        return self.__op1

    @op1.setter
    def op1(self, valor):
        self.__op1 = valor

    @property
    def op2(self):
        return self.__op2

    @op2.setter
    def op2(self, valor):
        self.__op2 = valor

    @property
    def op3(self):
        return self.__op3

    @op3.setter
    def op3(self, valor):
        self.__op3 = valor

    def toString(self):
        return (self.category, self.question, self.answer,
                self.op1, self.op2, self.op3)

    def display_question(self):


        print(self.question)
        print("")

    def randomize_answers(self):

        opciones = [self.answer, self.op1, self.op2, self.op3]
        new_order = randomize(opciones)
        random_opciones = {
            "A": new_order[0],
            "B": new_order[1],
            "C": new_order[2],
            "D": new_order[3]
        }
        return random_opciones

    def display_options(self, diccionario):

        for key, value in diccionario.items():
            print(f"{key}: {value}")
        print("")

    def verify_answer(self, opciones):

        return self.answer == opciones
