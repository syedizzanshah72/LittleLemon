from django.test import TestCase
from .models import Booking
from django.contrib.auth.models import User


class BookingTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="ali", password="12345")
    
    def test_booking_create(self):
        Booking.objects.create(
            user=self.user,
            phoneNumber="03001234567",
            noOfGuests="4"
        )
        self.assertEqual(Booking.objects.count(), 1)


