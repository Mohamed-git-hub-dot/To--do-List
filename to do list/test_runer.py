import test_cases

if __name__ == "__main__":
    test_cases.setup()
    
    try:
        print("Running Test Case 1: Add a New Task")
        test_cases.test_add_new_task()
        print("Test Case 1 Passed")

        print("Running Test Case 2: Edit an Existing Task")
        test_cases.test_edit_task()
        print("Test Case 2 Passed")

        print("Running Test Case 3: Delete a Task")
        test_cases.test_delete_task()
        print("Test Case 3 Passed")
    except AssertionError as e:
        print(f"Test failed: {e}")
    finally:
        test_cases.teardown()
