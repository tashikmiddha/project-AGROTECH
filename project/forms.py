from django import forms


class CropPredictionForm(forms.Form):
    nitrogen = forms.FloatField(
        label='N',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter nitrogen level'})
    )
    phosphorus = forms.FloatField(
        label='P',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter phosphorus level'})
    )
    potassium = forms.FloatField(
        label='K',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter potassium level'})
    )
    temperature = forms.FloatField(
        label='Temperature',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter temperature in °C'})
    )
    humidity = forms.FloatField(
        label='Humidity',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter humidity in %'})
    )
    ph = forms.FloatField(
        label='pH',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter soil pH'})
    )
    rainfall = forms.FloatField(
        label='Rainfall',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter rainfall in mm'})
    )

class fertilizerForm(forms.Form):
    temperature = forms.FloatField(
        label='Temperature (°C)',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter temperature in °C'})
    )
    
    humidity = forms.FloatField(
        label='Humidity (%)',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter humidity in %'})
    )
    
    moisture = forms.FloatField(
        label='Soil Moisture (%)',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter soil moisture level'})
    )
    
    nitrogen = forms.FloatField(
        label='Nitrogen (N)',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter nitrogen level'})
    )
    
    potassium = forms.FloatField(
        label='Potassium (K)',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter potassium level'})
    )
    
    phosphorous = forms.FloatField(
        label='Phosphorous (P)',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter phosphorous level'})
    )

    soil_type = forms.ChoiceField(
        label='Soil Type',
        choices=[
            ('Clayey', 'Clayey'),
            ('Black', 'Black'),
            ('Red', 'Red'),
            ('Loamy', 'Loamy'),
            ('Sandy', 'Sandy')
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    crop_type = forms.ChoiceField(
        label='Crop Type',
        choices=[
            ('Sugarcane', 'Sugarcane'),
            ('Maize', 'Maize'),
            ('Wheat', 'Wheat'),
            ('Ground Nuts', 'Ground Nuts'),
            ('Pulses', 'Pulses'),
            ('Cotton', 'Cotton'),
            ('Millets', 'Millets'),
            ('Tobacco', 'Tobacco'),
            ('Oil seeds', 'Oil seeds'),
            ('Paddy', 'Paddy'),
            ('Barley', 'Barley')
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class wateringForm(forms.Form):
    nitrogen = forms.FloatField(
        label='N',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter nitrogen level'})
    )
    phosphorus = forms.FloatField(
        label='P',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter phosphorus level'})
    )
    potassium = forms.FloatField(
        label='K',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter potassium level'})
    )
    temperature = forms.FloatField(
        label='Temperature',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter temperature in °C'})
    )
    humidity = forms.FloatField(
        label='Humidity',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter humidity in %'})
    )
    water_level = forms.FloatField(
        label='waterlevel',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter soil pH'})
    )


from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message', 'rows': 6}),
        }
