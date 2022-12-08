from copy import deepcopy

import numpy as np

from src.containers.containers import AppContainer


def test_predicts_not_fail(app_container: AppContainer, sample_image_np: np.ndarray):
    """Test all functions in weather classifier.

    Args:
        sample_image_np: np.ndarray - image.
        app_container: AppContainer - di container.
    """
    planet_classifier = app_container.planet_classifier()
    planet_classifier.predict(sample_image_np)
    planet_classifier.predict_proba(sample_image_np)


def test_prob_less_or_equal_to_one(app_container: AppContainer, sample_image_np: np.ndarray):
    """Test probs in weather classifier.

    Args:
        sample_image_np: np.ndarray - image.
        app_container: AppContainer - di container.
    """
    planet_classifier = app_container.planet_classifier()
    probs = planet_classifier.predict_proba(sample_image_np)
    for prob in probs:
        assert prob <= 1
        assert prob >= 0


def test_predict_dont_mutate_initial_image(app_container: AppContainer, sample_image_np: np.ndarray):
    """Test mutation of original image.

    Args:
        sample_image_np: np.ndarray - image.
        app_container: AppContainer - di container.
    """
    initial_image = deepcopy(sample_image_np)
    planet_classifier = app_container.planet_classifier()
    planet_classifier.predict(sample_image_np)

    assert np.allclose(initial_image, sample_image_np)
