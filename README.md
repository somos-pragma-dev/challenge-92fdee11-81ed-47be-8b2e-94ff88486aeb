# Diseño de una API REST en un sistema de gestión de préstamos

En el sistema de gestión de préstamos de una entidad financiera, se requiere diseñar una API REST que permita la creación, consulta y actualización de préstamos. La API debe autenticar a los usuarios antes de permitir cualquier operación. Los préstamos tienen atributos como monto, plazo, tasa de interés y estado. El sistema debe manejar correctamente los errores y validaciones del dominio, como préstamos con montos negativos o plazos inválidos. Además, debe asegurar la idempotencia en la creación de préstamos para evitar duplicados.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Python Django REST |
| **Nivel** | junior-l2 |
| **Tipo** | theoretical |
| **Tiempo estimado** | 2 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Exploración del dominio y requerimientos

**Objetivo:** Identificar los actores, fuentes y sumideros involucrados en el proceso de gestión de préstamos, así como las propiedades operativas y umbrales numéricos relevantes.

**Tiempo estimado:** 30 minutos

**Instrucciones:**

- Enumera los actores principales en el proceso de gestión de préstamos (originador de créditos, motor antifraude, buró de riesgos).
- Identifica las fuentes y sumideros de datos en el sistema (solicitudes de préstamos, respuestas del buró, actualizaciones de estado).
- Define las propiedades operativas del sistema, como la latencia esperada en la consulta de préstamos y la consistencia requerida entre los datos del préstamo y el estado del cliente.

**Entregable:** Documento que describe los actores, fuentes, sumideros y propiedades operativas del sistema de gestión de préstamos.

<details>
<summary>Pistas de conocimiento</summary>

- Piensa en los diferentes roles que intervienen en la concesión de un préstamo y cómo se relacionan.
- Considera los umbrales numéricos que son críticos para el negocio, como el monto máximo de un préstamo o la tasa de interés mínima.

</details>

### Fase 2: Definición de la API REST y autenticación

**Objetivo:** Establecer los endpoints de la API REST y definir el proceso de autenticación de usuarios.

**Tiempo estimado:** 1 hora

**Instrucciones:**

- Diseña los endpoints para la creación, consulta y actualización de préstamos.
- Define el proceso de autenticación de usuarios, incluyendo los métodos de autenticación válidos y los roles de usuario.
- Especifica las validaciones y errores comunes que deben manejarse en cada endpoint.

**Entregable:** Documento que describe los endpoints de la API REST, el proceso de autenticación y las validaciones y errores comunes.

<details>
<summary>Pistas de conocimiento</summary>

- Considera los diferentes métodos HTTP (POST, GET, PUT) y cómo se aplican a cada operación.
- Piensa en los posibles errores y validaciones que deben implementarse para asegurar la integridad de los datos.

</details>

### Fase 3: Idempotencia y consistencia en la creación de préstamos

**Objetivo:** Asegurar la idempotencia en la creación de préstamos y mantener la consistencia de los datos.

**Tiempo estimado:** 40 minutos

**Instrucciones:**

- Define la clave de idempotencia para la creación de préstamos y describe cómo se asegura la idempotencia.
- Especifica las medidas para mantener la consistencia de los datos entre la creación de un préstamo y su registro en el sistema.
- Identifica los posibles modos de falla y cómo se manejarán.

**Entregable:** Documento que describe la implementación de la idempotencia y las medidas para mantener la consistencia de los datos.

<details>
<summary>Pistas de conocimiento</summary>

- Piensa en cómo se puede garantizar que dos solicitudes idénticas no creen duplicados.
- Considera los posibles modos de falla y cómo se pueden mitigar para mantener la consistencia.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Cuáles son los actores principales en el proceso de gestión de préstamos y cuáles son sus roles?
- **paraQueSirve**: ¿Para qué se utilizan los endpoints de la API REST en el sistema de gestión de préstamos?
- **comoSeUsa**: ¿Cómo se implementa la autenticación de usuarios en la API REST?
- **erroresComunes**: ¿Cuáles son los errores comunes que deben manejarse en la creación de préstamos y cómo se pueden mitigar?
- **queDecisionesImplica**: ¿Qué decisiones implica asegurar la idempotencia en la creación de préstamos y cómo se pueden justificar?

## Criterios de Evaluacion

- Identificación correcta de los actores, fuentes y sumideros en el dominio de la gestión de préstamos.
- Definición clara de los endpoints de la API REST y el proceso de autenticación.
- Manejo adecuado de las validaciones y errores comunes en la API.
- Implementación efectiva de la idempotencia y medidas para mantener la consistencia de los datos.

---

*Reto generado automaticamente por Challenge Generator - Pragma*
