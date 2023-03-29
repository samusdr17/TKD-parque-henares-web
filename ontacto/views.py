from django.shortcuts import redirect, render
from .forms import FormularioOntacto

from django.core.mail import EmailMessage
# Create your views here.

def ontacto(request):
    fomulario_ontacto = FormularioOntacto()

    if request.method == "POST":
        formulario_ontacto = FormularioOntacto(data=request.POST)
        
        if formulario_ontacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email = EmailMessage("Mensaje desde App Django",
            " {}, {}, Mensaje:\n\n {}".format(nombre, email, contenido),
            "",["samusdr27@gmail.com"],reply_to=[email])

            try:
                email.send()
                return redirect("/ontacto/?valido")
            except:
                return redirect("/ontacto/?novalido")


    return render(request, "ontacto/ontacto.html", {'miFormulario': fomulario_ontacto})