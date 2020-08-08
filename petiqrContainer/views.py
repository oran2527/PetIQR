from rest_framework import generics
from .models import Countries
from .serializers import CountriesSerializer

class CountriesAPIView(generics.ListCreateAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer