from rest_framework.routers import DefaultRouter

from CensusSuportToolBackendAplication.api import CommunityAdminViewSet, CommunityViewSet, FieldViewSet, FormViewSet, MemberSchemaViewSet, OptionViewSet, QuestionViewSet, SchemaFieldViewSet, UserViewSet, ValueViewSet, VolunteerViewSet

 
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'communities', CommunityViewSet, basename='community')
router.register(r'community-admins', CommunityAdminViewSet, basename='community-admin')
router.register(r'volunteers', VolunteerViewSet, basename='volunteer')
router.register(r'forms', FormViewSet, basename='form')
router.register(r'member-schemas', MemberSchemaViewSet, basename='member-schema')
router.register(r'fields', FieldViewSet, basename='field')
router.register(r'schema-fields', SchemaFieldViewSet, basename='schema-field')
router.register(r'values', ValueViewSet, basename='value')
router.register(r'questions', QuestionViewSet, basename='question')
router.register(r'options', OptionViewSet, basename='option')

# Ensure you export the router
__all__ = ['router']
