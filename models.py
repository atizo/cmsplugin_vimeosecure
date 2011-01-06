from django.db import models
from django.utils.translation import ugettext as _
from cms.models import CMSPlugin
import settings

SECURE_SRC = ("http://secure.vimeo.com/moogaloop.swf?clip_id=%(video_id)d&amp;server=secure.vimeo.com&amp;"
              "show_title=%(show_title)d&amp;show_byline=%(show_byline)d&amp;show_portrait=%(show_portrait)d"
              "&amp;color=%(color)s&amp;fullscreen=1&amp;autoplay=%(autoplay)d&amp;loop=%(loop)d")
PLAYER_SRC = ("http://player.vimeo.com/video/%(video_id)d?color=%(color)s&amp;byline=%(show_byline)d&portrait=%(show_portrait)"
              "d&title=%(show_title)d&autoplay=%(autoplay)d&loop=%(loop)d")

class Vimeo(CMSPlugin):
    video_id = models.PositiveIntegerField(_('Video id'), 
        help_text=_('The video id is the number you see in the URL. e.g http://vimeo.com/17808185'),
        max_length=60)
    width = models.IntegerField(_('Width'), default=settings.CMS_VIMEO_DEFAULT_WIDTH)
    height = models.IntegerField(_('Height'), default=settings.CMS_VIMEO_DEFAULT_HEIGHT)
    autoplay = models.BooleanField(_('Autoplay'), default=settings.CMS_VIMEO_DEFAULT_AUTOPLAY)
    loop = models.BooleanField(_('Loop'), default=settings.CMS_VIMEO_DEFAULT_LOOP)
    show_title = models.BooleanField(default=settings.CMS_VIMEO_DEFAULT_SHOW_TITLE,
        help_text=_('Whether to show the (clickable) title in the beginning of the movie'))
    show_portrait = models.BooleanField(default=settings.CMS_VIMEO_DEFAULT_SHOW_PORTRAIT,
        help_text=_('Whether to show the authors icon in the beginning of the movie'))
    show_byline = models.BooleanField(default=settings.CMS_VIMEO_DEFAULT_SHOW_BYLINE,
        help_text=_('Whether to show the authors name in the beginning of the movie'))
    show_secure = models.BooleanField(default=settings.CMS_VIMEO_DEFAULT_SECURE,
        help_text=_('Whether to get the video over HTTPS'))

    def __unicode__(self):
        return u'<a href="http://vimeo.com/%s">http://vimeo.com/%s</a>' % (self.video_id, self.video_id)
    __unicode__.allow_tags = True

    @property
    def src(self):        
        src_dict = self.__dict__
        src_dict['color'] = settings.CMS_VIMEO_DEFAULT_TITLE_COLOR
        
        if self.show_secure:
            return SECURE_SRC % src_dict
        else:
            return PLAYER_SRC % src_dict