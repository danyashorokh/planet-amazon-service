from dependency_injector import containers, providers

from src.services.planet_classifier import PlanetClassifier


class AppContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    planet_classifier = providers.Factory(
        PlanetClassifier,
        config=config.services.planet_classifier,
    )
