# api_final
api final - приложение API, связывающее преставление публикаций, комментариев к публикациям, групп публикаций и пользователей с внешнеми приложениями. Приложение вариантивно в настрйоке и поддерживает расширение контента и его типов.

Установка:
Ссылка на репозиторий:

Установите виртуальное окружение:
python -n venv venv
Активация окружения:
source venv/Script/activate

Установить зависимости из файла requirements.txt:
python -m pip install --upgrade pip
pip install -r requirements.txt

Выполнить миграции:
python manage.py migrate

Запустить проект из директории yatube_api:
python manage.py runserver

Список доступных адресов, обрабатываемых API:
admin/
api/ v1/ ^posts/(?P<post_id>\d+)/comments/$ [name='comments-list']
api/ v1/ ^posts/(?P<post_id>\d+)/comments/(?P<pk>[^/.]+)/$ [name='comments-detail']
api/ v1/ ^posts/$ [name='post-list']
api/ v1/ ^posts/(?P<pk>[^/.]+)/$ [name='post-detail']
api/ v1/ ^groups/$ [name='group-list']
api/ v1/ ^groups/(?P<pk>[^/.]+)/$ [name='group-detail']
api/ v1/ ^follow/$ [name='follows-list']
api/ v1/ ^follow/(?P<pk>[^/.]+)/$ [name='follows-detail']
api/ v1/ ^users/$ [name='user-list']
api/ v1/ ^users\.(?P<format>[a-z0-9]+)/?$ [name='user-list']
api/ v1/ ^users/activation/$ [name='user-activation']
api/ v1/ ^users/activation\.(?P<format>[a-z0-9]+)/?$ [name='user-activation']
api/ v1/ ^users/me/$ [name='user-me']
api/ v1/ ^users/me\.(?P<format>[a-z0-9]+)/?$ [name='user-me']
api/ v1/ ^users/resend_activation/$ [name='user-resend-activation']
api/ v1/ ^users/resend_activation\.(?P<format>[a-z0-9]+)/?$ [name='user-resend-activation']
api/ v1/ ^users/reset_password/$ [name='user-reset-password']
api/ v1/ ^users/reset_password\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-password']
api/ v1/ ^users/reset_password_confirm/$ [name='user-reset-password-confirm']
api/ v1/ ^users/reset_password_confirm\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-password-confirm']
api/ v1/ ^users/reset_username/$ [name='user-reset-username']
api/ v1/ ^users/reset_username\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-username']
api/ v1/ ^users/reset_username_confirm/$ [name='user-reset-username-confirm']
api/ v1/ ^users/reset_username_confirm\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-username-confirm']
api/ v1/ ^users/set_password/$ [name='user-set-password']
api/ v1/ ^users/set_password\.(?P<format>[a-z0-9]+)/?$ [name='user-set-password']
api/ v1/ ^users/set_username/$ [name='user-set-username']
api/ v1/ ^users/set_username\.(?P<format>[a-z0-9]+)/?$ [name='user-set-username']
api/ v1/ ^users/(?P<id>[^/.]+)/$ [name='user-detail']
api/ v1/ ^users/(?P<id>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='user-detail']
api/ v1/ ^$ [name='api-root']
api/ v1/ ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']
api/ v1/ ^jwt/create/? [name='jwt-create']
api/ v1/ ^jwt/refresh/? [name='jwt-refresh']
api/ v1/ ^jwt/verify/? [name='jwt-verify']
redoc/ [name='redoc']