#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# @author     Raúl Caro Pastorino
# @email      dev@fryntiz.es
# @web        https://fryntiz.es
# @gitlab     https://gitlab.com/fryntiz
# @github     https://github.com/fryntiz
# @twitter    https://twitter.com/fryntiz
# @telegram   https://t.me/fryntiz

# Create Date: 2019/10/27
# Project Name:
# Description:
#
# Dependencies:
#
# Revision 0.01 - File Created
# Additional Comments:

# @copyright  Copyright © 2019 Raúl Caro Pastorino
# @license    https://wwww.gnu.org/licenses/gpl.txt

# Copyright (C) 2019  Raúl Caro Pastorino
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

# Guía de estilos aplicada: PEP8

# #           Descripción           # #
# Ejemplo de uso para la librería, mostrará el índice UV, el valor UVA y UVB

from time import sleep
from VEML6075 import VEML6075
from VEML6075_uv_index import VEML6075_uv_index
from VEML6075_uva import VEML6075_uva
from VEML6075_uvb import VEML6075_uvb

veml6075 = VEML6075(integration_time=200)
veml6075_uv_index = VEML6075_uv_index(integration_time=200)
veml6075_uva = VEML6075_uva(integration_time=200)
veml6075_uvb = VEML6075_uvb(integration_time=200)

while True:
    print('Debug Clase Padre')
    veml6075.debug()
    sleep(3)
    print('')
    print('Debug de cada Clase Hija')
    veml6075_uv_index.debug()
    veml6075_uva.debug()
    veml6075_uvb.debug()
    sleep(3)
    print('')
