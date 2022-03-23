# AIVA_2022_METAL GRUPO C
## Clasificación y localización de defectos en imágenes de superficies de metal.

## AUTORES

* **PÉREZ GARCÍA DE LA PUENTE, NATALIA LOURDES** - *Miembro 1* - [Natalia](https://github.com/natalialperez)
* **GILABERT MAÑO, VICENTE** - *Miembro 2* - [Vicent](https://github.com/vgilabert94)
* **ROSARIO TREMOULET, LUIS** - *Miembro 3* - [Luis](https://github.com/Luisrosario2604)


## DESCRIPCION
Este repositorio contiene la práctica para la asignatura Aplicaciones Industriales en la Visión Artificial perteneciente al Máster Universitario en Visión Artificial impartido en la Universidad Rey Juan Carlos.  

El objetivo de este trabajo es la clasificación y detección de defectos en superficies metalicas en una línea de producción. Para ello realizaremos una implementacion en *Python* con un detector de objetos (YOLOv5) y lo conectaremos mediante *C* a la aplicacion que ya esta funcionando en la fabrica.


## ESQUEMA GENERAL
<p align="center">
	<img src="Exemples/esquema.jpeg" alt="esquema"/>
</p>


## Estructura del proyecto

```
.
├── Data
│   ├── ANNOTATIONS
│   └── IMAGES
├── Exemples
│   └── Screen1.png
├── .gitignore
├── main.py
├── README.md
├── requirements.txt
└── tests.py
```

## Tests

![Tests](https://github.com/Luisrosario2604/AIVA_2022_METAL/actions/workflows/tests.yml/badge.svg)


#### Parte 1

* main.py :

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce consectetur augue quis odio rutrum consequat. Etiam ultricies vehicula purus, nec fermentum augue iaculis at. Suspendisse id molestie dolor, sollicitudin imperdiet magna. Vivamus porta sapien ut finibus tempus. Pellentesque et ex sapien. Praesent justo est, tristique sit amet libero quis, tincidunt laoreet augue. Vivamus auctor sem nunc. Suspendisse scelerisque feugiat congue. Sed id elit massa. Sed elit mi, semper ac mi nec, venenatis ultricies risus. Fusce consequat purus imperdiet porta consequat.

#### Parte 2

* test.py :

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce consectetur augue quis odio rutrum consequat. Etiam ultricies vehicula purus, nec fermentum augue iaculis at. Suspendisse id molestie dolor, sollicitudin imperdiet magna. Vivamus porta sapien ut finibus tempus. Pellentesque et ex sapien. Praesent justo est, tristique sit amet libero quis, tincidunt laoreet augue. Vivamus auctor sem nunc. Suspendisse scelerisque feugiat congue. Sed id elit massa. Sed elit mi, semper ac mi nec, venenatis ultricies risus. Fusce consequat purus imperdiet porta consequat.

## Requisitos

* Python 3.7+
* Requirements = Requirement.txt
```bash
$ pip install -r requirements.txt
```
###### matplotlib (3.3.4)
###### numpy (1.21.3)
###### opencv_python (4.5.3.56)
###### Pillow (8.4.0)

## Usage

#### Ejecutar la detection de defectos en imágenes de superficies de metal

```bash
$ python main.py
```

#### Ejecutar los tests

```bash
$ python tests.py -v
```

## Ejemplos

![Exemples](./Exemples/Screen1.png)


