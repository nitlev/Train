from mock import MagicMock

from train.learning.state import State
from train.environment.episode import Episode
from train.environment.recorder import Recorder


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
        assert len(list(recorder.all_states)) == 2
