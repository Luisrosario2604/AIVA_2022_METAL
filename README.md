# AIVA_2022_METAL
# Clasificación y localización de defectos en imágenes de superficies de metal.

## AUTORES
* **PÉREZ GARCÍA DE LA PUENTE, NATALIA LOURDES** - *Miembro 1* - [Natalia](https://github.com/natalialperez)
* **GILABERT MAÑO, VICENTE** - *Miembro 2* - [Vicent](https://github.com/vgilabert94)
* **ROSARIO TREMOULET, LUIS** - *Miembro 3* - [Luis](https://github.com/Luisrosario2604)

## Descripción
Este repositorio contiene la práctica para la asignatura Aplicaciones Industriales en la Visión Artificial perteneciente al Máster Universitario en Visión Artificial impartido en la Universidad Rey Juan Carlos.

El objetivo de este trabajo es la clasificación y detección de defectos en superficies metálicas en una línea de producción. Para ello realizaremos una implementación en *Python* con un detector de objetos (YOLOv5) y lo conectaremos mediante *C* a la aplicación que ya está funcionando en la fábrica.

## Dataset
El dataset proporcionado por la empresa está compuesto por imágenes de 200x200 en escala de grises.
Por cada categoría nos han proporcionado 300 imágenes con sus etiquetas. Las categorías a clasificar son las siguientes:
* *Inclusions*
* *Patches*
* *Scratches*

<p align="center">
	<img src="exemples/tipos_defectos.png" alt="resultado" width="80%"/>
</p>


## Eequema general
<p align="center">
	<img src="exemples/esquema.jpeg" alt="esquema"/>
</p>


## Documentación
Se adjunta la lista de la documentación oficial del proyecto entregada al cliente:
* ERS : -> [Especificación de Requisitos Software (ERS)](docs/ERS_grupoC.pdf)
* Diseño : -> [Documento de diseño](docs/Diseño_grupoC.pdf)
* Sistema Funcional: -> [Documento del Sistema funcional](docs/SistemaFuncional_grupoC.pdf)


## Requisitos
* Docker
* Postman (http requests)


## Ejecutar la aplicación
Utilizando nuestra imagen de docker, podemos instalar todo nuestro repositirio y las dependencias que necesitaremos. 
```bash
$ docker pull luisrosario04/aiva_2022_metal
```

Una vez descargada la imagen, vamos a lanzar el contenedor (docker) con el siguiente comando:
```bash
$ docker run -p 8000:5000 luisrosario04/aiva_2022_metal
```
El servidor escucha en *localhost:8000*

Documentación de las requests http -> [POSTMAN](https://documenter.getpostman.com/view/4800670/UyrAGHub)


## Tests
![Tests](https://github.com/Luisrosario2604/AIVA_2022_METAL/actions/workflows/tests.yml/badge.svg)

Cuado un push o pull se effectua automaticamente :

* Los tests se lazan, resultados en github actions
* La calidad del codigo esta probado con *flake8* y *mypy*

Hay 20 tests con un coverage total de 96%


## ESTRUCTURA DEL PROYECTO
```
.
├── dataset
│        ├── ANNOTATIONS
│        └── IMAGES
├── docs
│        ├── Diseño_grupoC.pdf
│        └── ERS_grupoC.pdf
├── docker
│        └── Dockerfile
├── exemples
│        ├── esquema.jpeg
│        ├── resultado.jpeg
│        ├── Screen1.png
│        └── tipos_defectos.png
├── pyproject.toml
├── README.md
├── requirements_dev.txt
├── requirements.txt
├── setup.cfg
├── setup.py
├── src
│   └── algorithm
│       └── main_algorithm.py
│   └── fast_rcnn
│       └── main_fast_rcnn.py
│   └── imperfection
│       └── main_imperfection.py
│   └── server
│       └── main_server.py
│   └── system_recognition
│       └── main_system_recognition.py
│   └── yolo_v5
│       └── main_yolo_v5.py
├── tests
│       └── test_algorithm.py
├── yolo_v5
│       ├── models
│       ├── utils
│       ├── weights
│       ├── detect.py
│       └── export.py
└── tox.ini
```

## RESULTADOS
<p align="center">
	<img src="exemples/resultado.jpeg" alt="resultado" width="50%"/>
</p>
