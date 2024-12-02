from typing import Union

from coarnotify.core.notify import NotifyActor, NotifyProperties
from coarnotify.patterns import RequestEndorsement as COARRequestEndorsement
from coarnotify.exceptions import ValidationError
from coarnotify.core.activitystreams2 import Properties
from pcinotify.validate import add_rules, mailto

_ADDITIONAL_VALIDATION = {
    Properties.ID: {
        "context": {
            Properties.ACTOR: {
                "default": mailto
            }
        }
    }
}

class PCIRequestEndorsement(COARRequestEndorsement):

    def __init__(self, *args, **kwargs):
        super(PCIRequestEndorsement, self).__init__(*args, **kwargs)
        # FIXME: requires a setter in the coarnotify library
        self._validators = add_rules(self.validators, _ADDITIONAL_VALIDATION)

    @property
    def author(self):
        return self.actor

    @property
    def requested_resource_landing_page(self):
        obj = self.object
        if obj is not None:
            return obj.id

    @property
    def requested_resource_cite_as(self):
        obj = self.object
        if obj is not None:
            return obj.cite_as

    @property
    def actor(self) -> Union["PCIRequestEndorsementActor", None]:
        """Get the actor property of the notification"""
        a = self.get_property(Properties.ACTOR)
        if a is not None:
            return PCIRequestEndorsementActor(a,
                               validate_stream_on_construct=False,
                               validate_properties=self.validate_properties,
                               validators=self.validators,
                               validation_context=Properties.ACTOR,
                               properties_by_reference=self._properties_by_reference)
        return None

    def validate(self) -> bool:
        ve = ValidationError()
        try:
            super(PCIRequestEndorsement, self).validate()
        except ValidationError as superve:
            ve = superve

        self.required_and_validate(ve, Properties.ACTOR, self.actor)

        if ve.has_errors():
            raise ve
        return True

class PCIRequestEndorsementActor(NotifyActor):
    def validate(self) -> bool:
        ve = ValidationError()
        try:
            super(PCIRequestEndorsementActor, self).validate()
        except ValidationError as superve:
            ve = superve

        self.required(ve, NotifyProperties.NAME, self.name)

        if ve.has_errors():
            raise ve
        return True