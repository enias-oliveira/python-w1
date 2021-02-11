#!/usr/bin/env python3
import pytest

from main import enqueue, dequeue, priority_queue


@pytest.fixture
def empty_priority_queue():
    return priority_queue


@pytest.fixture
def one_patient_priority_queue():
    test_priority_queue = {
        "Não urgência": [],
        "Pouca Urgência": [],
        "Urgência": [],
        "Muito Urgente": ["Joaquim Bastos"],
        "Emergência": [],
    }

    return test_priority_queue


@pytest.fixture
def full_patient_priority_queue():
    test_priority_queue = {
        "Não urgência": ["Ana Pereira"],
        "Pouca Urgência": ["Victor da Silva"],
        "Urgência": ["José Almeida", "Vinicius Cruz"],
        "Muito Urgente": ["Joaquim Bastos", "Matheus Garcia"],
        "Emergência": ["Viviane dos Reis"],
    }

    return test_priority_queue


def test_enqueue_empty_queue(empty_priority_queue):

    patient = ("José Almeida", 3)

    expected = {
        "Não urgência": [],
        "Pouca Urgência": [],
        "Urgência": ["José Almeida"],
        "Muito Urgente": [],
        "Emergência": [],
    }

    actual = enqueue(empty_priority_queue, patient)

    assert actual == expected


def test_enqueue_with_one_patient_in_queue(one_patient_priority_queue):

    patient = ("José Almeida", 3)

    expected = {
        "Não urgência": [],
        "Pouca Urgência": [],
        "Urgência": ["José Almeida"],
        "Muito Urgente": ["Joaquim Bastos"],
        "Emergência": [],
    }

    actual = enqueue(one_patient_priority_queue, patient)

    assert actual == expected


def test_dequeue_full_queue(full_patient_priority_queue):

    expected = (
        {
            "Não urgência": ["Ana Pereira"],
            "Pouca Urgência": ["Victor da Silva"],
            "Urgência": ["José Almeida", "Vinicius Cruz"],
            "Muito Urgente": ["Joaquim Bastos", "Matheus Garcia"],
            "Emergência": [],
        },
        "Viviane dos Reis",
    )

    actual = dequeue(full_patient_priority_queue)

    assert actual == expected
