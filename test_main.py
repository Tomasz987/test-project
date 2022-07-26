"""Collection of tests to mouse_listener module."""
from pynput.mouse import Listener

from tools.mouse_listener import RecordMouseEvents


def test_listener_start_record(mocker):
    """Test check if record method is called to Listener.join method."""
    mocker.patch.object(Listener, 'join')
    record_object = RecordMouseEvents()

    record_object.record()

    Listener.join.assert_called_once()


def test_passed_listener_arguments(mocker):
    """Test check passed arguments to create Listener."""
    mocker.patch.object(Listener, '__new__')
    mocker.patch.object(RecordMouseEvents, 'on_move')
    mocker.patch.object(RecordMouseEvents, 'on_click')
    mocker.patch.object(RecordMouseEvents, 'on_scroll')

    record_object = RecordMouseEvents()
    record_object.record()

    Listener.__new__.assert_called_once_with(
        Listener,
        on_move=record_object.events.append(record_object.on_move),
        on_click=record_object.events.append(record_object.on_click),
        on_scroll=record_object.events.append(record_object.on_scroll),
    )


def test_output_record(mocker):
    """Test check output record method"""
    mocker.patch.object(Listener, '__new__')
    mocker.patch.object(RecordMouseEvents, 'on_move')
    mocker.patch.object(RecordMouseEvents, 'on_click')
    mocker.patch.object(RecordMouseEvents, 'on_scroll')
    mocker.patch.object(RecordMouseEvents, 'record', side_effect=RecordMouseEvents().record)

    record_object = RecordMouseEvents()

    excepted_result = [
        RecordMouseEvents().on_move,
        RecordMouseEvents().on_click,
        RecordMouseEvents().on_scroll,
    ]

    assert record_object.record() == excepted_result
