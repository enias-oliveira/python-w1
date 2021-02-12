#!/usr/bin/env python3
import pytest

from main import enqueue, dequeue


@pytest.fixture
def empty_priority_queue():

    test_priority_queue = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
    }

    return test_priority_queue


@pytest.fixture
def one_patient_priority_queue():
    test_priority_queue = {
        1: [],
        2: [],
        3: [],
        4: ["Joaquim Bastos"],
        5: [],
    }

    return test_priority_queue


@pytest.fixture
def full_patient_priority_queue():
    test_priority_queue = {
        1: ["Ana Pereira"],
        2: ["Victor da Silva"],
        3: ["José Almeida", "Vinicius Cruz"],
        4: ["Joaquim Bastos", "Matheus Garcia"],
        5: ["Viviane dos Reis"],
    }

    return test_priority_queue


def test_enqueue_empty_queue(empty_priority_queue):

    patient = ("José Almeida", 3)

    expected = {
        1: [],
        2: [],
        3: ["José Almeida"],
        4: [],
        5: [],
    }

    actual = enqueue(empty_priority_queue, patient)

    assert actual == expected


def test_enqueue_with_one_patient_in_queue(one_patient_priority_queue):

    patient = ("José Almeida", 3)

    expected = {
        1: [],
        2: [],
        3: ["José Almeida"],
        4: ["Joaquim Bastos"],
        5: [],
    }

    actual = enqueue(one_patient_priority_queue, patient)

    assert actual == expected


def test_dequeue_full_queue(full_patient_priority_queue):

    expected = (
        {
            1: ["Ana Pereira"],
            2: ["Victor da Silva"],
            3: ["José Almeida", "Vinicius Cruz"],
            4: ["Joaquim Bastos", "Matheus Garcia"],
            5: [],
        },
        "Viviane dos Reis",
    )

    actual = dequeue(full_patient_priority_queue)

    assert actual == expected


def test_dequeue_one_pacient(one_patient_priority_queue, empty_priority_queue):

    print(empty_priority_queue)

    expected = (
        empty_priority_queue,
        "Joaquim Bastos",
    )

    actual = dequeue(one_patient_priority_queue)

    assert actual == expected
