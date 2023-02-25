from django import forms
from APP_ESPORTS.models import *
class RaceTypeForm(forms.ModelForm):
    class Meta:
        gender = [('ชาย'),('หญิง')]
        model = TypeList
        fields = ('nameType', 'gender')

        widgets = {
            'nameType': forms.TextInput(attrs={'class': 'form-control',  'size':55, 'maxlength':50}),
            'gender': forms.Select(choices=gender),
        }
        labels = {
            'nameType': 'ประเภทการแข่ง',
            'gender': 'เพศ',
        }

    def updateForm(self):
        self.fields['nameType'].widget.attrs['readonly'] = True
        self.fields['gender'].widget.attrs['readonly'] = True
    def deleteForm(self):
        self.fields['nameType'].widget.attrs['readonly'] = True
        self.fields['desc'].widget.attrs['readonly'] = True

class Director(forms.ModelForm): #กรรมการ
    class Meta:
        GENDER = (
            ("male", "male"),
            ("female", "female"),
        )
        model = Director
        fields = ('name', 'gender','birthdate','tel','address')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',  'size':55, 'maxlength':50}),
            'gender': forms.Select(choices=GENDER, attrs={'class': 'form-control'}),
            'birthdate':forms.NumberInput(attrs={'class': 'form-control',   'type': 'date'}),
            'tel': forms.TextInput(attrs={'class ': 'form-control', 'size': 55, 'maxlength': 50}),
            'address': forms.TextInput(attrs={'class ': 'form-control', 'size': 200, 'maxlength': 50}),

        }
        labels = {
            'name': 'ชื่อกรรมการ',
            'gender': 'เพศ',
            'birthdate': 'วันเกิด',
            'tel': 'เบอร์โทร',
            'address': 'ที่อยู่',
        }

    def deleteForm(self):
        self.fields['name'].widget.attrs['readonly'] = True
        self.fields['gender'].widget.attrs['readonly'] = True
        self.fields['birthdate'].widget.attrs['readonly'] = True
        self.fields['tel'].widget.attrs['readonly'] = True
        self.fields['address'].widget.attrs['readonly'] = True

class AgeCategory(forms.ModelForm): #ประเภทอายุแข่ง
    class Meta:
        model = AgeCategory
        fields = ('name', 'desc')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',  'size':55, 'maxlength':50}),
            'desc': forms.TextInput(attrs={'class ': 'form-control', 'size': 55, 'maxlength': 50}),
        }
        labels = {
            'name': 'ชื่อประเภท',
            'desc': 'รายละเอียด',
        }

    def deleteForm(self):
        self.fields['name'].widget.attrs['readonly'] = True
        self.fields['desc'].widget.attrs['readonly'] = True

class Season(forms.ModelForm): #ประเภทอายุแข่ง
    class Meta:
        model = Season
        fields = ('name', 'desc')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',  'size':55, 'maxlength':50}),
            'desc': forms.TextInput(attrs={'class ': 'form-control', 'size': 55, 'maxlength': 50}),
        }
        labels = {
            'name': 'ชื่อประเภท',
            'desc': 'รายละเอียด',
        }

    def deleteForm(self):
        self.fields['name'].widget.attrs['readonly'] = True
        self.fields['desc'].widget.attrs['readonly'] = True

