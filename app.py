from flask import Flask, render_template, request

app = Flask(__name__)

#-- Ruta del menú principal --
@app.route('/')
def home():
    return render_template('index.html')

#-- Ruta para el ejercicio 1 --
@app.route('/ejercicio1', methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        numero1 = int(request.form["num1"])
        numero2 = int(request.form["num2"])
        numero3 = int(request.form["num3"])
        asistencia = int(request.form["Asistencia"])
        promedio = (numero1 + numero2 + numero3) / 3
        aprobado = promedio >= 40 and asistencia >= 75
        resultado = "Aprobado" if aprobado else "Reprobado"
        return render_template("Pagina1.html",
                               nom=resultado,
                               promedio=round(promedio, 1),
                               nota1=numero1,
                               nota2=numero2,
                               nota3=numero3,
                               asistencia=asistencia)
    return render_template("Pagina1.html")

#-- Ruta para el ejercicio 2 --
@app.route('/ejercicio2', methods=["GET", "POST"])
def ejercicio2():
    if request.method == "POST":
        nombre1 = request.form["nombre1"]
        nombre2 = request.form["nombre2"]
        nombre3 = request.form["nombre3"]

        nombres = [nombre1, nombre2, nombre3]
        nombre_mas_largo = max(nombres, key=len)
        cantidad_caracteres = len(nombre_mas_largo)

        return render_template("Pagina2.html",
                               nombre1=nombre1,
                               nombre2=nombre2,
                               nombre3=nombre3,
                               largo=nombre_mas_largo,
                               cantidad=cantidad_caracteres)

    return render_template("Pagina2.html")

if __name__ == '__main__':
    app.run(debug=True)


