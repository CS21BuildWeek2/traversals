#!/usr/bin/env python

from typing import Dict, Any
from time import sleep
from random import choice

from sqlalchemy import create_engine, exists # type: ignore
from sqlalchemy.orm.session import Session, sessionmaker # type: ignore
from sqlalchemy.exc import OperationalError # type: ignore

#from api_funcs import (status, init, move_, take_)
from model import Room, Base
#from settings import REVERSE
from utils import Queue, Stack, bf_paths, df_paths

engine = create_engine('sqlite:///map-1030-wednesday.db')
Session = sessionmaker()

sess = Session(bind=engine)

all = sess.query(Room).all()

if __name__=='__main__':
    # Dict[int, Dict[str, int]]
    graph = dict()
    for room in all:
        graph[room.room_id] = dict()
        if room.n_to:
            graph[room.room_id]['n'] = room.n_to
        if room.s_to:
            graph[room.room_id]['s'] = room.s_to
        if room.w_to:
            graph[room.room_id]['w'] = room.w_to
        if room.e_to:
            graph[room.room_id]['e'] = room.e_to


    print(bf_paths(graph, 216))
