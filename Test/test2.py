import random
from multiprocessing import Process, freeze_support
from qpkg.StockDB import StockDB
from qpkg.config import configUpdate
import time
 
def multi(data, idx):
    db = StockDB(user=configUpdate.USER,
                 pwd=configUpdate.PWD,
                 db=configUpdate.DB)
    for i in data:
        db.cur.execute('INSERT INTO test(b, c) VALUES ({0}, {1})'.format(i, idx))
    db.commit()
    db.close()
 
if __name__=='__main__':
    freeze_support() # for multiprocessing other process on windows
    data = [[random.randint(0,100) for i in range(5000)] for j in range(5)]
    procs = []
    start_time = time.time()
 
    for idx, n in enumerate(data):
        proc = Process(target=multi, args=(n,idx))
        procs.append(proc)
        proc.start()
 
    for proc in procs:
        proc.join()
 
    end_time = time.time()
    print('time : {0}'.format(end_time - start_time))