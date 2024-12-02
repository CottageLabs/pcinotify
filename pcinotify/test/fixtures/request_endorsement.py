from copy import deepcopy

from coarnotify.test.fixtures import RequestEndorsementFixtureFactory


class PCIRequestEndorsementFixtureFactory(RequestEndorsementFixtureFactory):
    @classmethod
    def source(cls, copy=True):
        if copy:
            return deepcopy(REQUEST_ENDORSEMENT)
        return REQUEST_ENDORSEMENT


REQUEST_ENDORSEMENT = {
    "@context": [
        "https://www.w3.org/ns/activitystreams",
        "https://coar-notify.net"
    ],
    "actor": {
        "id": "mailto:josiah.carberry@example.com",
        "name": "Josiah Carberry",
        "type": "Person"
    },
    "id": "urn:uuid:0370c0fb-bb78-4a9b-87f5-bed307a509dd",
    "inReplyTo": "urn:uuid:0370c0fb-bb78-4a9b-87f5-bed307a509dd",
    "object": {
        "id": "https://research-organisation.org/repository/preprint/201203/421/",
        "ietf:cite-as": "https://doi.org/10.5555/12345680",
        "ietf:item": {
            "id": "https://research-organisation.org/repository/preprint/201203/421/content.pdf",
            "mediaType": "application/pdf",
            "type": [
                "Article",
                "sorg:ScholarlyArticle"
            ]
        },
        "type": [
            "Page",
            "sorg:AboutPage"
        ]
    },
    "origin": {
        "id": "https://research-organisation.org/repository",
        "inbox": "https://research-organisation.org/inbox/",
        "type": "Service"
    },
    "target": {
        "id": "https://evolbiol.peercommunityin.org/coar_notify/",
        "inbox": "https://evolbiol.peercommunityin.org/coar_notify/inbox/",
        "type": "Service"
    },
    "type": [
        "Offer",
        "coar-notify:EndorsementAction"
    ]
}
