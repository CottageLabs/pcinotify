from unittest import TestCase
from copy import deepcopy

from coarnotify.test.fixtures import (
    AnnounceEndorsementFixtureFactory,
    AnnounceReviewFixtureFactory
)

from pcinotify.patterns import (
    PCIAnnounceEndorsement,
    PCIAnnounceReview,
    PCIRequestEndorsement
)

from pcinotify.test.fixtures import (
    PCIRequestEndorsementFixtureFactory
)

class TestModels(TestCase):
    # FIXME: these should be importable from the coarnotify library
    def _get_testable_properties(self, source, prop_map=None):
        def expand(node, path):
            paths = []
            for k, v in node.items():
                if isinstance(v, dict):
                    paths += expand(v, f"{path}.{k}")
                else:
                    paths.append(f"{path}.{k}")
            paths = [p[1:] if p.startswith(".") else p for p in paths if "@context" not in p]  # strip the leading "."
            return paths

        obj_properties = expand(source, "")

        if prop_map is None:
            prop_map = {
                "inReplyTo": "in_reply_to",
                "context.ietf:cite-as": "context.cite_as",
                "context.ietf:item.id": "context.item.id",
                "context.ietf:item.mediaType": "context.item.media_type",
                "context.ietf:item.type": "context.item.type",
                "object.as:subject": "object.triple[2]",
                "object.as:relationship": "object.triple[1]",
                "object.as:object": "object.triple[0]",
                "object.ietf:cite-as": "object.cite_as",
                "object.ietf:item.id": "object.item.id",
                "object.ietf:item.mediaType": "object.item.media_type",
                "object.ietf:item.type": "object.item.type",
                "object.object.ietf:cite-as": "object.object.cite_as",
                "object.object.ietf:item.id": "object.object.item.id",
                "object.object.ietf:item.mediaType": "object.object.item.media_type",
                "object.object.ietf:item.type": "object.object.item.type",
            }

        proptest = [p if p not in prop_map else (prop_map[p], p) for p in obj_properties]
        return proptest

    def _apply_property_test(self, proptest, obj, fixtures):
        def get_prop(source, prop):
            p = prop
            if isinstance(prop, tuple):
                p = prop[1]
            bits = p.split(".")
            for bit in bits:
                idx = None
                if "[" in bit:
                    bit, idx = bit.split("[")
                    idx = int(idx[:-1])
                source = getattr(source, bit)
                if idx is not None:
                    source = source[idx]
            return source

        for prop in proptest:
            if isinstance(prop, tuple):
                oprop = prop[0]
                fprop = prop[1]
            else:
                oprop = prop
                fprop = prop

            print(oprop, fprop)
            oval = get_prop(obj, oprop)
            eval = fixtures.expected_value(fprop)

            # allow a single value to be equivalent to a list containing a single value
            if isinstance(oval, list) and len(oval) == 1:
                oval = oval[0]
            if isinstance(eval, list) and len(eval) == 1:
                eval = eval[0]

            assert oval == eval, f"{oprop}:{oval} - {fprop}:{eval}"


    def test_01_announce_endorsement(self):
        ae = PCIAnnounceEndorsement()
        source = AnnounceEndorsementFixtureFactory.source()

        compare = deepcopy(source)
        ae = PCIAnnounceEndorsement(source)
        assert ae.validate() is True
        assert ae.to_jsonld() == compare

        # apply the general tests
        proptest = self._get_testable_properties(compare)
        self._apply_property_test(proptest, ae, AnnounceEndorsementFixtureFactory)

        customtest = [
            ("review_community.id", "actor.id"),
            ("endorsed_resource_landing_page", "context.id"),
            # Base fixture does not contain this field, so can't test it this way
            # ("endorsed_resource_cite_as", "context.ietf:cite-as"),
            ("endorsement_url", "object.id"),
            ("endorsement_cite_as", "object.ietf:cite-as")
        ]

        # apply our custom property tests
        self._apply_property_test(customtest, ae, AnnounceEndorsementFixtureFactory)

        ae.context.cite_as = "http://example.com/cite-as"
        assert ae.endorsed_resource_cite_as == "http://example.com/cite-as"

    def test_02_announce_review(self):
        ae = PCIAnnounceReview()
        source = AnnounceReviewFixtureFactory.source()

        compare = deepcopy(source)
        ae = PCIAnnounceReview(source)
        assert ae.validate() is True
        assert ae.to_jsonld() == compare

        # apply the general tests
        proptest = self._get_testable_properties(compare)
        self._apply_property_test(proptest, ae, AnnounceReviewFixtureFactory)

        customtest = [
            ("review_community.id", "actor.id"),
            ("reviewed_resource_landing_page", "context.id"),
            # Base fixture does not contain this field, so can't test it this way
            # ("reviewed_resource_cite_as", "context.ietf:cite-as"),
            ("review_url", "object.id")
        ]

        # apply our custom property tests
        self._apply_property_test(customtest, ae, AnnounceReviewFixtureFactory)

        ae.context.cite_as = "http://example.com/cite-as"
        assert ae.reviewed_resource_cite_as == "http://example.com/cite-as"

    def test_03_request_endorsement(self):
        ae = PCIRequestEndorsement()
        source = PCIRequestEndorsementFixtureFactory.source()

        compare = deepcopy(source)
        ae = PCIRequestEndorsement(source)
        assert ae.validate() is True
        assert ae.to_jsonld() == compare

        # apply the general tests
        proptest = self._get_testable_properties(compare)
        self._apply_property_test(proptest, ae, PCIRequestEndorsementFixtureFactory)

        customtest = [
            ("author.id", "actor.id"),
            ("requested_resource_landing_page", "object.id"),
            ("requested_resource_cite_as", "object.ietf:cite-as")
        ]

        # apply our custom property tests
        self._apply_property_test(customtest, ae, PCIRequestEndorsementFixtureFactory)
