from store.core.apps import CoreConfig


def test_app_name():
    """Test if the name of app corresponds to the correct on settings"""
    assert CoreConfig.name == 'core'
