import patoolib
import json


import json

def getJSON(filePathAndName):
    with open(filePathAndName, 'r') as fp:
        return json.load(fp)

json_data = open("Data/unpacked/products.jsonl", 'r')
for line in json_data :
    save_file = open('Data/unpacked/products_line.jsonl', 'w')
    save_file.write(line)
    save_file.close()
    json_obj = getJSON('Data/unpacked/products_line.jsonl')
    print (json_obj.get("epid", ""))
    print (json_obj.get("xm_id", ""))
############## Read Product_data ##############################
    prod_data = json_obj.get("product_data", "")
    print(prod_data['maturity_score'])
    print(prod_data['product_origin'])
############## Read Title ##############################
    title = prod_data['title']
    print (title['value'])
    print(title['score'])
############## Read categories ##############################
    categories_list = prod_data['categories']
    categories = (categories_list[0])
    print(categories['id'])
    print(categories['score'])
    #########################
    aspect = (prod_data['aspects'])
    for asp in aspect :
        print (asp)
        print(asp['key'])



