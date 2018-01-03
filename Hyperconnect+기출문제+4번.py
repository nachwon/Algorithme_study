
# coding: utf-8

# In[1]:

'''
Implement the function sort_by_price_ascending, which:
    - Accepts a string in JSON format, as in the example below.
    - Orders items by price in ascending order.
    - If two products have the same price, it orders them by their name in alphabetical order.
    - Returns a string in JSON format that is equivalent to the one in the input format.

For example, the call

Products.sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]')

should return

'[{"name":"eggs","price":1},{"name":"rice","price":4.04},{"name":"coffee","price":9.99}]'
''' 


# In[78]:

class Products:
    
    @staticmethod
    def sort_by_price_ascending(json_string):
        import json
        data = json.loads(json_string)
        for i in range(len(data)-1):
            min_num = i
            for j in range(i+1, len(data)):
                if data[min_num]['price'] == data[j]['price']:
                    if data[min_num]['name'] > data[j]['name']:
                        min_num = j
                        data[i], data[min_num] = data[min_num], data[i]
                
                elif data[min_num]['price'] > data[j]['price']:
                    min_num = j
                    data[i], data[min_num] = data[min_num], data[i]
                
        return data
    


# In[80]:

Products.sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04},{"name":"apple","price":1.5}]')


# In[ ]:



