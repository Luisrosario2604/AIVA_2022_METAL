# AIVA_2022_METAL_GRUPO_C
# Clasificación y localización de defectos en imágenes de superficies de metal.


## AUTORES

* **PÉREZ GARCÍA DE LA PUENTE, NATALIA LOURDES** - *Miembro 1* - [Natalia](https://github.com/natalialperez)
* **GILABERT MAÑO, VICENTE** - *Miembro 2* - [Vicent](https://github.com/vgilabert94)
* **ROSARIO TREMOULET, LUIS** - *Miembro 3* - [Luis](https://github.com/Luisrosario2604)


## DESCRIPCION
Este repositorio contiene la práctica para la asignatura Aplicaciones Industriales en la Visión Artificial perteneciente al Máster Universitario en Visión Artificial impartido en la Universidad Rey Juan Carlos.  

El objetivo de este trabajo es la clasificación y detección de defectos en superficies metálicas en una línea de producción. Para ello realizaremos una implementación en *Python* con un detector de objetos (YOLOv5) y lo conectaremos mediante *C* a la aplicación que ya está funcionando en la fábrica.

## RESULTADOS DE LOS TESTS

![Tests](https://github.com/Luisrosario2604/AIVA_2022_METAL/actions/workflows/tests.yml/badge.svg)

## DATASET
El dataset proporcionado por la empresa esta compuesto por imágenes de 200x200 en escala de grises.
Por cada categoría nos han proporcionado 300 imágenes con sus etiquetas. Las categorías a clasificar son las siguientes:
* *Inclusions*
* *Patches*
* *Scratches*

<p align="center">
	<img src="Exemples/tipos_defectos.png" alt="resultado" width="80%"/>
</p>


## ESQUEMA GENERAL
<p align="center">
	<img src="Exemples/esquema.jpeg" alt="esquema"/>
</p>


## DOCUMENTACION

Se adjunta la lista de la documentación oficial del proyecto entregada al cliente:
* Entrega 1: -> [Especificación de Requisitos Software (ERS)](docs/ERS_grupoC.pdf)


## REQUISITOS

* Python 3.7+
* Requirements = Requirement.txt
```bash
$ pip install -r requirements.txt
```
###### numpy (1.21.3)
###### opencv_python (4.5.3.56)


## EJECUTAR LA APLICACION

* yolo_implentation : El archivo "core" de nuestra aplicacion, donde estan las funciones para ejecutar las tereas deseadas. 

* main_algorithm : El archivo principal de la aplicación es el main.py, con el que podemos realizar las primeras pruebas de la clasificación y localización de defectos llamando a nuestra funcion ImperDetect.classify_and_locate.

* file_manager : El archivo donde se importarant las imagenes.

```bash
$ python3 src/algorithm/main_algorithm.py --file="dataset/IMAGES/inclusion_1.jpg" -s
```

* test_algorithm.py: Es el archivo que realiza los test unitarios sobre el código principal para verificar que las funciones/clases funcionen correctamente 

```bash
$ pip install tox
$ tox
```

## ESTRUCTURE DEL PROYECTO

```
.
├── dataset
│        ├── ANNOTATIONS
│        └── IMAGES
├── docs
│        └── ERS_grupoC.pdf
├── Exemples
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
│            ├── file_manager.py
│            ├── __init__.py
│            ├── main_algorithm.py
│            ├── py.typed
│            └── yolo_implementation.py
├── tests
│       └── test_algorithm.py
└── tox.ini
```


## RESULTADOS 
<p align="center">
	<img src="Exemples/resultado.jpeg" alt="resultado" width="50%"/>
</p>
