from multiprocessing import Process, Manager

def worker(shared_list, shared_dict):
    shared_list.append(10)
    shared_dict["x"] = 42

if __name__ == "__main__":
    with Manager() as manager:
        shared_list = manager.list()
        shared_dict = manager.dict()

        p1 = Process(target=worker, args=(shared_list, shared_dict))
        p2 = Process(target=worker, args=(shared_list, shared_dict))

        p1.start(); p2.start()
        p1.join(); p2.join()

        print(shared_list)  # [10, 10]
        print(shared_dict)  # {'x': 42}