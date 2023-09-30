from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordResetForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

DESIGNATION = (
        ('', ''),
        ('S3', 'Assistant'),
        ('S4', 'Senior Assistant'),
        ('S5', 'Senior Assistant'),
        ('S6', 'Senior Assistant'),
        ('S7', 'Senior Assistant'),
        ('E0', 'Senior Assistant'),
        ('E1', 'Engineer'),
        ('E1', 'Officer'),
        ('E2', 'Senior Engineer'),
        ('E2', 'Senior Officer'),
        ('E3', 'Manager'),
        ('E4', 'Senior Manager'),
        ('E5', 'Chief Manager'),
        ('E6', 'Dy. General Manager'),
        ('E7', 'General Manager'),
        ('E8', 'Chief General Manager'),
        ('E9', 'Executive Director')
    )
DEPARTMENT = (
        ('', ''),
        ('bis', 'BIS'),
        ('civil', 'CIVIL'),
        ('cnp', 'Contract & Procurement'),
        ('ele', 'Electrical'),
        ('fna', 'Finance & Accounts'),
        ('fns', 'Fire & Safety'),
        ('gailtel', 'GAILTEL'),
        ('hr', 'Human & Resource Development'),
        ('inst', 'Instrumentation'),
        ('mech', 'Mechanical'),
        ('ops', 'Operation'),
        ('onm', 'Operation & Maintenance'),
        ('pipeline', 'Pipeline'),
        ('sec', 'SECURITY')
    )

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label="",max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="",max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    mobile_number = forms.CharField(label="", min_length=10,max_length=10,help_text= '<span class="form-text text-muted"><small>Valid 10 Digit Phone Number</small></span>',widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mobile Number'}))
    designation = forms.CharField(label="",max_length=100, widget=forms.Select(choices=DESIGNATION,attrs={'class':'form-control'}))
    department = forms.CharField(label="",max_length=100, widget=forms.Select(choices=DEPARTMENT,attrs={'class':'form-control', 'placeholder':'Department'}))
    class Meta:
        model = User
        fields = ['email', 'username','first_name', 'last_name', 'designation','department','mobile_number', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']= 'form-control'
        self.fields['username'].widget.attrs['placeholder']= 'User Name'
        self.fields['username'].label= ''
        self.fields['username'].help_text= '<span class="form-text text-muted"><small>Auto creation of username.</small></span>'
        self.fields['username'].widget.attrs['readonly'] = True

        self.fields['email'].widget.attrs['class']= 'form-control'
        self.fields['email'].widget.attrs['placeholder']= 'E-mail Address'
        self.fields['email'].label= ''
        self.fields['email'].help_text= '<span class="form-text text-muted"><small>Valid e-mail id</small></span>'

        self.fields['password1'].widget.attrs['class']= 'form-control'
        self.fields['password1'].widget.attrs['placeholder']= 'Password'
        self.fields['password1'].label= ''
        self.fields['password1'].help_text= '<span class="form-text text-muted"><small>Your password must contain at least 8 characters. Your password can’t be entirely numeric.</small></span>'

        self.fields['password2'].widget.attrs['class']= 'form-control'
        self.fields['password2'].widget.attrs['placeholder']= 'Confirm Password'
        self.fields['password2'].label= ''
        self.fields['password2'].help_text= '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

  
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'
    

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']= 'form-control'
        self.fields['username'].widget.attrs['placeholder']= 'User Name'
        self.fields['username'].label= ''
        self.fields['username'].help_text= ''

        self.fields['password'].widget.attrs['class']= 'form-control'
        self.fields['password'].widget.attrs['placeholder']= 'Password'
        self.fields['password'].label= ''
        self.fields['password'].help_text= ''

class CustomPasswordResetForm(PasswordResetForm):
    class Meta:
        model = User
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(CustomPasswordResetForm, self).__init__(*args, **kwargs)
       
        self.fields['email'].widget.attrs['class']= 'form-control'
        self.fields['email'].widget.attrs['placeholder']= 'E-mail Address'
        self.fields['email'].label= ''
        self.fields['email'].help_text= '<span class="form-text text-muted"><small>Valid e-mail id</small></span>'
        