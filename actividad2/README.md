# Proyecto DevOps: Scraping de Datos con CI/CD

## Descripción

Este proyecto implementa un sistema de scraping para capturar información de tarjetas gráficas en Mercado Libre y utiliza Git, GitHub y GitHub Actions para integrar un flujo de trabajo DevOps con CI/CD. Incluye herramientas y buenas prácticas para gestión de versiones, desarrollo colaborativo, pruebas automatizadas y despliegue.

## Contenido

1. [Requisitos](#requisitos)
2. [Instalación](#instalación)
3. [Uso](#uso)
4. [Estructura del Proyecto](#estructura-del-proyecto)
5. [Pipeline CI/CD](#pipeline-cicd)
6. [Contribuciones](#contribuciones)
7. [Licencia](#licencia)

---

## Requisitos

- Python 3.9 o superior.
- Pip (gestor de paquetes de Python).
- Una cuenta de GitHub para clonar y colaborar en el repositorio.

---

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/usuario/proyecto.git
   cd proyecto
   ```
2. Instalar dependencias:
   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

---

## Uso

1. Ejecutar el scraper:
   ```bash
   python src/scraper.py
   ```
   Esto generará una lista de productos extraídos de Mercado Libre con sus nombres y precios.

2. Ejecutar pruebas automatizadas:
   ```bash
   python -m unittest discover tests
   ```

---

## Estructura del Proyecto

```plaintext
proyecto/
├── src/          # Código fuente del proyecto
│   ├── scraper.py # Archivo principal del scraping
├── tests/        # Pruebas automatizadas
│   ├── test_scraper.py
├── .github/      # Configuración de GitHub Actions
│   ├── workflows/
│       ├── ci-cd.yml
├── requirements.txt # Dependencias del proyecto
├── README.md     # Documentación principal
├── .gitignore    # Archivos y carpetas a excluir del control de versiones
```

---

## Pipeline CI/CD

### Configuración de GitHub Actions
El archivo `.github/workflows/ci-cd.yml` define un pipeline para automatizar pruebas y despliegues.

**Pipeline:**

1. **Pruebas**:
   - Validar el código con `unittest`.
2. **Despliegue**:
   - Implementar cambios aprobados en la rama `main`.

### Archivo de configuración
```yaml
name: CI/CD Pipeline

on:
  push:
    branches:
      - main
      - develop
  pull_request:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: |
          python -m unittest discover tests

  deploy:
    needs: test
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Deploy to server
        run: |
          echo "Despliegue completado."
```

---

## Contribuciones

1. Crear una rama a partir de `develop`:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
2. Realizar cambios y confirmar commits:
   ```bash
   git commit -m "Descripción de los cambios"
   ```
3. Crear un Pull Request hacia `develop`.

---

## Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).

