import json
import inspect

def array_object_to_json(array_object):
    array_json = []
    for objet in array_object:
        json_object = object_to_json(objet)
        array_json.append(json_object)
    #array_json_string = json.dumps(array_json)
    return array_json

def object_to_json(obj):
    if inspect.isclass(obj) or inspect.isfunction(obj):
        # Si l'objet est une classe ou une fonction, on ne peut pas le convertir en JSON
        raise TypeError("Unsupported type: {}".format(type(obj)))
    elif inspect.ismethod(obj) or inspect.ismethoddescriptor(obj):
        # Si l'objet est une méthode, on ne peut pas le convertir en JSON
        return None
    elif inspect.ismodule(obj):
        # Si l'objet est un module, on retourne son dictionnaire d'attributs
        return object_to_json(obj.__dict__)
    elif inspect.isroutine(obj):
        # Si l'objet est une fonction ou une méthode non liée, on ne peut pas le convertir en JSON
        return None
    elif isinstance(obj, (int, float, bool, str, type(None))):
        # Si l'objet est d'un type primitif, on le retourne tel quel
        return obj
    elif isinstance(obj, (list, tuple, set)):
        # Si l'objet est une liste, un tuple ou un ensemble, on convertit récursivement ses éléments en JSON
        return [object_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        # Si l'objet est un dictionnaire, on convertit récursivement ses valeurs en JSON
        return {key: object_to_json(value) for key, value in obj.items()}
    elif hasattr(obj, '__dict__'):
        # Si l'objet a un attribut __dict__, on convertit récursivement ses attributs en JSON
        return object_to_json(obj.__dict__)
    else:
        # Si l'objet est d'un type non pris en charge, on le convertit en chaîne de caractères
        return str(obj)
