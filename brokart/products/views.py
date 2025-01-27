from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def list_products(request):
    """_summary_
returns product list page
Args:
    request (_type_): description
Returns:
    _type_: description
"""

     
    return render(request,'products.html')

def detailed_product(request):
    return render(request,'product_deatails.html')

