serie = "N-02"

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe")

cliente = { "nombre": "Bruce",
            "edad": 25,
            "ocupacion": "programador" }

pelicula = {"titulo": "John Wick",
            "ficha_tecnica": { "protagonista": "Keanu Reevs",
                            "director": "Chad Stahelski" }}

elementos = [cliente, pelicula, "comic"]

for e in elementos:
    match e:
        case {
            "nombre": nombre,
            "edad": edad,
            "ocupacion": ocupacion
        }:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case {
            "titulo": titulo,
            "ficha_tecnica": {
                "protagonista": protagonista,
                "director": director
            }
        }:
            print("Es una pelicula")
            print(titulo, director, protagonista)
        case _:
            print("No se que es esto")