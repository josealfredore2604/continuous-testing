#  🧪 Continuous Testing - Flask API

Un proyecto de ejemplo que demuestra diferentes niveles de testing automatizado en una aplicación Flask simple, implementando **Unit Tests**, **Integration Tests**, y **End-to-End Tests** con Docker y CI/CD.

## 📋 Descripción del Proyecto

Esta aplicación Flask proporciona una API REST simple para realizar operaciones matemáticas. El proyecto está diseñado para mostrar las mejores prácticas de testing continuo con diferentes niveles de pruebas automatizadas.

### ✨ Funcionalidades

- **API REST** con Flask para operaciones matemáticas
- **Endpoint de suma** (`POST /suma`) que recibe dos números y devuelve el resultado
- **Página de inicio** (`GET /`) con información básica de la API
- **Testing multicapa** con diferentes tipos de pruebas
- **Análisis estático** con flake8
- **Containerización** completa con Docker

## 🏗️ Estructura del Proyecto

```
continuous-testing/
├── calc/                    # Módulo de cálculos
│   ├── __init__.py
│   └── calc.py             # Lógica de negocio (función suma)
├── tests/                   # Suite de pruebas
│   ├── test_calc.py        # Unit Tests
│   ├── test_api.py         # Integration Tests  
│   └── test_e2e.py         # End-to-End Tests
├── main.py                 # Aplicación Flask principal
├── requirements.txt        # Dependencias Python
├── Dockerfile             # Imagen Docker
├── docker-compose.yml     # Orquestación de servicios
└── .github/workflows/     # Pipeline CI/CD
    └── ci.yml
```

## 🧪 Niveles de Testing

### 1. **Unit Tests** (`test_calc.py`)
Pruebas unitarias que validan la lógica de negocio aislada:
```python
def test_suma():
  assert suma(2, 3) == 5
```

### 2. **Integration Tests** (`test_api.py`)  
Pruebas de integración que validan la API completa:
```python
def test_api_suma():
  with app.test_client() as client:
    response = client.post('/suma', json={"a": 4, "b": 6})
    assert response.status_code == 200
    assert response.json()["resultado"] == 10
```

### 3. **End-to-End Tests** (`test_e2e.py`)
Pruebas end-to-end que validan el flujo completo con servidor real:
```python
def test_e2e_full_workflow():
  # Inicia Flask en un hilo separado
  # Hace peticiones HTTP reales
  # Valida el comportamiento completo
```

## 🚀 Uso Local

### Prerequisitos
- Docker y Docker Compose instalados
- Python 3.11+ (opcional, para desarrollo local)

### Ejecutar con Docker

#### 🧪 **Ejecutar todos los tests:**
```bash
docker compose build
docker compose run --rm app pytest tests/ -v
```

#### 📊 **Análisis estático:**
```bash
docker compose run --rm app flake8 calc/
```

#### 🎯 **Tests específicos:**
```bash
# Unit tests
docker compose run --rm app pytest tests/test_calc.py -v

# Integration tests  
docker compose run --rm app pytest tests/test_api.py -v

# End-to-end tests
docker compose run --rm app pytest tests/test_e2e.py -v
```

#### 🌐 **Ejecutar la aplicación:**
```bash
docker compose run --rm -p 5000:5000 app python main.py
```
Luego visita: http://localhost:5000

### API Endpoints

#### `GET /`
Página de inicio con información de la API
```bash
curl http://localhost:5000
```

#### `POST /suma`
Suma dos números
```bash
curl -X POST http://localhost:5000/suma \
  -H "Content-Type: application/json" \
  -d '{"a": 10, "b": 15}'
```

**Respuesta:**
```json
{
  "resultado": 25
}
```

## 🔄 Pipeline CI/CD

El proyecto incluye un pipeline de GitHub Actions que ejecuta:

1. **Static Analysis** - Análisis de código con flake8
2. **Unit Tests** - Pruebas unitarias de lógica de negocio  
3. **Integration Tests** - Pruebas de API y componentes
4. **E2E Tests** - Pruebas end-to-end del flujo completo

### Triggers del Pipeline:
- **Push** a ramas `main` y `dev`
- **Pull Requests** a cualquier rama

## 🛠️ Desarrollo Local (sin Docker)

Si prefieres desarrollar sin Docker:

```bash
# Crear entorno virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# o .venv\Scripts\activate  # Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar tests
pytest tests/ -v

# Ejecutar aplicación
python main.py
```

## 📈 Métricas de Testing

- **Cobertura de código:** Unit + Integration + E2E
- **Tiempo de ejecución:** ~10-15 segundos para toda la suite
- **Tipos de validación:**
  - Lógica de negocio (Unit)
  - API endpoints (Integration)  
  - Flujo completo (E2E)
  - Calidad de código (Static Analysis)

## 🎯 Casos de Uso

Este proyecto sirve como referencia para:

- **Implementar testing multicapa** en aplicaciones Flask
- **Configurar pipelines de CI/CD** con GitHub Actions
- **Containerizar aplicaciones Python** con Docker
- **Establecer prácticas de testing continuo** en equipos de desarrollo
- **Demostrar diferentes enfoques de testing** (unitario, integración, e2e)

## 🔧 Personalización

Para adaptar este proyecto a tus necesidades:

1. **Modificar la lógica de negocio** en `calc/calc.py`
2. **Añadir nuevos endpoints** en `main.py`
3. **Extender los tests** en el directorio `tests/`
4. **Configurar variables de entorno** en `docker-compose.yml`
5. **Ajustar el pipeline** en `.github/workflows/ci.yml`
