from django.forms import ModelForm

from main.models import *

from django.forms import widgets
from django.utils import six
from django import forms

from datetime import date




class EntryForm(ModelForm):

	class Meta:
		model=Entry
		fields='__all__'

	def clean(self):
		super(EntryForm, self).clean()
		Name=self.cleaned_data.get('Name')
		Quote=self.cleaned_data.get('Quote')
		if len(Name) <4 :
			self._errors['Name'] = self.error_class(['Minimum 4 characters Name required'])
		if len(Quote) <5 :
			self._errors['Quote'] = self.error_class(['Minimum length of quote should be 5'])
		return self.cleaned_data
