🚗 Proyecto Urban Routes - Pruebas Automatizadas 🧪

📑 Índice

📝 Descripción general del proyecto

🎯 Objetivos

🔍 Alcance de las pruebas

🧠 Estrategia de pruebas

🏷️ Tipos de pruebas

🛠️ Herramientas y tecnologías

📊 Casos de prueba

🐛 Reporte de defectos

📈 Resultados y métricas

📂 Evidencias

📁 Estructura del repositorio

💡 Principales aprendizajes

🚀 Mejoras futuras

📝 Descripción general del proyecto

El proyecto Urban Routes consiste en la automatización del flujo completo de trabajo de la plataforma web de transporte Urban Routes. La suite de pruebas verifica desde la configuración inicial de la ruta hasta la confirmación de la reserva de un vehículo, abarcando la selección de tarifas y la adición de requerimientos extra de forma automatizada y fluida.

🎯 Objetivos

📌 Validar la correcta ejecución del flujo completo de reserva en la plataforma web de Urban Routes.

📌 Automatizar la interacción con los elementos clave de la interfaz aplicando el patrón de diseño Page Object Model (POM).

📌 Garantizar que las funcionalidades clave (métodos de pago, preferencias y complementos) se procesen adecuadamente en cada interacción.

🔍 Alcance de las pruebas

El alcance abarca la automatización de los siguientes parámetros y escenarios de prueba:

📍 Configurar la dirección: Definición exitosa de las direcciones de origen y destino.

🚕 Selección de tarifa: Elección de la tarifa Comfort.

📱 Número de teléfono: Ingreso y validación del número telefónico.

💳 Método de pago: Vinculación e integración de una tarjeta de crédito.

💬 Mensaje al conductor: Envío de un mensaje personalizado para el conductor.

🛋️ Requerimientos especiales: Solicitud de manta y pañuelos en las opciones del viaje.

🍦 Agregar artículos: Adición de 2 helados al pedido.

⏳ Búsqueda de taxi: Verificación de la visualización e interacción con el modal de búsqueda.

👨‍✈️ Información del conductor (Opcional): Espera y visualización de los datos asignados del conductor en el modal.

🧠 Estrategia de pruebas

La estrategia sigue las mejores prácticas dentro de la automatización del software:

🧩 Modularidad: Separación clara entre la lógica de las pruebas y los localizadores/elementos mediante POM.

🔒 Independencia: Cada caso de prueba está diseñado para ejecutarse de manera limpia, aislada e independiente.

⏱️ Fiabilidad: Implementación de esperas explícitas de Selenium (WebDriverWait) para lidiar con componentes dinámicos y modales.

🏷️ Tipos de pruebas

🔄 Pruebas Funcionales (E2E): Cobertura completa del flujo de usuario de extremo a extremo.

🎨 Pruebas de Interfaz de Usuario (UI): Formulario, botones, modales y selección de elementos.

🔌 Pruebas de Integración / API: Verificaciones complementarias utilizando peticiones HTTP cuando corresponde.

🛠️ Herramientas y tecnologías

🐍 Lenguaje de programación: Python

🌐 Automatización Web: Selenium WebDriver

🧪 Framework de Pruebas: Pytest

📡 Librerías auxiliares: requests (para llamadas/aserciones API)

📐 Patrón de diseño: Page Object Model (POM)

💻 IDE recomendada: PyCharm

📊 Casos de prueba

Los casos de prueba detallados y la matriz de cobertura se encuentran documentados en los siguientes recursos externos:

📋 Matriz y Casos de Prueba (Google Sheets)

📄 Documentación complementaria de pruebas

🐛 Reporte de defectos

Cualquier comportamiento inusual o fallo detectado durante la ejecución de la suite automatizada es documentado siguiendo el ciclo de vida del error. Los reportes detallados están adjuntos en la documentación de evidencias.

📈 Resultados y métricas

📊 Pruebas ejecutadas: 9 escenarios automatizados principales.

✅ Tasa de éxito: 100% de efectividad en la suite principal.

⏱️ Tiempo de ejecución: Determinado dinámicamente por la sincronización de las esperas explícitas de los modales.

📂 Evidencias

Puedes consultar las capturas de pantalla, grabaciones y evidencias de ejecución en los siguientes enlaces:

📁 Evidencias de Ejecución - Archivo 1

📁 Evidencias de Ejecución - Archivo 2

📁 Estructura del repositorio

├── 📄 data.py          # Datos de prueba (direcciones, tarjetas, mensajes)
├── 🧪 main.py          # Suite de pruebas automatizadas (test cases)
├── 🧱 pages.py         # Clases de páginas y localizadores (POM)
├── 📘 README.md        # Documentación principal del proyecto
└── 📦 requirements.txt # Dependencias del proyecto (pytest, selenium, requests)


⚙️ Requisitos e instalación

🐍 Asegúrate de tener instalado Python en tu equipo.

📦 Instala los paquetes y dependencias necesarias:

pip install pytest selenium requests


🚀 Ejecuta todas las pruebas automatizadas con Pytest:

pytest


💡 Principales aprendizajes

🏛️ Implementación sólida del patrón Page Object Model (POM) para un código mantenible, limpio y reutilizable.

⏱️ Manejo avanzado de sincronización y esperas explícitas (WebDriverWait) en elementos dinámicos y temporizadores.

🔗 Integración exitosa entre casos de prueba ejecutados con Pytest y llamadas/validaciones HTTP con requests.

🚀 Mejoras futuras

⚙️ Integrar la suite automatizada en una canalización de Integración Continua (CI/CD) usando GitHub Actions o Jenkins.

📊 Generar reportes visuales e interactivos utilizando pytest-html o Allure Reports.

🧪 Extender la cobertura para incluir rutas alternativas, casos límite y escenarios negativos.
