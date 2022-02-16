'''
Note: To activate virtual environment from other folder . "C:\Users\Admin\Django Projects\djangovenv\scripts\activate"

JSON Data:

Python has built-in package called json, which is used to work with json data.
dumps(data) - It is used to convert python object into JSON string.

    import json
    python_dict = {'name':'Sonam','roll':101}
    json_data = json.dumps(python_dict)
    print(json_data)
    output-> {"name":"Sonam","roll":101}

loads(data) - This is used to parson json string.

    import json
    json_data = {"name":"Sonam","roll":101}
    python_dict = json.loads(json_data)
    print(python_dict)
    output-> {'name':'Sonam','roll':101}

Serializers:
    In django REST Framework, serializers are responisble for converting complex data such as querysets and model instances to
    native Python datatypes(called serialization) that can then be easily rendered into JSON, XML or other content types which
    is understandable by Front End.

    Serializers are also responsible for deserialization which means it allows parsed data to be converted back into complex
    data types, after first validating the incoming data.

Serializer class:
    A serializer class is very similar to a Django Form and ModelForm class, and includes similar validation flags on the
    various fields, such as required, max_length and default

    How to create Serializer Class?
    -> create a separate serializers.py file to write all serializers
    -> from rest_framework import serializers
    class StudentSerializer(serializers.Serializer):
        name = serializers.CharField(max_length = 100)
        roll = serializers.IntegerField()
        city = serializers.CharField(max_length = 100)

Serialization Steps:
    -> creating model instance stu
        stu = Student.objects.get(id=1)
    -> converting model instances stu to Python Dict / Serializing object
        serializer = StudentSerializer(stu)
    -> creating query set
        stu = Student.objects.all()
    -> Converting query set stu to List of python dict/ serializing query set
        serializer = StudentSerializer(stu, many=True)

JSON Renderer:
    -> This is used to render Serialized data into JSON which is understandable by Front End.
        importing JSONRenderer
        from rest_framework.renderers import JSONRenderer

        Render the data into JSON
        json_data =  JSONRenderer().render(serializer.data)

JSON Response:
    ->  JsonResponse(data, encoder = DjangoJSONEncoder, safe=True, json_dumps_params = None,**kwargs)
    ->  An HttpResponse subclass that helps to create a JSON-encoded response. It inherits most behaviour from its superclass
        with a couple differences.








'''