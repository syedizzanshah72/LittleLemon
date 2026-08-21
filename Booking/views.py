from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer,RegisterSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer



class BookingViewSet(viewsets.ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

        
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

