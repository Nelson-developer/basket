from flask import Blueprint, render_template, jsonify
from flask_graphql import GraphQLView
from bson.objectid import ObjectId
import graphene
from pymongo import MongoClient

graph_todo = Blueprint('graph_todo', __name__)

# conectando a mongodb
client = MongoClient('mongodb://localhost:27017')

# nombre de la base de datos
db = client['basket']
equipos = db['equipos']
partidos = db['partidos']


class Jugador(graphene.ObjectType):
    _id = graphene.ID()
    nombre = graphene.String()
    posicion = graphene.String()
    imagen = graphene.String()
    puntos = graphene.Int()
    asistencia = graphene.Int()
    rebotes = graphene.Int()
    tapas = graphene.Int()
    estado = graphene.String()
    edad = graphene.Int()
    altura = graphene.Int()


class Equipo(graphene.ObjectType):
    _id = graphene.ID()
    nombreEquipo = graphene.String(required=True)
    entrenador = graphene.String(required=True)
    categoria = graphene.String(required=True)
    logo = graphene.String()
    jugadores = graphene.List(Jugador)


class Puntos(graphene.ObjectType):
    equipoCasa = graphene.Int()
    equipoVisitante = graphene.Int()


class Partido(graphene.ObjectType):
    _id = graphene.ID()
    equipoVisitante = graphene.List(Equipo)
    equipoCasa = graphene.List(Equipo)
    Tiempo1 = graphene.Field(Puntos)
    Tiempo2 = graphene.Field(Puntos)
    Tiempo3 = graphene.Field(Puntos)
    Tiempo4 = graphene.Field(Puntos)
    Tiempo5 = graphene.Field(Puntos)
    lugar = graphene.String()
    HoradeInicio = graphene.String()
    HoradeFinalizado = graphene.String()


class JugadorRespuesta(graphene.ObjectType):
    _id = graphene.ID()
    jugadores = graphene.List(Jugador)

class Query(graphene.ObjectType):
    hello = graphene.String()
    equipos = graphene.List(Equipo)
    partidos = graphene.List(Partido)
    EquiposPorCategoria = graphene.List(Equipo, categoria=graphene.String())
    EquipoJugadores = graphene.List(Equipo, _id=graphene.ID())
    UnJugador = graphene.List(JugadorRespuesta, idjugador=graphene.ID())

    def resolve_equipos(self, info):
        data = equipos.find()
        print(data)
        return data

    def resolve_partidos(self,info,*args, **kwargs):
        data = partidos.find()
        print(data)
        return data

    def resolve_EquiposPorCategoria(self,info,categoria):
        data = equipos.find({"categoria": str(categoria)})
        print(data)
        return data
    def resolve_EquipoJugadores(self,info,_id):
        data = equipos.find({"_id": ObjectId(str(_id))})
        print(data)
        return data
    def resolve_UnJugador(self,info,idjugador):
        data = equipos.find({"jugadores._id": ObjectId(str(idjugador))}, { "jugadores.$" : True})
        print(data)
        return data

# mutations


class SaveEquipo(graphene.Mutation):
    class Arguments:
        nombreEquipo = graphene.String()
        entrenador = graphene.String()
        categoria = graphene.String()
        logo = graphene.String()

    ok = graphene.Boolean()
    @staticmethod
    def mutate(self, root, nombreEquipo, entrenador, categoria, logo):
        data = {"nombreEquipo": nombreEquipo, "entrenador": entrenador,"categoria": categoria, "logo": logo,}
        equipos.insert_one(data)  # guardando en mongodb
        ok = True
        return SaveEquipo(ok = ok)

class SaveJugador(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        nombreJugador = graphene.String()
        posicion = graphene.String()
        imagen = graphene.String()
        edad = graphene.Int()
        altura = graphene.Int()
    
    ok = graphene.Boolean()
    
    def mutate(self, root, id, nombreJugador, posicion, imagen, edad, altura):
        data = {"_id": ObjectId(), "nombre": nombreJugador, "posicion": posicion, "imagen": imagen, "edad": edad, "altura": altura, "puntos": 0, "asistencia": 0, "tapas": 0, "estado": "activo", "rebotes": 0}
        equipos.update({"_id": ObjectId(str(id))},{"$push": {"jugadores": data}})  # guardando en mongodb
        ok = True
        return SaveJugador(ok = ok)


class SavePartido(graphene.Mutation):
    class Arguments:
        idCasa = graphene.ID()
        idVisitante = graphene.ID()
        lugar = graphene.String()

    ok = graphene.Boolean()
    
    def mutate(self, root,idCasa, idVisitante, lugar):
        equipo_casa = equipos.find_one({"_id": ObjectId(str(idCasa))})
        equipo_visitante = equipos.find_one({"_id": ObjectId(str(idVisitante))})
        data = {"equipoVisitante": [equipo_visitante],"equipoCasa": [equipo_casa], "lugar": lugar}
        partidos.insert(data)
        ok = True
        return SavePartido(ok=ok)



class Mutation(graphene.ObjectType):
    save_equipo = SaveEquipo.Field()
    save_jugador = SaveJugador.Field()
    save_partido = SavePartido.Field()
    

schema = graphene.Schema(query=Query,  mutation=Mutation)

schema.execute('''
  query {
    hello
  }
''')


graph_todo.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

