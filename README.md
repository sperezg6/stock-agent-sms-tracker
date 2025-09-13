# stock-agent-sms-tracker

Un agente automatizado para el seguimiento de acciones vía SMS.

## Descripción

Este proyecto implementa un agente que permite rastrear y consultar información sobre acciones bursátiles utilizando mensajes SMS. El sistema está diseñado para ser modular y extensible, facilitando la integración de nuevas herramientas y fuentes de datos.

## Estructura del Proyecto

- `main.py`: Script principal para ejecutar el agente.
- `lib/`
  - `agent.py`: Lógica principal del agente.
  - `agent_tools.py`: Herramientas auxiliares utilizadas por el agente.
  - `stocks_lists.json`: Listado de acciones soportadas.
- `resources/`
  - `prompts.py`: Prompts y mensajes predefinidos para el agente.
- `tests/`
  - `agents.ipynb`: Notebook con pruebas y ejemplos de uso.

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/sperezg6/stock-agent-sms-tracker.git
   cd stock-agent-sms-tracker
   ```
2. Instala las dependencias necesarias (si aplica):
   ```bash
   pip install -r requirements.txt
   ```

## Uso

Ejecuta el agente con:
```bash
python main.py
```

Sigue las instrucciones en pantalla para interactuar con el agente y consultar información de acciones vía SMS.

## Pruebas

Puedes encontrar ejemplos y pruebas en el notebook `tests/agents.ipynb`.

## Contribución

Las contribuciones son bienvenidas. Por favor, abre un issue o pull request para sugerencias o mejoras.

## Licencia

MIT
