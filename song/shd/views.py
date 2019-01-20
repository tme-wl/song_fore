from django.shortcuts import render
from django.http import HttpResponse
import json
from shd.models import Tags, Element
from django.forms.models import model_to_dict


def response_json(data):
    return HttpResponse(json.dumps(data), content_type="application/json")

def response_error(msg):
    data = {
        "status":500,
        "msg":msg
    }
    return response_json(data)

# Create your views here.
def tagslist(request):
    if request.method == 'GET':
        tags = Tags.objects.all()
        return_data = []
        for tag in tags:
            return_data.append({"name":tag.name,"id":tag.id})
        data = {
            "status":200,
            "data":return_data,
            "msg":"获取数据成功"
        }
    else:
        data = {
            "method":"others"
        }
    return response_json(data)

def element(request):
    if request.method == "POST":
        request_data = json.loads(request.body)
        tag_id =  int(request_data.get("tag_id", 0))
        if not tag_id:
            return response_error("传入tag id错误")
        start = int(request_data.get("start", 0))
        length = int(request_data.get("length", 10))
        alls = int(request_data.get("alls", 0))
        objs = Element.objects.filter(tags_id=tag_id)
        if not alls:
            objs = objs[start:length+start]
        return_data = []
        for obj in objs:
            temp = model_to_dict(obj, exclude=["tags"])
            return_data.append(temp)
        data = {
            "msg":"获取数据成功",
            "status":200,
            "data": return_data
        }
        return response_json(data)
    if request.method == "PUT":
        request_data = json.loads(request.body)
        tag_id =  int(request_data.get("tag_id", 0))
        if not tag_id:
            return response_error("传入tag id错误")
        mine = request_data.get("mine", '')
        whant = request_data.get("whant", '')
        liaotianbao_id = request_data.get("liaotianbao_id", '')
        info = request_data.get("info", "")
        if (not mine) or (not whant) or (not liaotianbao_id):
            return response_error("传入数据错误")
        obj = Element()
        obj.mine = mine
        obj.whant = whant
        obj.liaotianbao_id = liaotianbao_id
        obj.info = info
        obj.tags_id = tag_id
        obj.save()
        return response_json({"msg":"ok","status":200})

    if request.method == "GET":
        return response_json({"msg":"ok"})