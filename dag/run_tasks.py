from tasks import task_a1, task_a2, task_b
from datetime import datetime

if __name__ == '__main__':
    result_a1 = task_a1.delay()
    result_a2 = task_a2.delay()

    a1_output = result_a1.wait(timeout=None, interval=0.1)
    a2_output = result_a2.wait(timeout=None, interval=0.1)

    print(datetime.now(), a1_output)
    print(datetime.now(), a2_output)

    result_b = task_b.delay()
    b_output = result_b.wait(timeout=None, interval=0.1)
    print(datetime.now(), b_output)
