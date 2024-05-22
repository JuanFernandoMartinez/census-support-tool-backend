from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    # Otros campos de usuario según sea necesario

class Community(models.Model):
    CommunityId = models.AutoField(primary_key=True, default=1)
    AdminId = models.ForeignKey('CommunityAdmin', on_delete=models.CASCADE, null=True)
    # Otros campos de Community

class CommunityAdmin(models.Model):
    AdminId = models.AutoField(primary_key=True)
    # Otros campos de CommunityAdmin

class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    communities = models.ManyToManyField(Community)
    # Otros campos de Volunteer según sea necesario

class Form(models.Model):
    title = models.CharField(max_length=100, default='')
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE, null=True)
    # Otros campos de Form

class MemberSchema(models.Model):
    CommunityId = models.OneToOneField(Community, on_delete=models.CASCADE)
    # Otros campos de MemberSchema

class Field(models.Model):
    TYPES = [
        ('numeric', 'Numeric'),
        ('text', 'Text'),
        ('date', 'Date'),
        ('boolean', 'Boolean'),
    ]
    SchemaId = models.ForeignKey(MemberSchema, on_delete=models.CASCADE)
    QuestionId = models.ForeignKey('Question', on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TYPES)
    # Otros campos de Field

class SchemaField(models.Model):
    SchemaId = models.ForeignKey(MemberSchema, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    # Otros campos de SchemaField

class Value(models.Model):
    FieldId = models.ForeignKey(Field, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)
    # Otros campos de Value

class Question(models.Model):
    title = models.CharField(max_length=255, default='')
    hint = models.CharField(max_length=255, default='')
    TYPE_CHOICES = [
        ('numeric', 'Numeric'),
        ('text', 'Text'),
        ('date', 'Date'),
        ('boolean', 'Boolean'),
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    form = models.ForeignKey(Form, on_delete=models.CASCADE, default=1)
    # Otros campos de Question

class Option(models.Model):
    text = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Otros campos de Option
