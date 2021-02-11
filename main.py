#!/usr/bin/env python3

priority_queue = {
    "Não urgência": [],
    "Pouca Urgência": [],
    "Urgência": [],
    "Muito Urgente": [],
    "Emergência": [],
}


def enqueue(priority_queue, patient):

    priority_index = [
        None,
        "Não urgência",
        "Pouca Urgência",
        "Urgência",
        "Muito Urgente",
        "Emergência",
    ]

    patient_name, patient_priority = patient

    priority_index = priority_index[patient_priority]

    priority_queue[priority_index].append(patient_name)

    return priority_queue


def dequeue(priority_queue):

    priority_index = [
        None,
        "Não urgência",
        "Pouca Urgência",
        "Urgência",
        "Muito Urgente",
        "Emergência",
    ]

    return (priority_queue, "Teste")
