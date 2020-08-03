from app import db, create_app
from app.public.models import Categoria, Pregunta, Respuesta
from app.auth.models import User, Role

app = create_app()
app.app_context().push()

db.drop_all()
db.create_all()

# categorias
c_geogra = Categoria(descripcion="Geografía")
c_deporte = Categoria(descripcion="Deportes")
c_histo = Categoria(descripcion="Historia")
c_arte = Categoria(descripcion="Arte")

# preguntas
q_Laos = Pregunta(text="¿Cuál es la capital de Laos?", categoria = c_geogra)
q_Armenia = Pregunta(text="¿Cuál es la población aproximada de Armenia?", categoria = c_geogra)
q_mundial = Pregunta(text="¿En qué país se jugó la Copa del Mundo de 1962?", categoria = c_deporte)
q_guerra = Pregunta(text="¿En qué año fue la batalla de Las Piedras?", categoria = c_histo)
q_pintura = Pregunta(text="¿Quien pinto la Capilla Sixtina?", categoria = c_arte)


# respuestas
r_Laos1 = Respuesta(text="Vientian", correct=True, pregunta = q_Laos)
r_Laos2 = Respuesta(text="Viena", correct=False, pregunta = q_Laos)
r_Laos3 = Respuesta(text="Paris", correct=False, pregunta = q_Laos)
r_Armenia1 = Respuesta(text="2 millones", correct=False, pregunta = q_Armenia)
r_Armenia2 = Respuesta(text="3 millones", correct=True, pregunta = q_Armenia)
r_Armenia3 = Respuesta(text="4 millones", correct=False, pregunta = q_Armenia)
r_mundial1 = Respuesta(text="Chile", correct=True, pregunta = q_mundial)
r_mundial2 = Respuesta(text="Inglaterra", correct=False, pregunta = q_mundial)
r_mundial3 = Respuesta(text="Alemania", correct=False, pregunta = q_mundial)
r_guerra1 = Respuesta(text="1811", correct=True, pregunta = q_guerra)
r_guerra2 = Respuesta(text="1817", correct=False, pregunta = q_guerra)
r_guerra3 = Respuesta(text="1830", correct=False, pregunta = q_guerra)
r_pintura1 = Respuesta(text="Vincent van Gogh", correct=False, pregunta = q_pintura)
r_pintura2 = Respuesta(text="Miguel Ángel", correct=True, pregunta = q_pintura)
r_pintura3 = Respuesta(text="Leonardo da Vinci", correct=False, pregunta = q_pintura)



#Usuarios
u1 = User(name="Fede", email="fede@gmail.com")
# el pass lo seteamos con el método set_password para que se guarde con hash
u1.set_password("1234");
# por defecto, el usuario no es admin
u2 = User(name="Fede2", email="fede2@gmail.com")
u2.set_password("12345");
u3 = User(name="Fede3", email="fede3@gmail.com")
u3.set_password("123456");


db.session.add(c_geogra)
db.session.add(c_deporte)
db.session.add(c_histo)
db.session.add(c_arte)
db.session.add(q_Laos)
db.session.add(q_Armenia)
db.session.add(q_mundial)
db.session.add(q_guerra)
db.session.add(q_pintura)
db.session.add(r_Laos1)
db.session.add(r_Laos2)
db.session.add(r_Laos3)
db.session.add(r_Armenia1)
db.session.add(r_Armenia2)
db.session.add(r_Armenia3)
db.session.add(r_mundial1)
db.session.add(r_mundial2)
db.session.add(r_mundial3)
db.session.add(r_guerra1)
db.session.add(r_guerra2)
db.session.add(r_guerra3)
db.session.add(r_pintura1)
db.session.add(r_pintura2)
db.session.add(r_pintura3)
db.session.add(u1)
db.session.add(u2)
db.session.add(u3)
db.session.add_all([Role(rolename='admin', user=u1),
                    Role(rolename='user', user=u1),
                    Role(rolename='user', user=u2)])
db.session.commit()
