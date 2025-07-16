from django.shortcuts import render,HttpResponse
from .forms import CropPredictionForm
from .load_model import predict_crop,predict_watering,predict_fertilizer
from .forms import wateringForm
from .forms import fertilizerForm
import numpy as np
# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')
def team(request):
    return render(request,'team.html')
def term(request):
    return render(request,'term.html')

def datasets(request):
    return render(request,'datasets.html')

def code(request):
    return render(request,'code.html')


def crop_predict_view(request):
    prediction = None
    x=['apple', 'banana', 'blackgram' ,'chickpea', 'coconut', 'coffee' ,'cotton',
       'grapes' ,'jute', 'kidneybeans', 'lentil', 'maize', 'mango' ,'mothbeans' ,
        'mungbean', 'muskmelon', 'orange', 'papaya' ,'pigeonpeas', 'pomegranate',
        'rice', 'watermelon']
    if request.method == 'POST':
        form = CropPredictionForm(request.POST)
        if form.is_valid():
            data = [
                form.cleaned_data['nitrogen'],
                form.cleaned_data['phosphorus'],
                form.cleaned_data['potassium'],
                form.cleaned_data['temperature'],
                form.cleaned_data['humidity'],
                form.cleaned_data['ph'],
                form.cleaned_data['rainfall'],
            ]
            prediction = x[predict_crop(data)]
            
   
    else:
        form = CropPredictionForm()

    return render(request, 'crop_prediction.html', {
        'form': form,
        'prediction': prediction
    })

def watering(request):
    prediction = None
    x=['NO','YES']
    if request.method == 'POST':
        form = wateringForm(request.POST)
        if form.is_valid():
            data = [
                form.cleaned_data['nitrogen'],
                form.cleaned_data['phosphorus'],
                form.cleaned_data['potassium'],
                form.cleaned_data['temperature'],
                form.cleaned_data['humidity'],
                form.cleaned_data['water_level'],
            ]
            prediction = x[predict_watering(data)]
            
   
    else:
        form = wateringForm()

    return render(request, 'watering.html', {
        'form': form,
        'prediction': prediction
    })

def encode_input(form_data):
    # Example for encoding categorical values (you may need to match your dataset's encoding)
    soil_types = ['Clayey', 'Loamy', 'Red', 'Sandy']
    crop_types = ['Cotton', 'Ground Nuts', 'Maize', 'Millets', 'Oil seeds', 'Paddy',
                  'Pulses', 'Sugarcane', 'Tobacco', 'Wheat']

    soil_encoded = [1 if form_data['soil_type'] == s else 0 for s in soil_types]
    crop_encoded = [1 if form_data['crop_type'] == c else 0 for c in crop_types]

    features = [
        form_data['temperature'],
        form_data['humidity'],
        form_data['moisture'],
        form_data['nitrogen'],
        form_data['potassium'],
        form_data['phosphorous'],
        *soil_encoded,
        *crop_encoded
    ]
    return features

def fertilizer_prediction(request):
    x=['10-26-26', '14-35-14', '17-17-17' ,'20-20' ,'28-28' ,'DAP' ,'Urea']
    if request.method == 'POST':
        form = fertilizerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            X_input = encode_input(data)
            prediction = x[predict_fertilizer(X_input)]
            return render(request, 'fertilizer_prediction.html', {'form': form, 'prediction': prediction})
    else:
        form = fertilizerForm()
    return render(request, 'fertilizer_prediction.html', {'form': form})
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
