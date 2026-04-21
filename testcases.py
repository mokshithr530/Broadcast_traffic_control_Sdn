import os
import time

def run_cmd(cmd):
    print(f"\n>>> {cmd}")
    os.system(cmd)


def test_uncontrolled():
    print("\n===== TEST CASE 1: UNCONTROLLED BROADCAST =====")

    print("-> Make sure broadcast control is DISABLED in controller")
    time.sleep(2)

    run_cmd("h1 ping -c 3 h4")


def test_controlled():
    print("\n===== TEST CASE 2: CONTROLLED BROADCAST =====")

    print("-> Make sure broadcast control is ENABLED")
    time.sleep(2)

    run_cmd("h1 ping -c 3 h4")


def test_performance():
    print("\n===== TEST CASE 3: PERFORMANCE TEST (IPERF) =====")

    print("-> Starting iperf server on h4")
    run_cmd("h4 iperf -s &")
    time.sleep(2)

    print("->  Running iperf client on h1")
    run_cmd("h1 iperf -c h4")


def run_all_tests():
    print("\n--> RUNNING ALL TEST CASES <--")

    test_uncontrolled()
    time.sleep(3)

    test_controlled()
    time.sleep(3)

    test_performance()

    print("\n--- ALL TESTS COMPLETED ---")


if __name__ == "__main__":
    run_all_tests()