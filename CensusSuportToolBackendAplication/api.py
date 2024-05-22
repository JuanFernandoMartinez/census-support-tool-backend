from rest_framework import viewsets, permissions
from .models import User, Community, CommunityAdmin, Volunteer, Form, MemberSchema, Field, SchemaField, Value, Question, Option
from .serializers import (
    UserSerializer, CommunitySerializer, CommunityAdminSerializer, VolunteerSerializer,
    FormSerializer, MemberSchemaSerializer, FieldSerializer, SchemaFieldSerializer,
    ValueSerializer, QuestionSerializer, OptionSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CommunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CommunityAdminViewSet(viewsets.ModelViewSet):
    queryset = CommunityAdmin.objects.all()
    serializer_class = CommunityAdminSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class FormViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MemberSchemaViewSet(viewsets.ModelViewSet):
    queryset = MemberSchema.objects.all()
    serializer_class = MemberSchemaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class FieldViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SchemaFieldViewSet(viewsets.ModelViewSet):
    queryset = SchemaField.objects.all()
    serializer_class = SchemaFieldSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ValueViewSet(viewsets.ModelViewSet):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

