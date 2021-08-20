from tkinter.filedialog import askopenfilename
alumnos = ''
alumnos1 = ''
alumnos2 = ''
alumnos3 = ''
alumnos4 = ''
alumnos5 = ''
alumnos6 = ''
nombreCurso = ''
parametros = ''
listaoriginal = ''
listaASC = ''
listaDESC = ''
listareprob = ''
listaaprob = ''
listapromedio = ''
contenidoparametros = ''
sumanotas = 0
promedio = ''
aprobados = 0
reprobados = 0
totalreprobados = ''
totalaprobados = ''
totalpromedio = ''
notaminima = ''
notamaxima = ''

def leer(ruta):
    archivo = open(ruta, "r", encoding='utf-8')
    contenido = archivo.read().replace("<","").replace(">","").replace('"',"")
    archivo.close
    global nombreCurso
    global parametros
    global prueba
    lista1 = contenido.split("=")
    nombreCurso = lista1[0]
    listaparametro = contenido.split('}')
    parametros = listaparametro[1]
    prueba = parametros
    return contenido

def escribirArchivo(ruta, contenido):
    archivo = open(ruta, 'w')
    archivo.write(contenido)
    archivo.close()    
    

def cargar():
    global alumnos
    global listaoriginal
    global listaASC
    global listaDESC
    global listareprob
    global listaaprob
    global listapromedio
    filename = askopenfilename()
    codigo = leer(filename)
    nombreCurso = ''
    for c in codigo:
        if c == '=':
            break
        else:
            nombreCurso += c    
 
    txtEstudiantes = ''
    bandera = False
    for c in codigo:
        if c == '{':
            bandera = True
            continue
        if c != '}' and bandera:
            txtEstudiantes += c            
        elif c == '}':
            break    

        
    contenidoestudiantes = ''
    bandera = False
    for c in codigo:
        if c == '<':
            bandera = True
            continue
        if c!= '>' and bandera:
            contenidoestudiantes += c
        if c == '>':
            continue
        elif c == '}':
            break

    global contenidoparametros
    contenidoparametros = ''    
    bandera = False
    for c in codigo:
        if c == '}':
            bandera = True    
            continue
        if c!= ',' and bandera:
            contenidoparametros += c

    print("Se ha cargado con exito el archivo")
       
    lineas = splitear(txtEstudiantes, ',')
    alumnos = getEstudiantes(lineas)
    alumnos1 = getEstudiantes(lineas)
    alumnos2 = getEstudiantes(lineas)
    alumnos3 = getEstudiantes(lineas)
    alumnos4 = getEstudiantes(lineas)
    alumnos5 = getEstudiantes(lineas)
    alumnos6 = getEstudiantes(lineas)
    listaoriginal = alumnos5
    listaASC = alumnos1    
    listaDESC = alumnos2
    listareprob = alumnos3
    listaaprob = alumnos4
    listapromedio = alumnos6
    print("")

    
        

def splitear(cadena, caracter):
    temporal = ""
    listaTemporal = []
    for i in cadena:
        if i == caracter:
            listaTemporal.append(temporal.strip())
            temporal = ""
        else:
            temporal += i
    if temporal.strip() != "":
        listaTemporal.append(temporal.strip())
    return listaTemporal


def getEstudiantes(listaSucia):
    listaNueva = []
    for linea in listaSucia:
        datos = splitear(linea,';') 
        nombre = datos[0]
        nota = int(datos[1])
        alumno = {"nombre": nombre, "nota": nota}
        listaNueva.append(alumno)
    return listaNueva

def getParametro():
    
    if 'ASC' in contenidoparametros:
             print("Ordenado Ascendente")
             ordenarAscendentemente(listaASC)
    for a in listaASC:                
                print("Nombre:", a['nombre'], "Nota:", a['nota'])
                print("")
            
    if 'DESC' in contenidoparametros:
            print("Ordenado descendente")
            ordenarDescendentemente(listaDESC)
            for a in listaDESC:
                print("Nombre:", a['nombre'], "Nota:", a['nota'])      
                print("") 
            
    if 'APR' in contenidoparametros:
            print("Lista Aprobados")
            global aprobados
            global totalaprobados
            aprobados = 0
            for a in alumnos:
                if a['nota'] >= 61:
                    aprobados += 1
            print("Aprobados: " , aprobados)
            totalaprobados = aprobados    
            print("")    
    if 'REP' in contenidoparametros:
            print("Lista Reprobados")
            global reprobados
            global totalreprobados
            reprobados = 0
            for a in listareprob:
                if a['nota'] < 61:
                    reprobados += 1     
            print("Reprobados: " , reprobados) 
            totalreprobados = reprobados
            print("")

    if 'AVG' in contenidoparametros:
            print("Promedio")
            global sumanotas
            global promedio
            sumanotas = 0

            for a in alumnos:
                sumanotas += int(a['nota'])
            print('Suma :', sumanotas)
            print("Total datos", len(alumnos))
            promedio = sumanotas/float(len(alumnos))
            print("Promedio es :", promedio)
            print("")
    
    if 'MIN' in contenidoparametros:
            global notaminima
            print("Nota minima")
            obtenerminimo(alumnos)
            for a in alumnos:
                print("Nombre:", a['nombre'], "Nota:", a['nota'])    
                break
            notaminima = 'Nombre:', a['nombre'], 'Nota:', a['nota']
            print("")     
            
    if 'MAX' in contenidoparametros:
            global notamaxima
            print("Nota maxima")
            obtenermaximo(alumnos)
            for a in alumnos:
                notamaxima = "Nombre:", a['nombre'], "Nota:", a['nota']
                print("Nombre:", a['nombre'], "Nota:", a['nota'])
                break  
                
            print("")  

      
            
def ordenarAscendentemente(lista):
    i = 0
    while i < len(lista) - 1:
        j = 0
        while j < len(lista) - 1:
            if lista[j]['nota'] > lista[j+1]['nota']:
                aux = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = aux
            j+=1
        i+=1

def ordenarDescendentemente(lista):
    i = 0
    while i < len(lista) - 1:
        j = 0
        while j < len(lista) - 1:
            if lista[j]['nota'] < lista[j+1]['nota']:
                aux = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = aux
            j+=1
        i+=1

def obtenerminimo(lista):
    i = 0
    while i < len(lista) - 1:
        j = 0
        while j < len(lista) - 1:
            if lista[j]['nota'] > lista[j+1]['nota']:
                aux = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = aux
            j+=1
        i+=1 
            

def obtenermaximo(lista):
    i = 0
    while i < len(lista) - 1:
        j = 0
        while j < len(lista) - 1:
            if lista[j]['nota'] < lista[j+1]['nota']:
                aux = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = aux
            j+=1
        i+=1     
             
def getHtmloriginal(lista):
    inicio = '<!DOCTYPE html><html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Original</title>' + '<center><h1>' + nombreCurso + '</h1></center>' + '</head><body background = ''http://blog.aulaformativa.com/wp-content/uploads/2016/06/fondos-de-pantalla-para-programadores-CodeWallpaper3.jpg''><center><table border=\"1\">'
    fin = '</table><h3>Parámetro: Original</h3></body></html>'
    for a in lista:
        inicio +=  "<tr><th>Nombre</th><th>Nota </th></tr><tr><td>" + a['nombre'] + "</td><td>" 
        if int(a['nota']) >= 61:
            inicio += '<td bgcolor = "blue">' + str(a['nota']) + "</td>"
        else:
            inicio += '<td bgcolor = "red">' + str(a['nota']) + "</td>"
        str(a['nota']) + "</td></tr></center>" 
    return inicio + fin
        

def getHtml(lista):
    inicio = '<!DOCTYPE html><html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Ordenamiento Ascendente</title>' + '<center><h1>' + nombreCurso + '</h1></center>' + '</head><body background = ''http://blog.aulaformativa.com/wp-content/uploads/2016/06/fondos-de-pantalla-para-programadores-CodeWallpaper3.jpg''><center><table border=\"1\">'
    fin = '</table><h3>Parámetro: ASC (Ascendente)</h3></body></html>'
    for a in lista:
        inicio +=  "<tr><th>Nombre </th>" + "<th >Nota </th></tr>" + "<tr><td>" + a['nombre'] + "</td>" + "<td>" + str(a['nota']) + "</td></tr></center>" 
        
    return inicio + fin     

def getHtml1(lista):
    inicio = '<!DOCTYPE html><html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Ordenamiento Descendente</title>' + '<center><h1>' + nombreCurso + '</h1></center>' + '</head><body background = ''http://blog.aulaformativa.com/wp-content/uploads/2016/06/fondos-de-pantalla-para-programadores-CodeWallpaper3.jpg''><center><table border=\"1\">'
    fin = '</table><h3>Parámetro: DESC (Descendente)</h3></body></html>'
    for a in lista:
        inicio +=  "<tr><th>Nombre </th>" + "<th >Nota </th></tr>" + "<tr><td>" + a['nombre'] + "</td>" + "<td>" + str(a['nota']) + "</td></tr></center>" 
    return inicio + fin     

def getHtmlreprobados(lista):
    inicio = '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"><title>Reprobados</title></head><body background = ''http://blog.aulaformativa.com/wp-content/uploads/2016/06/fondos-de-pantalla-para-programadores-CodeWallpaper3.jpg''>'+ '<center><h1>' + nombreCurso + '</h1></center>' + '<center><h2> Estudiantes reprobados: ' + str(reprobados)   + '</h2></center>'
    final = '<center><h2>Parámetro: REP (Reprobados)</h2></center></body></html>' 
    return inicio + final

def getHtmlaprobados(lista):
    inicio = '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"><title>Aprobados</title></head><body background=''http://blog.aulaformativa.com/wp-content/uploads/2016/06/fondos-de-pantalla-para-programadores-CodeWallpaper3.jpg''>'+ '<center><h1>' + nombreCurso + '</h1></center>' + '<center><h2> Estudiantes Aprobados: ' + str(aprobados)   + '</h2></center>'
    final = '<center><h2>Parámetro: APR (Aprobados)</h2></center></body></html>' 
    return inicio + final

def getMaximo(lista):
    inicio = '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"><title>Maximo</title></head><body background=''http://blog.aulaformativa.com/wp-content/uploads/2016/06/fondos-de-pantalla-para-programadores-CodeWallpaper3.jpg'' >' + '<center><h1>' + nombreCurso + '</h1></center>' + '<h2><center>Nota máxima </h2></center>' + '<h3><center>' + str(notamaxima) + '</h3></center>'
    fin = '<center><h2>Parámetro: MAX (Máximo)</h2></center></body></html>'
    return inicio + fin
    
def getMinimo(lista):
    inicio = '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"> <title>Minimo</title></head><body background=''http://blog.aulaformativa.com/wp-content/uploads/2016/06/fondos-de-pantalla-para-programadores-CodeWallpaper3.jpg'' >' + '<center><h1>' + nombreCurso + '</h1></center>' + '<h2><center>Nota mínima </h2></center>' + '<h3><center>' + str(notaminima) + '</h3></center>'
    fin = '<center><h2>Parámetro: MIN (Mínimo)</h2></center></body></html>'
    return inicio + fin 

def getHtmlpromedio(lista):
    inicio = '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"><title>Promedio</title></head><body background=''http://blog.aulaformativa.com/wp-content/uploads/2016/06/fondos-de-pantalla-para-programadores-CodeWallpaper3.jpg''>'+ '<center><h1>' + nombreCurso + '</h1></center>' + '<center><h2> Promedio es: ' + str(promedio)   + '</h2></center>'
    final = '<center><h2>Parámetro: AVG (Promedio)</h2></center></body></html>' 
    return inicio + final       
    
    
def menu():
    opcion = ''
   
    while opcion != '4':
        print('------------ Menu --------------')
        print('1. Cargar Archivo')
        print('2. Mostrar Reportes')
        print('3. Exportar Reportes')
        print('4. Salir')
        opcion = input('Ingrese una opción: ')
        if opcion == '1':
            cargar()
        elif opcion == '2':
            print("Mostrar reportes" + "\n")
            print('Curso: ',nombreCurso)
            print("Total de estudiantes asignados: " +  str(len(alumnos)) + "\n")
            print("Orden Original")
            for a in alumnos:
                print("Nombre:", a['nombre'], "Nota:", a['nota'])
                print("")

            getParametro()        
        
        elif opcion == '3':
            print("Se han generado exitosamente los reportes")
            
            cadenaoriginal = getHtmloriginal(listaoriginal)
            escribirArchivo('Desordenado.html', cadenaoriginal)

            cadenaHtml = getHtml(listaASC)
            escribirArchivo('Ascendente.html', cadenaHtml) 

            cadenaHtml1 = getHtml1(listaDESC)
            escribirArchivo('Descendente.html', cadenaHtml1) 

            cadenaHtml2 = getHtmlreprobados(totalreprobados)
            escribirArchivo('Reprobados.html', cadenaHtml2)

            cadenaHtml3 = getHtmlaprobados(totalaprobados)
            escribirArchivo('Aprobados.html', cadenaHtml3)

            htmlmaximo = getMaximo(alumnos)
            escribirArchivo('Maximo.html', htmlmaximo)

            htmlminimo = getMinimo(alumnos)
            escribirArchivo('Minimo.html', htmlminimo)

            htmlpromedio = getHtmlpromedio(alumnos)
            escribirArchivo('Promedio.html', htmlpromedio)
      
        elif opcion != "4":
            print("Ingrese una opcion correcta")
            
        else:
            print("Gracias por usar el programa :D")
            break
menu()











