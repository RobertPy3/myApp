from flask import Flask, render_template, request
import time

app = Flask(__name__)

frase_1 = '"Hay dos formas de difundir la luz. Ser la vela que la genera o el espejo que la refleja."'
frase_2 = '"Nadie logra cruzar un mar sin mojarse los pies"'
frase_3 = '"Conocí una flor única en el Universo"'
frase_4 = '"La creatividad es la inteligencia jugando"'
frase_5 = '"Es injusto juzgar a una planta por si es comestible o no y en vase a ello amarla o odiarla."'
frase_6 = '"Mala suerte, buena suerte, ¿quién sabe?"'
frase_7 = '"Cortar tu leña te calentará dos veces"'
frase_7 = '"Dos cosas te definen: como eres cuando lo tienes todo\n y como eres cuando no tienes nada"'
frase_8 = '"Las personas subimos a los trenes sin saber a donde nos llevan. Al menos si no sabemos el destino disfrutemos del viaje."'
frase_9 = '"No consideres nunca el estudio como una obligación, considéralo como una oportunidad de penetrar en el maravilloso mundo del saber."'
frase = [frase_1, frase_2, frase_3, frase_4, frase_5, frase_6, frase_7, frase_8, frase_9]

#Estos números sirven para poder darle a frase un x: frase[numero]

i = 7
z = 2
a = 3
b = 8
c = 0
d = 5
e = 1

date = time.strftime('%d_%m_%y')
user = ''
message = ''

@app.route('/')
def index():
    return render_template('index.html', title= 'Welcome', frase = frase[i])

@app.route('/cursos/programacion')
def courses():
    return render_template('cursos_programacion.html', title='Cursos', frase = frase[a])
@app.route('/cursos/comentarios', methods=['POST', 'GET'])
def comentarios():
    user = request.form['user']
    message = request.form['message']
    with open('message/{}.txt'.format(date), "a") as f:
        f.write('\t{}\n\n {}_________________\n\n'.format(user, message))
    return '{} gracias por tu contribución.'.format(user)
@app.route('/blog')
def blog():
    return render_template('blog.html', title = 'Blog', frase = frase[z])


if __name__ == '__main__':
    app.run(debug = True, port = 8000)
