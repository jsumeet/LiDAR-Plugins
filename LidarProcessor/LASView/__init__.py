# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LASView
                                 A QGIS plugin
 This plugin helps in visualization of LAS files
                             -------------------
        begin                : 2015-10-30
        copyright            : (C) 2015 by tuple coders
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
    """Load LASView class from file LASView.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .LiDAR_Processor import LASView
    return LASView(iface)
