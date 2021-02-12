#!/usr/bin/env python3

priority_queue = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
}


def enqueue(priority_queue, patient):

    patient_name, patient_priority = patient

    priority_queue[patient_priority].append(patient_name)

    return priority_queue


def dequeue(priority_queue):

    for pacients in reversed(priority_queue.values()):

        if len(pacients) > 0:
            pacient = pacients.pop(0)
            break

    return (priority_queue, pacient)
