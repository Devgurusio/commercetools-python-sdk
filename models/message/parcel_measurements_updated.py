from .message import Message
from models.types.parcel_measurements import ParcelMeasurements


class ParcelMeasurementsUpdated(Message):
    type: 'ParcelMeasurementsUpdated'
    deliveryId: str
    parcelId: str
    measurements: ParcelMeasurements

    def __init__(self, type: str = 'ParcelMeasurementsUpdated', deliveryId: str = None, parcelId: str = None, measurements: ParcelMeasurements = None, **kwargs):
        super().__init__(**kwargs)
        self.deliveryId = deliveryId
        self.parcelId = parcelId
        if measurements is not None:
            if isinstance(measurements, dict):
                self.measurements = ParcelMeasurements(**measurements)
            else:
                self.measurements = measurements
