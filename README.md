# Lavender
MongoDB Aggregation Class

MongoDB/aggregate.py is moudle for MongoDB Aggregation,it change operation easy and readable.



1,Class Pipeline(): construct pipeline for MongoDB Aggregation,such as $match,$group,$limit,unwind....
                  Note: sometimes you need special key, like '$_id' or 'eventValue.subValue',but '$','.' is invalid in              **kwargs's key. you should use '___' replace '$",use '__' replace '.' in this class and 
                         there is a method 'def __recover(self,arg)',could recoverd.
                  
    Example:

    p = Pipeline()
    p.limit(___limit=1000).match(city="Beijing",year__month=4).group(_id="$city",spots={"$push":"spot"})
    print p.get()

    you will get:
    [{'$limit': 1000}, {'$match': {'city': 'Beijing', 'year.month': 4}}, {'$group': {'_id': '$city', 'spots': {'$push': 'spot'}}}]



2,method aggregate(collection,pipeline,*keys) : excute collection.aggregate(pipeline) and return need lists with keys.
