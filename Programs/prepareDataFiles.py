# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 22:42:22 2018

@author: gulam
"""

import pymongo #; print(pymongo.version); print(pymongo.has_c())
import numpy as np
import math
import initialize as init
from progressBar import printProgressBar
import os
import distance as dis

import zipfile
#imdb_archive_dir = 'C:\\Data\\'
#imdb_dir = 'aclImdb'
#archive = zipfile.ZipFile(imdb_archive_dir + 'aclImdb.zip', 'r')
#train_dir = imdb_dir + '/train'
#labels = []
#texts = []
#for label_type in ['/neg', '/pos']:
#    dir_name = train_dir + label_type
#    for fname in [x for x in archive.namelist() if x.startswith(dir_name)]:  #os.listdir(dir_name):
#        if fname[-4:] == '.txt':
#            f = archive.open(fname)
#            texts.append(f.read())
#            f.close()
#            if label_type == 'neg':
#                labels.append(0)
#            else:
#                labels.append(1)
#archive.close()

def archive_files(archive_list=[], zfilename='default.zip'):    
    zout = zipfile.ZipFile(os.path.join(init.datapath, zfilename), "w", zipfile.ZIP_DEFLATED) # <--- this is the change you need to make
    for fname in archive_list:
        zout.write(os.path.join(init.datapath, fname))
    zout.close()

def normalize_data(x, length=0):
    float_data = np.array(x).astype(float) #copy input
    if length == 0: 
        length = len(x)
    mean = float_data[:length].mean()
    float_data -= mean
    std = float_data[:length].std()
    float_data /= std    
    return (np.nan_to_num(float_data), mean, std)

def running_mean(x, N):
    cumsum = np.cumsum(np.insert(x, 0, 0)) 
    return np.insert((cumsum[N:] - cumsum[:-N]) / float(N), 0, x[:N-1])
    #return (cumsum[N:] - cumsum[:-N]) / float(N)

def prepareData(state, idx=1, progress=0):
    running_mean_count = 3
    printProgressBar(idx + 1, progress, prefix = state["Id"], suffix = 'Complete')
    recs = db.decoded.find({ "$and" : [{"Id":state["Id"] }, {"_id":{"$gte": state["Rid"] }}, {"_id":{"$lte": state["Mid"]}}] },{"Dt.A00":1, "Dt.T01":1, "Dt.G01":1,"Dt.G02":1, "_id":0}).sort([("Dt.T01",pymongo.ASCENDING)])
    Dt = []; Ts = []; Ds = [];
    for i, item in enumerate(recs):
        Dt.append(float(item["Dt"]["A00"]))
        Ts.append(float(item["Dt"]["T01"]))
        if i == 0 :
            Ds.append(float("0.0"))
            _lt = float(item["Dt"]["G01"])
            _ln = float(item["Dt"]["G02"])
        else:
            d = dis.distance(float(item["Dt"]["G01"]), float(item["Dt"]["G02"]), _lt, _ln)
            Ds.append(d)
            #print (d)            
            _lt = float(item["Dt"]["G01"])
            _ln = float(item["Dt"]["G02"])

    #timestamp = [dt.datetime.fromtimestamp(int(s)/1000) for s in Ts]   
    A = np.array([Dt, Ts]) # merge Dt, Ts in to a matrix of two rows(vectors)
    
    diff = np.diff(A) # produces the difference matrix with n-1 rows 
    diff = np.insert(diff, 0, np.array((0, 0)), axis=1)   

    dydx = np.array(np.zeros(len(Dt)), dtype=float)
    for i in range(1, len(Dt) - 1):       
        if (Ds[i] > 0.0 and diff[1][i] > 1e3) :
            dydx[i] = (diff[0][i] / diff[1][i]) 

#        if diff[1][i] > 0.001 :
#            dydx[i] = (diff[0][i] / diff[1][i]) 
#        else:
#            if Ds[i] < 5.0 :     # distance less than 5 meters                
#                dydx[i] = diff[0][i] / (diff[1][i] * Ds[i])  
#            else: 
#                dydx[i] = diff[0][i] / 0.1
#        print(Ts[i], "\t", Dt[i], "\t", Ds[i], "\t", diff[1][i], "\t", diff[0][i], "\t", dydx[i])
    if running_mean_count < dydx.shape[0] :
        dydx = running_mean(dydx, running_mean_count) #running average of 4 
#        dydx = np.hstack([np.array(np.zeros(running_mean_count - 1, dtype=float)), 
#                      running_mean(dydx, running_mean_count) ])
    Dtn, Dtm, Dtstd = normalize_data(Dt)
    Tsn, Tsm, Tsstd = normalize_data(Ts)  
    dydx, dydxm, dydxstd = normalize_data(dydx) 

    diff[0], d0m, d0std = normalize_data(diff[0])
    diff[1], d1m, d1std = normalize_data(diff[1]) 
    Dsn, Dsm, Dsstd = normalize_data(Ds) 
    stacked = np.vstack([ Tsn, Dtn, Dsn, dydx, diff[1], diff[0]])
#    original = np.vstack([Ts, Dt, Ds])
    details = np.array([ (stacked.shape[0], Tsn.shape[0]), (Tsm, Tsstd), (Dtm, Dtstd), (Dsm, Dsstd), (dydxm, dydxstd), (d1m, d1std), (d0m, d0std)  ])
    squarified = squarify(stacked)
    #print (idx, "Total records:", Ts.shape[0], "Squarified:", squarified.shape, "dydx(min/max):", np.min(dydx), "/", np.max(dydx))
    return (details, squarified)

def squarify(arr, pad_value=0):
    h, w = arr.shape    
    if (w <= h):
        return np.expand_dims(pad_and_shape(arr, h, pad_value), axis=0)
    else:
        #print("arr:", arr.shape)
        if w  % h != 0 : 
            squared = np.array([ arr[0:h, i:i+h]
                for i in range(0, w-h, h)])            
            lastsquare =  pad_and_shape(arr[0:h, w // h * h:], h)
            lastsquare = np.expand_dims(lastsquare, axis=0)
#            print("squared:", squared.shape)
#            print("lastsquare:", lastsquare.shape)        
            return np.concatenate([squared, lastsquare])
        else:
            return np.array([ arr[0:h, i:i+h]
                for i in range(0, w, h)])


def pad_and_shape(arr, length=60, pad_value=0):
    if length > (arr.shape[1]):
#        _front = int((length - arr.shape[1])/2)
#        _back = math.ceil((length - arr.shape[1])/2)
#        return np.array([ np.hstack([ 
#                            (pad_value * np.ones(_front, dtype=float)), 
#                            (a), 
#                            (pad_value * np.ones(_back, dtype=float)) ])
#                            for a in arr ] )
        _back = (length - arr.shape[1])
        return np.array([ np.hstack([ 
                            (a), 
                            (pad_value * np.ones(_back, dtype=float)) ])
                            for a in arr ] )
    else:
        if length < (arr.shape[1])  :
            return np.array([ a[:length] 
                                for a in arr ] )
        else:
            if length == (arr.shape[1]):
                return arr                    

def categorize (x, pmin, pmax):
    if x[0] < pmin or x[1] > pmax:
        return 1    
    else: 
        return 0                                
                                
np.seterr(all='ignore')
np.seterr(invalid='print')

client = pymongo.MongoClient("localhost", 27017)
db = client.sandbox

_file_list = []
np.save(os.path.join(init.datapath, 'Ids.npy'), np.array(init.Ids))
_file_list.append('Ids.npy')
#Engine On Sates
for Id in init.Ids:
    states = db.states.find({ "$and" : [{"Id":Id}, {"Pid":"D00"}, {"St":1}, {'Ty': 'digital'}, { "$where" : "this.T1 < this.T2 && this.Dis > 0.0" } ]})
    #states.limit(20)
    totalStates = states.count()
    #print("Total States:" +  str(totalStates))
    _npd = []
    _npy = []
    _ndx = []
    
    for idx, state in enumerate(states) :
        d, y = prepareData(state, idx, totalStates)
        _npd.append(d)        
        _npy.append(y)        
        _ndx.append([d.shape, y.shape])
    data = np.array([ d for d in _npd])
    npy = np.array([ y for y in _npy])
    print ("saving..", os.path.join(init.datapath, (Id + '_data.npy')))
    np.save(os.path.join(init.datapath, (Id + '_data.npy')), data)
    np.save(os.path.join(init.datapath, (Id + '_index.npy')), np.array(_ndx))
    _file_list.append(Id + '_data.npy')
    _file_list.append(Id + '_index.npy')
#    print("npy.shape:", npy.shape)
#    #To place the patterns as a squre group of 60 x 60
#    for y in npy:
#        y = y.transpose()
    
    npy = np.concatenate([ y for y in npy])
#    print(npy.shape)
    
    train_images = npy.reshape(npy.shape[0], 6 , 6, 1)[:int(npy.shape[0]/100 * 80)]
    test_images =  npy.reshape(npy.shape[0], 6 , 6, 1)[int(npy.shape[0]/100 * 80) + 1:]
    
    print ("saving..", os.path.join(init.datapath, (Id + 'train_images.npy')))
    np.save(os.path.join(init.datapath, (Id + 'train_images.npy')), train_images)
    print ("saving..", os.path.join(init.datapath, (Id + 'test_images.npy')))
    np.save(os.path.join(init.datapath, (Id + 'test_images.npy')), test_images)
    _file_list.append(Id + 'train_images.npy')
    _file_list.append(Id + 'test_images.npy')
    #col 3 is dydx
    trip_minmax = np.array([ [np.ma.min(x[3]),  
               np.ma.max(x[3]) ]  for x in npy])
        
    #_min = np.ma.average(trip_minmax.transpose()[0])
    #_max = np.ma.average(trip_minmax.transpose()[1]) 
    #train_labels = np.array([categorize(x, _min, _max) for x in trip_minmax[:int(npy.shape[0]/100 * 80)] ])
    #test_labels  = np.array([categorize(x, _min, _max)  for x in trip_minmax[int(npy.shape[0]/100 * 80) + 1:] ])    
    
    _min = -3.5
    _max =  3.5
    
    train_labels = np.array([categorize(x, _min, _max) for x in trip_minmax[:int(npy.shape[0]/100 * 80)] ])
    test_labels  = np.array([categorize(x, _min, _max)  for x in trip_minmax[int(npy.shape[0]/100 * 80) + 1:] ])
    
    u, c = np.unique(np.array(train_labels), return_counts=True)    
    print("train_labels uniques:", np.stack([u, c]).T)
    u, c = np.unique(np.array(test_labels), return_counts=True)    
    print("test_label uniques:", np.stack([u, c]).T)
           
    print ("saving..", os.path.join(init.datapath, (Id + 'train_labels.npy')))
    np.save(os.path.join(init.datapath, (Id + 'train_labels.npy')), train_labels)
    print ("saving..", os.path.join(init.datapath, (Id + 'test_labels.npy')))
    np.save(os.path.join(init.datapath, (Id + 'test_labels.npy')), test_labels)
    _file_list.append(Id + 'test_labels.npy')
    _file_list.append(Id + 'test_labels.npy')

    print ("verifying..")
    print(npy.shape)
    print(npy[0].shape)
    
    for i in range(0, len(npy)):
        if (npy[i].shape != npy[0].shape):
            print(i, str(npy[i].shape))

client.close()
#archive_files(_file_list)