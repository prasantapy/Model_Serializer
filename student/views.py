from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student_model
from .serializers import student_serializer 
from rest_framework .renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator  # class based
from django.views import View

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class student_api(View):
    def get(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None:
            stu = Student_model.objects.get(id = id)
            serializers=student_serializer(stu)
            json_data = JSONRenderer().render(serializers.data)
            return HttpResponse(json_data,content_type='application/json')
        stu= Student_model.objects.all()
        serializers = student_serializer(stu, many=True)
        json_data = JSONRenderer().render(serializers.data) 
        return HttpResponse(json_data, content_type='application/json')
    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializers=student_serializer(data = pythondata)
        if serializers.is_valid():
    

             
            serializers.save()
            res ={'msg':'Data create'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializers.errors)
        return HttpResponse(json_data,content_type='application/json')

    def put(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student_model.objects.get(id=id)
        serializers=student_serializer(stu,data= pythondata,
        partial =True)
        if serializers.is_valid():
            serializers.save()
            res ={'msg':'Data Update'}

            json_data=JSONRenderer().render(res)
            return HttpResponse (json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializers.errors)
        return HttpResponse(json_data,content_type='application/json')
    def delete(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id = pythondata.get('id')
        stu=Student_model.objects.get(id =id)
        stu.delete()
        res={'msg':'data deleted'}
        #json_data = JSONRenderer().render(res)
        #return HttpResponse(json_data,content_type='application/json')
        return JsonResponse(res,safe=False)


        
