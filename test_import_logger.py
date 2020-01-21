import logging
import import_logger

def test_import_logger(caplog):
    caplog.set_level(logging.DEBUG)
    import_logger.register(0)
    import pathlib
    assert caplog.records