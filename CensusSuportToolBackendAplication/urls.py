from rest_framework.routers import DefaultRouter

from CensusSuportToolBackendAplication.api import CommunityAdminViewSet, CommunityViewSet, FieldViewSet, FormViewSet, MemberSchemaViewSet, OptionViewSet, QuestionViewSet, SchemaFieldViewSet, UserViewSet, ValueViewSet, VolunteerViewSet

 
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'communities', CommunityViewSet)
router.register(r'community-admins', CommunityAdminViewSet)
router.register(r'volunteers', VolunteerViewSet)
router.register(r'forms', FormViewSet)
router.register(r'member-schemas', MemberSchemaViewSet)
router.register(r'fields', FieldViewSet)
router.register(r'schema-fields', SchemaFieldViewSet)
router.register(r'values', ValueViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'options', OptionViewSet)

# Ensure you export the router
__all__ = ['router']
