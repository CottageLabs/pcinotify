from coarnotify.patterns import AnnounceReview as COARAnnounceReview

class PCIAnnounceReview(COARAnnounceReview):

    @property
    def review_community(self):
        return self.actor

    @property
    def reviewed_resource_landing_page(self):
        ctx = self.context
        if ctx is not None:
            return ctx.id

    @property
    def reviewed_resource_cite_as(self):
        ctx = self.context
        if ctx is not None:
            return ctx.cite_as

    @property
    def review_url(self):
        obj = self.object
        if obj is not None:
            return obj.id