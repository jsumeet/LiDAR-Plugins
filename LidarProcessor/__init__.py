# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LidarProcessor
                                 A QGIS plugin
 This plugin is used to Process Lidar files. Compression, Visualization and tile indexing can be done.
                             -------------------
        begin                : 2015-10-21
        copyright            : (C) 2015 by Tuple Coders
        email                : tuplecoders@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LidarProcessor class from file LidarProcessor.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .lidar_processor import LidarProcessor
    return LidarProcessor(iface)
