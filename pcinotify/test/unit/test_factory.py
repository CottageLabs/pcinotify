from unittest import TestCase
from pcinotify.factory import COARNotifyFactory
from pcinotify.patterns import (
    PCIAnnounceReview,
    PCIAnnounceEndorsement,
    PCIRequestEndorsement
)
from coarnotify.test.fixtures import (
    AnnounceEndorsementFixtureFactory,
    AnnounceReviewFixtureFactory,
    RequestEndorsementFixtureFactory
)

class TestFactory(TestCase):
    def test_01_announce_endorsement(self):
        ae = COARNotifyFactory.get_by_types(PCIAnnounceEndorsement.TYPE)
        assert ae == PCIAnnounceEndorsement

        source = AnnounceEndorsementFixtureFactory.source()
        ae = COARNotifyFactory.get_by_object(source)
        assert isinstance(ae, PCIAnnounceEndorsement)

        assert ae.id == source["id"]

    def test_02_announce_review(self):
        ae = COARNotifyFactory.get_by_types(PCIAnnounceReview.TYPE)
        assert ae == PCIAnnounceReview

        source = AnnounceReviewFixtureFactory.source()
        ae = COARNotifyFactory.get_by_object(source)
        assert isinstance(ae, PCIAnnounceReview)

        assert ae.id == source["id"]

    def test_03_request_endorsement(self):
        ae = COARNotifyFactory.get_by_types(PCIRequestEndorsement.TYPE)
        assert ae == PCIRequestEndorsement

        source = RequestEndorsementFixtureFactory.source()
        ae = COARNotifyFactory.get_by_object(source)
        assert isinstance(ae, PCIRequestEndorsement)

        assert ae.id == source["id"]