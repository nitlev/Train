from mock import MagicMock

from train.episode import Episode
from train.recorder import Recorder
from train.state import State


class TestRecorder:
    def test_recorder_should_have_one_more_transition_after_to_states(self):
        # Given
        recorder = Recorder()
        episode = Episode(None, "ID")
        state1 = MagicMock(State)
        state2 = MagicMock(State)

        # When
        recorder.record(episode)
        recorder.record_state(state1)
        recorder.record_state(state2)

        # Assert
        assert len(list(recorder.all_transitions)) == 1
