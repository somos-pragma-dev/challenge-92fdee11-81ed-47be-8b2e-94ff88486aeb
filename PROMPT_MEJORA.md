# Prompt para Mejorar el Codigo Base

Copia y pega el siguiente contenido completo en un asistente de IA (Claude, ChatGPT, etc.)
para obtener un ZIP con el proyecto corregido y listo para compilar.

---

```
Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación o descripciones sin código, genera los archivos
correspondientes sin aplicar análisis de compilación
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:
src/loans/api/views.py
from rest_framework import status, viewsets
from rest_framework.response import Response
from.serializers import LoanSerializer
from.models import Loan

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


src/loans/models.py
from django.db import models

class Loan(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    term = models.IntegerField()
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=20)


src/loans/serializers.py
from rest_framework import serializers
from.models import Loan

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'


src/loans/tests/test_views.py
from django.urls import reverse
from rest_framework.test import APITestCase
from..models import Loan

class LoanViewSetTest(APITestCase):
    def test_create_loan(self):
        url = reverse('loan-list')
        data = {
            'amount': 1000,
            'term': 12,
            'interest_rate': 5.0,
            'status': 'pending'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


src/users/api/views.py
from rest_framework import viewsets
from.serializers import UserSerializer
from..models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


src/users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


src/users/serializers.py
from rest_framework import serializers
from.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


src/users/tests/test_views.py
from django.urls import reverse
from rest_framework.test import APITestCase
from..models import User

class UserViewSetTest(APITestCase):
    def test_create_user(self):
        url = reverse('user-list')
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


src/loans/api/idempotency.py
import uuid
from django.core.cache import cache

def idempotent_create_loan(request, data):
    idempotency_key = request.headers.get('Idempotency-Key', uuid.uuid4())
    cached_response = cache.get(idempotency_key)
    if cached_response:
        return cached_response
    else:
        # Logic to create loan and save to cache
        pass


src/loans/api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from.views import LoanViewSet

router = DefaultRouter()
router.register(r'loans', LoanViewSet, basename='loan')

urlpatterns = [
    path('', include(router.urls))
]


src/users/api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls))
]


src/loans/api/permissions.py
from rest_framework.permissions import BasePermission

class IsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET']:
            return True
        return request.user and request.user.is_authenticated


src/loans/api/authentication.py
from rest_framework_simplejwt.authentication import JWTAuthentication

class CustomJWTAuthentication(JWTAuthentication):
    pass


src/loans/api/authentication.py
from rest_framework_simplejwt.authentication import JWTAuthentication

class CustomJWTAuthentication(JWTAuthentication):
    pass


src/loans/api/views.py
from rest_framework import status, viewsets
from rest_framework.response import Response
from.serializers import LoanSerializer
from.models import Loan
from.permissions import IsAuthenticatedOrReadOnly
from.authentication import CustomJWTAuthentication

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [CustomJWTAuthentication]


src/loans/models.py
from django.db import models

class Loan(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    term = models.IntegerField()
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=20)


src/loans/serializers.py
from rest_framework import serializers
from.models import Loan

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'


src/loans/tests/test_views.py
from django.urls import reverse
from rest_framework.test import APITestCase
from..models import Loan

class LoanViewSetTest(APITestCase):
    def test_create_loan(self):
        url = reverse('loan-list')
        data = {
            'amount': 1000,
            'term': 12,
            'interest_rate': 5.0,
            'status': 'pending'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


src/users/api/views.py
from rest_framework import viewsets
from.serializers import UserSerializer
from..models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


src/users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


src/users/serializers.py
from rest_framework import serializers
from.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


src/users/tests/test_views.py
from django.urls import reverse
from rest_framework.test import APITestCase
from..models import User

class UserViewSetTest(APITestCase):
    def test_create_user(self):
        url = reverse('user-list')
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


src/loans/api/idempotency.py
import uuid
from django.core.cache import cache

def idempotent_create_loan(request, data):
    idempotency_key = request.headers.get('Idempotency-Key', uuid.uuid4())
    cached_response = cache.get(idempotency_key)
    if cached_response:
        return cached_response
    else:
        # Logic to create loan and save to cache
        pass


src/loans/api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from.views import LoanViewSet

router = DefaultRouter()
router.register(r'loans', LoanViewSet, basename='loan')

urlpatterns = [
    path('', include(router.urls))
]


src/users/api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls))
]


src/loans/api/permissions.py
from rest_framework.permissions import BasePermission

class IsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET']:
            return True
        return request.user and request.user.is_authenticated


src/loans/api/authentication.py
from rest_framework_simplejwt.authentication import JWTAuthentication

class CustomJWTAuthentication(JWTAuthentication):
    pass

```
