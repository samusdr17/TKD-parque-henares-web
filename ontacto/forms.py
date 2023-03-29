from django import forms


class FormularioOntacto(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    email = forms.CharField(label="Email", required=True)
    contenido = forms.CharField(label="Contenido", widget=forms.Textarea)


    nombre.widget.attrs.update({'class': 'special'})
    email.widget.attrs.update({'class': 'special'})
    contenido.widget.attrs.update({'class': 'specialBig'})