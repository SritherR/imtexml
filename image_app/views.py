from django.http import HttpResponse 
from django.shortcuts import render, redirect 
import pytesseract
from PIL import Image
import numpy as np
from .forms import *
  
# Create your views here. 
def hotel_image_view(request): 
    
  
    if request.method == 'POST': 
        form = HotelForm(request.POST, request.FILES) 
      
  
        if form.is_valid(): 
            form.save()
        
            return redirect('success') 
    else: 
        form = HotelForm() 
        
        context={'form' : form}

    return render(request, 'im.html', {'form' : form}) 
  
  
def success(request): 
    Hotels=Hotel.objects.all()
    src_path=r"C:/Users/A1029500/imgupload"
    pytesseract.pytesseract.tesseract_cmd = r'C:/Users/A1029500/imgupload/tesseract/Tesseract-OCR/tesseract.exe'
    #rint(Hotels.values())
    Hotels=Hotels[len(Hotels)-1]
    
    if request.method == 'GET': 
  
        # getting all the objects of hotel. 
        print(Hotels.name)
        print(Hotels.Image.url)
        path=Hotels.Image.url
        #print(src_path+path)
        result=pytesseract.image_to_string(Image.open(src_path+path))
        print("result",result)
        context={'Hotels':Hotels,'result':result}
    return render(request,'vi.html',context)


   
# =============================================================================
#     
#     context={}
#     return render(request,'vi.html',context)    
# =============================================================================
