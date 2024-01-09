from ..valueobjects.id import Id
from ..valueobjects.state import State
from ..valueobjects.transection_type import TransectionType


class WorkflowHistory:
    def __init__(self, workflow_history_id: Id, transec_ref_id: Id,
                 state_id:Id, state: State, transection_type: TransectionType):
        self.workflow_history_id = workflow_history_id
        self.transec_ref_id = transec_ref_id
        self.state_id = state_id
        self.state = state
        self.transection_type = transection_type
