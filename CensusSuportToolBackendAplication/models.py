from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group  # Import the Group model

class User(AbstractUser):
    ROLES = (
        ('AG', 'Administrador Global'),
        ('AC', 'Administrador de Comunidades'),
        ('V', 'Voluntario'),
    )
    role = models.CharField(max_length=2, choices=ROLES)
    phone = models.CharField(max_length=20)
    profession = models.CharField(max_length=100)
    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set')


class Community(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    administrators = models.ManyToManyField(User, related_name='communities_administered')

    def __str__(self):
        return self.name


class CensusTemplate(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    categories = models.ManyToManyField('Category')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Question(models.Model):
    TYPES = (
        ('SU', 'Selección única'),
        ('SM', 'Selección múltiple'),
        ('CB', 'Casillas de verificación'),
        ('TC', 'Texto corto'),
        ('TL', 'Texto largo'),
        ('D', 'Fecha'),
        ('H', 'Hora'),
        ('L', 'Escala Likert'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=TYPES)
    text = models.TextField()

    def __str__(self):
        return self.text


class CensusRecord(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(User, on_delete=models.CASCADE)
    census_template = models.ForeignKey(CensusTemplate, on_delete=models.CASCADE)
    completion_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.community.name} - {self.volunteer.username}"


class CensusResponse(models.Model):
    record = models.ForeignKey(CensusRecord, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.TextField()

    def __str__(self):
        return f"{self.record.community.name} - {self.question.text}"


class PermissionRequest(models.Model):
    volunteer = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    census_template = models.ForeignKey(CensusTemplate, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, default='Pending')  # Pending, Accepted, Rejected

    def __str__(self):
        return f"{self.volunteer.username} - {self.community.name}"


class Report(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title