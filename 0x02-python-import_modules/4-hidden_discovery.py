#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    sem = dir(hidden_4)
    for sem in sems:
        if sem[:2] != "__":
            print(sem)
