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

    for i in range(5, 0, -1):

        pacients = priority_queue[i]

        if len(pacients) > 0:
            pacient = pacients.pop(0)
            break

    return (priority_queue, pacient)
