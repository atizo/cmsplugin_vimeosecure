from django.db import models
from django.utils.translation import ugettext as _
from cms.models import CMSPlugin
import settings

SECURE_SRC = ("https://secure.vimeo.com/moogaloop.swf?clip_id=%(video_id)d&amp;server=secure.vimeo.com&amp;"
              "title=%(title)d&amp;byline=%(byline)d&amp;portrait=%(portrait)d"
              "&amp;color=%(color)s&amp;fullscreen=1&amp;autoplay=%(autoplay)d&amp;loop=%(loop)d")
PLAYER_SRC = ("http://player.vimeo.com/video/%(video_id)d?color=%(color)s&amp;byline=%(byline)d&portrait=%(portrait)"
              "d&title=%(title)d&autoplay=%(autoplay)d&loop=%(loop)d")

class VimeoSecure(CMSPlugin):
    video_id = models.PositiveIntegerField(_('Video id'), 
        help_text=_('e.g http://vimeo.com/15189756'),
        max_length=60)
    color = models.CharField(default=settings.VIMEOSECURE_COLOR, max_length=6)    
    width = models.IntegerField(default=settings.VIMEOSECURE_WIDTH)
    height = models.IntegerField(default=settings.VIMEOSECURE_HEIGHT)
    title = models.BooleanField(default=settings.VIMEOSECURE_TITLE)
    portrait = models.BooleanField(default=settings.VIMEOSECURE_PORTRAIT)
    byline = models.BooleanField(default=settings.VIMEOSECURE_BYLINE)
    autoplay = models.BooleanField(_('Autoplay this video'), default=settings.VIMEOSECURE_AUTOPLAY)
    loop = models.BooleanField(_('Loop this video.'), default=settings.VIMEOSECURE_LOOP)    
    secure = models.BooleanField(default=settings.VIMEOSECURE_SECURE,
        help_text=_('Show video over HTTPS.'))

    def __unicode__(self):
        return u'<a href="http://vimeo.com/%(video_id)d">http://vimeo.com/%(video_id)d</a>' % {'video_id': self.video_id}
    __unicode__.allow_tags = True

    @property
    def src(self):
        if self.secure:
            return SECURE_SRC % self.__dict__        
        else:
            return PLAYER_SRC % self.__dict__