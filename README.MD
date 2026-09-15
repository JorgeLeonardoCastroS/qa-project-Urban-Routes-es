# 🚗 Proyecto Urban Routes - Pruebas Automatizadas 🧪

## 📑 Índice
- [📝 Descripción general del proyecto](#-descripción-general-del-proyecto)
- [🎯 Objetivos](#-objetivos)
- [🔍 Alcance de las pruebas](#-alcance-de-las-pruebas)
- [🧠 Estrategia de pruebas](#-estrategia-de-pruebas)
- [🏷️ Tipos de pruebas](#️-tipos-de-pruebas)
- [🛠️ Herramientas y tecnologías](#️-herramientas-y-tecnologías)
- [📊 Casos de prueba](#-casos-de-prueba)
- [🐛 Reporte de defectos](#-reporte-de-defectos)
- [📈 Resultados y métricas](#-resultados-y-métricas)
- [📂 Evidencias](#-evidencias)
- [📁 Estructura del repositorio](#-estructura-del-repositorio)
- [💡 Principales aprendizajes](#-principales-aprendizajes)
- [🚀 Mejoras futuras](#-mejoras-futuras)

---

## 📝 Descripción general del proyecto
El proyecto **Urban Routes** consiste en la automatización del flujo completo de trabajo de la plataforma web de transporte Urban Routes. La suite de pruebas verifica desde la configuración inicial de la ruta hasta la confirmación de la reserva de un vehículo, abarcando la selección de tarifas y la adición de requerimientos extra de forma automatizada y fluida.

---

## 🎯 Objetivos
- 📌 Validar la correcta ejecución del flujo completo de reserva en la plataforma web de **Urban Routes**.
- 📌 Automatizar la interacción con los elementos clave de la interfaz aplicando el patrón de diseño **Page Object Model (POM)**.
- 📌 Garantizar que las funcionalidades clave (métodos de pago, preferencias y complementos) se procesen adecuadamente en cada interacción.

---

## 🔍 Alcance de las pruebas
El alcance abarca la automatización de los siguientes parámetros y escenarios de prueba:

1. 📍 **Configurar la dirección:** Definición exitosa de las direcciones de origen y destino.
2. 🚕 **Selección de tarifa:** Elección de la tarifa *Comfort*.
3. 📱 **Número de teléfono:** Ingreso y validación del número telefónico.
4. 💳 **Método de pago:** Vinculación e integración de una tarjeta de crédito.
5. 💬 **Mensaje al conductor:** Envío de un mensaje personalizado para el conductor.
6. 🛋️ **Requerimientos especiales:** Solicitud de manta y pañuelos en las opciones del viaje.
7. 🍦 **Agregar artículos:** Adición de 2 helados al pedido.
8. ⏳ **Búsqueda de taxi:** Verificación de la visualización e interacción con el modal de búsqueda.
9. 👨‍✈️ **Información del conductor (Opcional):** Espera y visualización de los datos asignados del conductor en el modal.

---

## 🧠 Estrategia de pruebas
La estrategia sigue las mejores prácticas dentro de la automatización del software:
- 🧩 **Modularidad:** Separación clara entre la lógica de las pruebas y los localizadores/elementos mediante **POM**.
- 🔒 **Independencia:** Cada caso de prueba está diseñado para ejecutarse de manera limpia, aislada e independiente.
- ⏱️ **Fiabilidad:** Implementación de esperas explícitas de Selenium (`WebDriverWait`) para lidiar con componentes dinámicos y modales.

---

## 🏷️ Tipos de pruebas
- 🔄 **Pruebas Funcionales (E2E):** Cobertura completa del flujo de usuario de extremo a extremo.
- 🎨 **Pruebas de Interfaz de Usuario (UI):** Formulario, botones, modales y selección de elementos.
- 🔌 **Pruebas de Integración / API:** Verificaciones complementarias utilizando peticiones HTTP cuando corresponde.

---

## 🛠️ Herramientas y tecnologías
- 🐍 **Lenguaje de programación:** Python
- 🌐 **Automatización Web:** Selenium WebDriver
- 🧪 **Framework de Pruebas:** Pytest
- 📡 **Librerías auxiliares:** `requests` (para llamadas/aserciones API)
- 📐 **Patrón de diseño:** Page Object Model (POM)
- 💻 **IDE recomendada:** PyCharm

---

## 📊 Casos de prueba
Los casos de prueba detallados y la matriz de cobertura se encuentran documentados en los siguientes recursos externos:
- 📋 [Matriz y Casos de Prueba (Google Sheets)](https://docs.google.com/spreadsheets/d/1EKqraMX7wnIfejrSfI0kyFkvZP5pYCM3/edit?usp=sharing&ouid=117662769631159222767&rtpof=true&sd=true)
- 📄 [Documentación complementaria de pruebas](https://docs.google.com/spreadsheets/d/1J7yz6u1FKaTTKn5V8bP7KuxGdpw-WsK-/edit?usp=sharing&ouid=117662769631159222767&rtpof=true&sd=true)

---

## 🐛 Reporte de defectos
Cualquier comportamiento inusual o fallo detectado durante la ejecución de la suite automatizada es documentado siguiendo el ciclo de vida del error. Los reportes detallados están adjuntos en la documentación de evidencias.

---

## 📈 Resultados y métricas
- 📊 **Pruebas ejecutadas:** 9 escenarios automatizados principales.
- ✅ **Tasa de éxito:** 100% de efectividad en la suite principal.
- ⏱️ **Tiempo de ejecución:** Determinado dinámicamente por la sincronización de las esperas explícitas de los modales.

---

## 📂 Evidencias
Puedes consultar las capturas de pantalla, grabaciones y evidencias de ejecución en los siguientes enlaces:
- 📁 [Evidencias de Ejecución - Archivo 1](https://drive.google.com/file/d/1m4fxFs-PpMvzW7mRmBogz5fP50LKRc6m/view?usp=sharing)
- 📁 [Evidencias de Ejecución - Archivo 2](https://drive.google.com/file/d/1OxxTrjEAZ31lP_ZMznEuPuFZ4E5nk6nR/view?usp=sharing)

---

## 📁 Estructura del repositorio
```text
├── 📄 data.py          # Datos de prueba (direcciones, tarjetas, mensajes)
├── 🧪 main.py          # Suite de pruebas automatizadas (test cases)
├── 🧱 pages.py         # Clases de páginas y localizadores (POM)
├── 📘 README.md        # Documentación principal del proyecto
└── 📦 requirements.txt # Dependencias del proyecto (pytest, selenium, requests)
```

### ⚙️ Requisitos e instalación
1. 🐍 Asegúrate de tener instalado Python en tu equipo.
2. 📦 Instala los paquetes y dependencias necesarias:
   ```bash
   pip install pytest selenium requests
   ```
3. 🚀 Ejecuta todas las pruebas automatizadas con Pytest:
   ```bash
   pytest
   ```

---

## 💡 Principales aprendizajes
- 🏛️ Implementación sólida del patrón **Page Object Model (POM)** para un código mantenible, limpio y reutilizable.
- ⏱️ Manejo avanzado de sincronización y esperas explícitas (`WebDriverWait`) en elementos dinámicos y temporizadores.
- 🔗 Integración exitosa entre casos de prueba ejecutados con **Pytest** y llamadas/validaciones HTTP con **requests**.

---

## 🚀 Mejoras futuras
- ⚙️ Integrar la suite automatizada en una canalización de **Integración Continua (CI/CD)** usando GitHub Actions o Jenkins.
- 📊 Generar reportes visuales e interactivos utilizando `pytest-html` o **Allure Reports**.
- 🧪 Extender la cobertura para incluir rutas alternativas, casos límite y escenarios negativos.
