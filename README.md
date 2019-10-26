# raspberry-sensor-veml6075

Clase para integrar el sensor VEML6075 con python en aplicaciones fácilmente con métodos para obtener valores y estructura para generar dinámicamente su tabla con SQLAlchemy. 
Mide:

- Índice UV
- UVA
- UVB

Repositorio con modelo y ejemplos para el sensor VEML6075 que obtiene valores
UVA/UVB de la luz en el ambiente.

Para el funcionamiento del sensor se parte de la librería oficial de adafruit:

https://github.com/adafruit/Adafruit_CircuitPython_VEML6075

De forma que este repositorio utiliza esa librería y sus dependencias como base
añadiendo otras características que he visto necesarias en mi caso.

## Dependencias

Los entornos donde han sido probados satisfactoriamente utilizaban las 
siguientes versiones de las aplicaciones necesarias:

- python 3.7.3
- raspbian, basado en debian 10.1
- bash 5.0.3
- pip3 18.1

Se tiene que instalar la librería de adafruit mediante el gestor de paquetes de
python 3

```bash
pip3 install adafruit-circuitpython-veml6070
```

Además, también es necesario instalar las librerías siguientes:

```bash
pip3 install adafruit-circuitpython-busdevice
pip3 install Adafruit-Blinka
```

También puedes adaptarlo usando entornos virtuales o descargar el repositorio
manualmente desde el enlace indicado al comienzo de este documento.

## Métodos de la librería original Adafruit para obtener valores

- uv_index - The calculated UV Index.
- uva - The calibrated UVA reading, in 'counts' over the sample period
- uvb - The calibrated UVB reading, in 'counts' over the sample period

## Links interesantes relacionados

https://github.com/adafruit/Adafruit_CircuitPython_VEML6075
https://learn.adafruit.com/adafruit-veml6075-uva-uvb-uv-index-sensor/python-circuitpython
https://www.raspberrypi.org/forums/viewtopic.php?t=151317