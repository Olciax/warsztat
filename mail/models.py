from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import validate_email
from django.urls import reverse

TYPE_NULL = 0
TYPE_OFFICE = 1
TYPE_PRIVATE = 2

TYPE = (
    (TYPE_NULL, "Nie określono"),
    (TYPE_OFFICE, "Służbowy"),
    (TYPE_PRIVATE, "Prywatny"),

)


class Address(models.Model):
    street = models.CharField(max_length=64)
    numofstreet = models.PositiveSmallIntegerField(null=True)
    numofhouse = models.TextField(max_length=5, null=True, blank=True)
    city = models.CharField(max_length=64)
    postalcode = models.CharField(max_length=6, null=True, blank=True,
                                  help_text=("Kod pocztowy"),
                                  validators=[RegexValidator(
                                      regex=r'^(^[0-9]{2}(?:-[0-9]{3})?$|^$)',
                                      message=('Kod musi mieć format xx-xxx'),
                                  )])

    def __str__(self):
        if self.numofhouse:
            return f"""ul.{self.street} {self.numofstreet}/{self.numofhouse}
                {self.postalcode} {self.city}"""
        else:
            return f"""ul.{self.street} {self.numofstreet}
                {self.postalcode} {self.city}"""


class Person(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    description = models.TextField()
    address = models.ForeignKey('Address', models.SET_NULL, blank=True, null=True)

    class Meta:
        order_with_respect_to = 'surname'

    def get_absolute_url(self):
        return reverse('details', kwargs={'person_id': self.pk})

    def __str__(self):
        return f'{self.surname} {self.name}'


class Telephone(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    number_regex = RegexValidator(regex=r'^\d{9}$', message="Numer musi mieć format 9 cyfr.")
    number = models.CharField(validators=[number_regex], max_length=12, blank=True, unique=True,
                              help_text=('Numer w formacie 9cyfrowym'))
    type = models.IntegerField(choices=TYPE, default=0)

    def __str__(self):
        return f'Tel.{self.type}: {self.number}'


class Email(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    email = models.EmailField(max_length=128, blank=False, unique=True, validators=[validate_email],
                              help_text=('Np. abc@xyz.com'))
    type = models.IntegerField(choices=TYPE, default=0)

    def __str__(self):
        return f'{self.email}, {self.type}'

# Create your models here.
