from coarnotify.patterns import AnnounceEndorsement as COARAnnounceEndorsement

class PCIAnnounceEndorsement(COARAnnounceEndorsement):

    @property
    def review_community(self):
        return self.actor

    @property
    def endorsed_resource_landing_page(self):
        ctx = self.context
        if ctx is not None:
            return ctx.id

    @property
    def endorsed_resource_cite_as(self):
        ctx = self.context
        if ctx is not None:
            return ctx.cite_as

    @property
    def endorsement_url(self):
        obj = self.object
        if obj is not None:
            return obj.id

    @property
    def endorsement_cite_as(self):
        obj = self.object
        if obj is not None:
            return obj.cite_as