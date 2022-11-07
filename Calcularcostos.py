import webbrowser


print (''' Para calcular el costo del trabajo de proyectos de cualquiera de programacion se hace lo siguiente   ''')

print (''' Primero haz una aproximacion de lineas de codigo
supongamos 10,000 lineas de codigo agregar ese valor   ''')

print("Ingresa el valor: ")

valor1= float(input())


print("Inngresa el valor de las lineas de codigo que haras por hora")

valor2 = float(input())


resultado = valor1 / valor2

print("Esta son las horas que se desarrollaran  ",resultado )

print ("Despues se realizara la division con los dias que te dieron de plazo pon los dias de plazo")

dias= float(input("Ingresa los dias... "))

mostrar = dias / resultado

print ("Esta son las horas de trabajo que tendras que trabajar diariamente  " ,mostrar)

print ("Investiga cuanta gana un desarrollador en el lenguaje que estas usando , La pagina esta es solo como referencia")

webbrowser.open("https://www.google.com/search?q=cuanto+cobrar+por+hora+programador+ecuador&sxsrf=ALiCzsZHA3FkXq7zpVp3uFBMFDKgiIqEdg%3A1667855342430&ei=7nNpY73WGfrbwbkPjqCKkA0&oq=cuanto+cobrar+por+hora+programador+ec&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgAMgUIIRCgATIFCCEQoAEyBQghEKABOgoIABBHENYEELADOgYIABAWEB46CAghEBYQHhAdSgQITRgBSgQIQRgASgQIRhgAUOQDWNkGYLEMaAFwAXgAgAHHAYgBrASSAQMwLjOYAQCgAQHIAQjAAQE&sclient=gws-wiz-serp", new=2, autoraise=True)

horas =float(input("Ingresa las horas : "))
horas2 = horas * mostrar


print ("No olvidarse de los costos externos que habria que agregar")


costos = float(input("Costos : "))

suma =costos + horas2

print ("Esto seria el total de lo que tendrias que cobrar " , suma)






