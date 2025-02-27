from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from magic_link import urls as magic_link_urls

from .redbox_core import views

auth_urlpatterns = [
    path("magic_link/", include(magic_link_urls)),
    path("sign-in/", views.sign_in_view, name="sign-in"),
    path(
        "sign-in-link-sent/",
        views.sign_in_link_sent_view,
        name="sign-in-link-sent",
    ),
    path("signed-out/", views.signed_out_view, name="signed-out"),
]

info_urlpatterns = [
    path("privacy-notice/", views.info_views.privacy_notice_view, name="privacy-notice"),
    path(
        "accessibility-statement/",
        views.accessibility_statement_view,
        name="accessibility-statement",
    ),
    path("support/", views.support_view, name="support"),
]

file_urlpatterns = [
    path("documents/", views.DocumentView.as_view(), name="documents"),
    path("upload/", views.UploadView.as_view(), name="upload"),
    path("remove-doc/<uuid:doc_id>", views.remove_doc_view, name="remove-doc"),
]

chat_urlpatterns = [
    path("chats/<uuid:chat_id>/", views.ChatsView.as_view(), name="chats"),
    path("chats/", views.ChatsView.as_view(), name="chats"),
    path("chat/<uuid:chat_id>/title/", views.ChatsTitleView.as_view(), name="chat-titles"),
    path("post-message/", views.post_message, name="post-message"),
    path("citations/<uuid:message_id>/", views.CitationsView.as_view(), name="citations"),
    path("ratings/<uuid:message_id>/", views.RatingsView.as_view(), name="ratings"),
]

admin_urlpatterns = [
    path("admin/", admin.site.urls),
]

other_urlpatterns = [
    path("", views.homepage_view, name="homepage"),
    path("health/", views.health, name="health"),
    path("file-status/", views.file_status_api_view, name="file-status"),
    path("check-demographics/", views.CheckDemographicsView.as_view(), name="check-demographics"),
    path("demographics/", views.DemographicsView.as_view(), name="demographics"),
    path(".well-known/security.txt", views.SecurityTxtRedirectView.as_view(), name="security.txt"),
    path("security", views.SecurityTxtRedirectView.as_view(), name="security"),
    path("sitemap", views.misc_views.sitemap_view, name="sitemap"),
]

urlpatterns = (
    info_urlpatterns + other_urlpatterns + auth_urlpatterns + chat_urlpatterns + file_urlpatterns + admin_urlpatterns
)

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
