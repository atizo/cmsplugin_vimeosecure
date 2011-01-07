from django.conf import settings

VIMEOSECURE_COLOR = getattr(settings, 'VIMEOSECURE_COLOR', 'ffffff')
VIMEOSECURE_WIDTH = getattr(settings, 'VIMEOSECURE_WIDTH', 500)
VIMEOSECURE_HEIGHT = getattr(settings, 'VIMEOSECURE_HEIGHT', 375)
VIMEOSECURE_AUTOPLAY = getattr(settings, 'VIMEOSECURE_AUTOPLAY', False)
VIMEOSECURE_LOOP = getattr(settings, 'VIMEOSECURE_LOOP', False)
VIMEOSECURE_TITLE = getattr(settings, 'VIMEOSECURE_TITLE', True)
VIMEOSECURE_PORTRAIT = getattr(settings, 'VIMEOSECURE_PORTRAIT', True)
VIMEOSECURE_BYLINE = getattr(settings, 'VIMEOSECURE_BYLINE', False)
VIMEOSECURE_SECURE = getattr(settings, 'VIMEOSECURE_SECURE', True)

