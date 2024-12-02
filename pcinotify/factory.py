from coarnotify.factory import COARNotifyFactory

from pcinotify.patterns.announce_review import PCIAnnounceReview
from pcinotify.patterns.announce_endorsement import PCIAnnounceEndorsement
from pcinotify.patterns.request_endorsement import PCIRequestEndorsement

# FIXME: this should be part of the coarnotify library
def register(model):
    existing = COARNotifyFactory.get_by_types(model.TYPE)
    if existing is not None:
        COARNotifyFactory.MODELS.remove(existing)
    COARNotifyFactory.MODELS.append(model)

register(PCIAnnounceReview)
register(PCIAnnounceEndorsement)
register(PCIRequestEndorsement)