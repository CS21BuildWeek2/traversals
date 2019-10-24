#!/usr/bin/env python
from typing import Optional, List, Dict, TypeVar
A = TypeVar('A')

class Queue:
    def __init__(self):
        self.queue: List[A] = list()

    def enqueue(self, a: A):
        self.queue.append(a)

    def dequeue(self) -> Optional[A]:
        if self.size > 0:
            rtrn: A = self.queue.pop(0)
            return rtrn
        else:
            return None

    @property
    def size(self):
        return len(self.queue)

class Stack:
    def __init__(self):
        self.stack: List[A] = list()

    def push(self, a: A):
        self.stack.append(a)

    def pop(self) -> A:
        if self.size > 0:
            return self.stack.pop()
        else:
            return None

    @property
    def size(self):
        return len(self.stack)


def bf_paths(graph: Dict[int, Dict[str, int]], starting_room: int) -> Dict[int, List[str]]:
    qq = Queue()
    visited = set()
    qq.enqueue([starting_room])

    paths = {(starting_room,starting_room): [starting_room]}

    while qq.size > 0:
        path: List[int] = qq.dequeue()
        room = path[-1]

        if room not in visited:

            visited.add(room)
            for move, nextroom in graph[room].items():
                path_copy = path.copy()
                path_copy.append(nextroom)
                qq.enqueue(path_copy)

                paths[(starting_room, nextroom)] = paths[(starting_room, room)] + [move]

    paths = {key: val[1:] for key, val in paths.items()}
    return paths

def df_paths(graph: Dict[int, Dict[str, int]], starting_room: int) -> Dict[int, List[str]]:
    ss = Stack()
    visited = set()
    ss.push([starting_room])

    paths = {(starting_room,starting_room): [starting_room]}

    while ss.size > 0:
        path: List[int] = ss.pop()
        room = path[-1]
        if room not in visited:
            visited.add(room)
            for move, nextroom in graph[room].items():
                path_copy = path.copy()
                path_copy.append(nextroom)
                ss.push(path_copy)

                paths[(starting_room, nextroom)] = paths[(starting_room, room)] + [move]

    paths = {key: val[1:] for key, val in paths.items()}
    return paths
