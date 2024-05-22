from rest_framework import serializers
from .models import User, Community, CommunityAdmin, Volunteer, Form, MemberSchema, Field, SchemaField, Value, Question, Option

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ['CommunityId', 'AdminId']

class CommunityAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityAdmin
        fields = ['AdminId']

class VolunteerSerializer(serializers.ModelSerializer):
    communities = CommunitySerializer(many=True, read_only=True)
    
    class Meta:
        model = Volunteer
        fields = ['id', 'name', 'email', 'communities']

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ['id', 'title', 'volunteer']

class MemberSchemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberSchema
        fields = ['CommunityId']

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ['id', 'SchemaId', 'QuestionId', 'type']

class SchemaFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchemaField
        fields = ['id', 'SchemaId', 'field']

class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = ['id', 'FieldId', 'value']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'title', 'hint', 'type', 'form']

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'text', 'question']