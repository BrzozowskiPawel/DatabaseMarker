import json

# This function requaire a BoundingBox objec.

# TODO: What is in dict but not in BoundingBox class -> split, width,height (of photo)
def crete_JSON_labels(list_of_BoundingBox):
    for item in list_of_BoundingBox:
        # List of JSONs
        list_of_JSONs = []
        # Data to be written (created for each BoundingBox object)
        dict_to_JSON = {
            "name" : "test_name",
            "split" : "test",
            "annotation" : {
                "key" : "brbthn56.jpg",
                "boxes": [{
                    "label": "cyclist",
                    "x":328.5,
                    "y":235.5,
                    "width":152.0,
                    "height":269.5
                          }],
                "width":416,
                "height":416,
            }
        }
        list_of_JSONs.append(dict_to_JSON)
    for single_JSON in list_of_JSONs:
        # TODO: add destination of saving
        # Serializing json
        json_object = json.dumps(single_JSON, indent=4)

        # Writing to sample.json
        with open(dict_to_JSON["name"]+".json", "w") as outfile:
            outfile.write(json_object)


crete_JSON_labels(range(1))
