from __future__ import unicode_literals
from django.db import models

class PetManager(models.Manager):
    def add_pet(self, form_data):
        print("Creating new pet")
        errors = []
        if len(form_data['name']) == 0:
            errors.append("Name cannot be empty")
        if len(form_data['description']) == 0:
            errors.append("Description cannot be empty")
        if len(form_data['name']) == 0:
            errors.append("Price must be set")
        if len(errors):
            print("validation errors")
            return (False, errors)
        else:
            print("passed validations")
            pet = Pet.objects.create(name=form_data['name'], description=form_data['description'], price=form_data['price'])
            return (True, pet)
    def edit_pet(self, form_data, id):
        print("editing pet with id {}".format('id'))
        errors = []
        if len(form_data['name']) == 0:
            errors.append("Name cannot be empty")
        if len(form_data['description']) == 0:
            errors.append("Description cannot be empty")
        if len(form_data['name']) == 0:
            errors.append("Price must be set")
        if len(errors):
            print("validation errors")
            return (False, errors)
        else:
            print("passed update validations")
            pet = Pet.objects.filter(id=id).update(name=form_data['name'], description=form_data['description'], price=form_data['price'])
            return (True, pet)

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PetManager()
