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
El dataset proporcionado por la empresa está compuesto por imágenes de 200x200 en escala de grises.
Por cada categoría nos han proporcionado 300 imágenes con sus etiquetas. Las categorías a clasificar son las siguientes:
* *Inclusions*
* *Patches*
* *Scratches*

<p align="center">
	<img src="exemples/tipos_defectos.png" alt="resultado" width="80%"/>
</p>


## ESQUEMA GENERAL
<p align="center">
	<img src="exemples/esquema.jpeg" alt="esquema"/>
</p>


## DOCUMENTACION

Se adjunta la lista de la documentación oficial del proyecto entregada al cliente:
* Entrega 1: -> [Especificación de Requisitos Software (ERS)](docs/ERS_grupoC.pdf)
* Entrega 2: -> [Documento de diseño](docs/Diseño_grupoC.pdf)


## REQUISITOS

* Python 3.7+
* Requirements = Requirement.txt
```bash
$ pip install -e .
$ pip install -r requirements.txt
```
###### numpy (1.22.3)
###### opencv_python (4.5.3.56)


## EJECUTAR LA APLICACION

* **algorithm:** El archivo main_algorithm.py es el archivo principal, con el podemos realizar las primeras pruebas de la clasificación y localización de defectos llamando a nuestra funcion ImperDetect.detection().

* **imper_detect:** El archivo main_imper_detect.py es el archivo de nuestra clase principal (fachada), donde desde aqui llamamos a las clase RecognitionSystem para realizar la deteción y el dibujado de las imágenes. 

* **system_recognition:** El archivo main_system_recognition.py es el core de nuestra aplicación. Desde esta clase se realiza la detección, utilizando yolo_v5 aunque se podria utilizar otra red neuronal si la tuvieramos entrenada. También se realiza el dibujado de los resultados y un post-procesado de los resultados para quedarnos con la etiqueta de mayor peso como resultado final.

* **imperfection:** El archivo main_imperfection.py contiene la clase Imperfection, donde definimos que formato tendrá cada resultado de la red neuronal. El resultado obtenido desde yolo_v5, será una lista de Imperfection.


### Run algorithm (¡No olvidar los requisitos!)
```bash
$ python src/algorithm/main_algorithm.py --file="dataset/IMAGES/inclusion_1.jpg" -s
```

* **test_algorithm.py**: Es el archivo que realiza los test unitarios sobre el código principal para verificar que las funciones/clases funcionen correctamente.

### Tests automáticos.  
Estos test son automáticos cuando hay un push o un pull desde github.

Es necesario instalar el siguiente paquete:
```bash
$ pip install tox
$ tox
```

## ESTRUCTURA DEL PROYECTO

```
.
├── dataset
│        ├── ANNOTATIONS
│        └── IMAGES
├── docs
│        └── ERS_grupoC.pdf
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
│   └── imper_detect
│       └── main_imper_detect.py
│   └── imperfection
│       └── main_imperfection.py
│   └── system_recognition
│       └── main_system_recognition.py
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
