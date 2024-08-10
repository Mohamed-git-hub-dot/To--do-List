from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver (make sure to specify the path to your WebDriver)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

def setup():
    driver.get('file:///path/to/to_do_list.html')  # Replace with the path to your HTML file

def teardown():
    driver.quit()

# Test Case 1: Add a New Task
def test_add_new_task():
    task_input = driver.find_element(By.ID, 'new-task')
    task_input.send_keys('Buy groceries')
    task_input.send_keys(Keys.RETURN)

    task_list = driver.find_element(By.ID, 'task-list')
    tasks = task_list.find_elements(By.TAG_NAME, 'li')
    assert any('Buy groceries' in task.text for task in tasks), "Task not added"

# Test Case 2: Edit an Existing Task
def test_edit_task():
    tasks = driver.find_elements(By.CLASS_NAME, 'task-item')
    for task in tasks:
        if 'Buy groceries' in task.text:
            edit_button = task.find_element(By.CLASS_NAME, 'edit-btn')
            edit_button.click()
            edit_input = task.find_element(By.CLASS_NAME, 'edit-input')
            edit_input.clear()
            edit_input.send_keys('Buy milk')
            edit_input.send_keys(Keys.RETURN)
            break
    
    updated_task = driver.find_element(By.XPATH, "//li[contains(text(), 'Buy milk')]")
    assert updated_task is not None, "Task not edited"

# Test Case 3: Delete a Task
def test_delete_task():
    tasks = driver.find_elements(By.CLASS_NAME, 'task-item')
    for task in tasks:
        if 'Buy milk' in task.text:
            delete_button = task.find_element(By.CLASS_NAME, 'delete-btn')
            delete_button.click()
            break

    task_list = driver.find_element(By.ID, 'task-list')
    tasks = task_list.find_elements(By.TAG_NAME, 'li')
    assert not any('Buy milk' in task.text for task in tasks), "Task not deleted"
