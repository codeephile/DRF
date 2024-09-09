from rest_framework import generics
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
# deafult import for restframework
from crud.models import Booklist
from crud.serializers import BooklistSerializer
from django.shortcuts import get_object_or_404

#for list show
@api_view(['GET']) #use get method for show
@renderer_classes([JSONRenderer]) # change to JSON
@permission_classes([IsAuthenticated]) # close permission also can use Allowany
def book_list(request):
    booklist = Booklist.objects.all()
    serializer = BooklistSerializer(booklist, many=True)
    return Response (serializer.data)


#for create
@api_view(['POST']) # for create post method
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def book_create(request):
    serializer = BooklistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#for detail
@api_view(['GET'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def book_detail(request, pk):
    booklist = get_object_or_404(Booklist, pk=pk)
    serializer = BooklistSerializer(booklist)
    return Response(serializer.data)


#for update
@api_view(['PUT'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def book_update(request, pk):
    booklist = get_object_or_404(Booklist, pk=pk)
    serializer = BooklistSerializer(booklist, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#for delete
@api_view(['DELETE'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def book_delete(request, pk):
    booklist = get_object_or_404(Booklist, pk=pk)
    booklist.delete()
    return Response({'detail': 'book deleted successfully.'}, status=status.HTTP_200_OK)