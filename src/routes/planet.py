import cv2
import numpy as np
from dependency_injector.wiring import Provide, inject
from fastapi import Depends, File

from src.containers.containers import AppContainer
from src.routes.routers import router
from src.services.planet_classifier import PlanetClassifier


@router.get('/all_conditions')
@inject
def planet_conditions(service: PlanetClassifier = Depends(Provide[AppContainer.planet_classifier])):
    return {
        'conditions': service.classes,
    }


@router.post('/predict')
@inject
def predict(
    image: bytes = File(),
    service: PlanetClassifier = Depends(Provide[AppContainer.planet_classifier]),
):
    img = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_COLOR)
    conditions = service.predict(img)

    return {'conditions': conditions}


@router.post('/predict_proba')
@inject
def predict_proba(
    image: bytes = File(),
    service: PlanetClassifier = Depends(Provide[AppContainer.planet_classifier]),
):
    img = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_COLOR)
    return {'conditions': service.predict_proba(img)}
