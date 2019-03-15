# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 17:54:25 2018

@author: gulam
"""

from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
R = 6373.0
#lat1 = radians(52.2296756)
#lon1 = radians(21.0122287)
#lat2 = radians(52.406374)
#lon2 = radians(16.9251681)
#
#dlon = lon2 - lon1
#dlat = lat2 - lat1
#
#a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
#c = 2 * atan2(sqrt(a), sqrt(1 - a))
#
#distance = R * c
#
#print("Result:", distance)
#print("Should be:", 278.546, "km")


def distance(lt1, ln1, lt2, ln2):

    lat1 = radians(lt1)
    lon1 = radians(ln1)
    lat2 = radians(lt2)
    lon2 = radians(ln2)
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    #distance = R * c
    return float(R * c * 1000.0) #in meters
#    print("Result:", distance)
#    print("Should be:", 278.546, "km")