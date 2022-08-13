
from django.shortcuts import render
from rest_framework.response import Response
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .serializers import Eventserializer
from .models import Events
from rest_framework import status
from rest_framework.views import APIView

class home(APIView):
    def get(self,resquest):
        return Response({'events':{'msg':'Hey Welcome! Here you can post and update ur events '},'links':{'/event':'to get all the events','/event/category or place ':'To search event with category or place','/edit':'edit event','delete/<int:id>':'delete event'},'Post event':{'Add':{'category':' ','Place':' ','date':'YYYY-MM-DD','time':'hour:min'}}})

    
    def post(self,request):
        print(request.data)
        creation=Eventserializer(data=request.data)
        if creation.is_valid():
            creation.save()
            return Response({'msg':'your event has been added!!'},status=status.HTTP_201_CREATED)
        return Response({'msg':creation.errors},status=status.HTTP_403_FORBIDDEN)
    
    
class Eventhandle(APIView):
    def get(self,request,category=None):
        if category is not None:
            try:
                partevent=Events.objects.filter(Q(type=category)|Q(Place=category))
                serializer=Eventserializer(partevent,many=True)
                return Response(serializer.data,status=status.HTTP_302_FOUND)
            except:
                event=Events.objects.all()
                serializer=Eventserializer(event,many=True)
                return Response({'msg':'pls check category or place carefully','select category or place from ':serializer.data},status=status.HTTP_302_FOUND)
        allevent=Events.objects.all()
        serializer=Eventserializer(allevent,many=True)
        return Response({'msg':'To search event by category enter category or place name in url!!!','data':serializer.data},status=status.HTTP_302_FOUND)
    
class Editevent(APIView):
    def get(self,request,id=None):
        if id is not None:
            try:
                editableevent=Events.objects.get(id=id)
                serializer=Eventserializer(editableevent)
                return Response({'msg':serializer.data},status=status.HTTP_202_ACCEPTED)
            except:
                event=Events.objects.all()
                serializer=Eventserializer(event,many=True)
                return Response({'msg':'pls check id carefully','select id from ':serializer.data},status=status.HTTP_302_FOUND)
        event=Events.objects.all()
        serializer=Eventserializer(event,many=True)
        return Response({'msg':'To search event by category enter category or place name in url!!!','data':serializer.data},status=status.HTTP_302_FOUND)
    
    def put(self,request,id=None):
        if id is not None:
            try:
                editableevent=Events.objects.get(id=id)
                serializer=Eventserializer(editableevent,data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'msg':'Event has been updated'},status=status.HTTP_202_ACCEPTED)
                return Response({'msg':serializer.errors},status=status.HTTP_403_FORBIDDEN)
            except:
                event=Events.objects.all()
                serializer=Eventserializer(event,many=True)
                return Response({'msg':'pls check id carefully','select id from ':serializer.data},status=status.HTTP_302_FOUND)

    
        
class Deleteevent(APIView):
 def delete(self,request,id):
        try:
            delevent=Events.objects.filter(id=id)
            delevent.delete()
            return Response({'msg':'Event deleted successfully!!!'},status=status.HTTP_302_FOUND)
        except:
            event=Events.objects.all()
            serializer=Eventserializer(event,many=True)
            return Response({'msg':'pls check id carefully','select id from ':serializer.data},status=status.HTTP_302_FOUND)
        