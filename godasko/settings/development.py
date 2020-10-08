from godasko.settings.base import *

DEBUG = True

STATIC_ROOT = os.path.join(os.path.join(BASE_DIR,'static_cdn')) #burdaki cdn eklememiz işe yaradı acıkcası

STATICFILES_DIRS=[os.path.join(BASE_DIR,"static")] 
                        
                        
                          