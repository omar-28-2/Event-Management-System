from django.utils.timezone import make_aware
from datetime import datetime

class EventModelTest(TestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create(
            name="Test Vendor", 
            email="vendor@example.com"
        )
        self.event = Event.objects.create(
            name="Sample Event",
            description="A test description",
            date=make_aware(datetime(2024, 12, 31, 10, 0, 0)),  # Timezone-aware datetime
            location="Test Location",
            number_of_seats=100,
            price=25.50,
            vendor_id=self.vendor.id,
        )

    def test_event_creation(self):
        self.assertEqual(self.event.name, "Sample Event")
