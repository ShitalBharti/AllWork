'''
->  Django's form functionality can simplify and automate vast portions of work.
    ->  Preparing and restructuring data to make it ready for rendering.
    ->  Creating HTML forms for the data.
    ->  Receiving and processing submitted forms and data from the client.

->  Bound and Unbound forms
    ->  Bound: It is set of data, it is capable of validating that data and rendering the form as HTML with data displayed
        in HTML.
    ->  Unbound: It cannot do validation, but it can still render the blank forms as HTML.

->  Steps to create Django forms:
    ->  forms.py (file name)
    Syntax: from django import forms
            class FormClassName(forms.Form):
                label = forms.FieldType()
                label = forms.FieldType(label = 'display_lable')
    Example:
            from django import forms
            class StudentRegisterForm(forms.Form):
                name =  forms.CharField()       # Length of fields is not required
                email = forms.EmailField()
    Views.py:
        ->  Object of Form class and pass object to template files
        ->  use Form object in template file

            from .forms import StudentRegisterForm
            def showformdata(request):
                fm = StudentRegisterForm()
                return render(request, 'userregister.html', {'form':fm})

    templates:
        userregister.html
            ->  <html>
                    <body>
                        <form method="Post>
                            {{ form }}
                            <button name='Submit'></button>
                        <\form>
                    </body>
                </html>

->  Form rendering options:
    ->  {{ form }}:                 will render them all
    ->  {{ form.as_table }}:        will render them as table cells wrapped in <tr> tag
    ->  {{ form.as_p }}:            will render them wrapped in <p> tag
    ->  {{ form.as_ul }}:           will render them wrapped in <li> tag
    ->  {{ form.name_of_field }}:   will render field manually as given


'''