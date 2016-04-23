# encoding: utf-8
'''
Created on 2016/4/22
@author: wangguojie
'''

class Pipeline:
    
    """ construct pipeline for MongoDB Aggregation"""
    
    def __init__(self):
        self.pipeline = []
        
    def match(self,**arg):
        self.pipeline.append({"$match":self.__recover(arg)})
        return self
    
    def group(self,**arg):
        self.pipeline.append({"$group":self.__recover(arg)})
        return self
    
    def unwind(self,**arg):
        self.pipeline.append({"$unwind":self.__recover(arg)})
        return self
        
    def project(self,**arg):
        self.pipeline.append({"$project":self.__recover(arg)})
        return self
    
    def sort(self,**arg):
        self.pipeline.append({"$sort":self.__recover(arg)})
        return self    
    
    def limit(self,**arg):
        self.pipeline.append(self.__recover(arg))
        return self  
    
    def get(self):
        return self.pipeline
    
    #  '___'    -->  '$', for first '___'
    #  '__'   -->  '.'
    def __recover(self,arg):
        for k in arg.keys():
            arg[k.replace('___','$',1).replace('__','.')] = arg.pop(k)
        return arg

# collection: datebase's collection
# pipeline: MongDB aggregate pipeline
# keys: key need to push or addToSet
# note: this aggregation assume unique '_id'.
def aggregate(collection,pipeline,*keys):
    result_list = []
    agg_list = list(collection.aggregate(pipeline))
    if len(agg_list) > 0:
        for key in keys:
            result_list.append(agg_list[0][key])
    else:
        result_list.append([])
    return result_list