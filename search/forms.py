from django import forms

class FlightSearchForm(forms.Form):
    ORIGIN_CHOICES = [
        ('JFK', 'JFK'),
        ('DEL', 'DEL'),
        ('SYD', 'SYD'),
        ('BOM', 'BOM'),
        ('BNE', 'BNE'),
        ('BLR', 'BLR'),
    ]

    DESTINATION_CHOICES = [
        ('JFK', 'JFK'),
        ('DEL', 'DEL'),
        ('SYD', 'SYD'),
        ('LHR', 'LHR'),
        ('CDG', 'CDG'),
        ('DOH', 'DOH'),
        ('SIN', 'SIN'),
    ]

    CABIN_CHOICES = [
        ('Economy', 'Economy'),
        ('Business', 'Business'),
        ('First', 'First'),
    ]

    origin = forms.ChoiceField(choices=ORIGIN_CHOICES, label="Origin")
    destination = forms.ChoiceField(choices=DESTINATION_CHOICES, label="Destination")
    cabin = forms.ChoiceField(choices=CABIN_CHOICES, label="Cabin Selection")
