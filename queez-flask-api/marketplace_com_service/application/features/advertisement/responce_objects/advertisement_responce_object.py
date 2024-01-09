class AdvertisementResponse:
    def __init__(self, advertisement):
        self.header_id = advertisement.header_id
        self.publisher_id = advertisement.publisher_id
        self.time_period = advertisement.time_period
        self.is_active = advertisement.is_active
        self.coordinates = advertisement.coordinates
        self.wf_state_id = advertisement.wf_state_id
        self.date = advertisement.date
        self.user_id = advertisement.user_id
        self.package_id = advertisement.package_id
        self.customer = {
            'customer_id': advertisement.customer.customer_id,
            'name': advertisement.customer.name,
            'sys_user_id': advertisement.customer.sys_user_id
        }
        self.advertisement_package = {
            'package_id': advertisement.advertisement_package.package_id,
            'description': advertisement.advertisement_package.description,
            'number_of_add': advertisement.advertisement_package.number_of_add,
            'num_days': advertisement.advertisement_package.num_days,
            'is_active': advertisement.advertisement_package.is_active,
            'price': advertisement.advertisement_package.price
        }
        self.advertisement_details = [
            {
                'advertisement_details_id': detail.advertisement_details_id,
                'add_id': detail.add_id,
                'filter_id': detail.filter_id,
                'value': detail.value
            }
            for detail in advertisement.advertisement_details
        ]
        self.image_details = [
            {
                'image_details_id': image.image_details_id,
                'image_url': image.image_url,
                'transec_ref_id': image.transec_ref_id
            }
            for image in advertisement.image_details
        ]
        self.workflow_history = [
            {
                'workflow_history_id': history.workflow_history_id,
                'transec_ref_id': history.transec_ref_id,
                'state_id': history.state_id,
                'state': history.state,
                'transection_type': history.transection_type
            }
            for history in advertisement.workflow_history
        ]

    def to_dict(self):
        return {
            'header_id': self.header_id,
            'publisher_id': self.publisher_id,
            'time_period': self.time_period,
            'is_active': self.is_active,
            'coordinates': self.coordinates,
            'wf_state_id': self.wf_state_id,
            'date': self.date,
            'user_id': self.user_id,
            'package_id': self.package_id,
            'customer': self.customer,
            'advertisement_package': self.advertisement_package,
            'advertisement_details': self.advertisement_details,
            'image_details': self.image_details,
            'workflow_history': self.workflow_history
        }

