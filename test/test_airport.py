import unittest
from app.airport import Airport


class TestAiport(unittest.TestCase):

    def setUp(self):
        self.airport = Airport()

    def tearDown(self):
        pass

    def test_Airport_exists(self):
        self.assertEqual(self.airport, self.airport)

    def test_Airport_stores_planes(self):
        self.assertEqual(self.airport.planes, [])

    def test_Airport_confirms_plane_landed(self):
        self.assertEqual(self.airport.land("plane"), "plane has landed")

    def test_Airport_lands_plane_and_stores_it_in_planes(self):
        self.airport.land("plane")
        self.assertEqual(self.airport.planes, ["plane"])

    def test_Airport_instructs_plane_to_take_off(self):
        self.airport.land("plane")
        self.airport.takeoff("plane")
        self.assertEqual(self.airport.planes, [])

    def test_Airport_instructs_plane_to_take_off(self):
        self.airport.land("plane")
        self.assertEqual(self.airport.takeoff("plane"), "plane has taken off")

    def test_Airport
