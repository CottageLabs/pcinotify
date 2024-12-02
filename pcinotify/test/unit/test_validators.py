from unittest import TestCase

from pcinotify import validate

class TestValidate(TestCase):
    def test_01_mailto(self):
        valid = [
            "mailto:dev@example.com",
            "mailto:dev.name@example.co.uk",
            "mailto:firstname+lastname@example.com",
            "mailto:email@123.123.123.123",
            "mailto:1234567890@example.com",
            "mailto:email@example.museum",
        ]

        invalid = [
            "email@example.com"
            "uri:email@example.com",
            "mailto:email",
            "mailto:email@",
            "mailto:email@example"
        ]

        for v in valid:
            validate.mailto(None, v)

        for v in invalid:
            with self.assertRaises(ValueError):
                validate.mailto(None, v)