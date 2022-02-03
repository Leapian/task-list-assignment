'''
Below is a task todo app. This app has the responsibilities:
    1) Fetch a list of tasks from an API (Will be provided)
    2) Create TodoTasks based on the data returned from the server and insert into a list
    3) Based on the user input there are a couple of operations that need to happen -> Fill the methods. 
    (Feel free to add any other methods, variables that you deem are needed for the completion of this exercise)
    
Useful Information:
    1) The datetimes are provided in miliseconds from the server
    2) The id is provided from the server for each task

The tasks should be displayed in the format below:
[ ] Task description / Due 12th Jan 2021 - For todo tasks
[x] Task description / Due 12th Jan 2021 - For done tasks
[o] Task description / Due 12th Jan 2021 - For overdue tasks

There is a bonus task:
    - Results should be displayed ascending / descending based on a flag that the user can change and stays that way until the user changes it again
'''

class TodoTask:
    def __init__(self, id, taskDescripton, dueDate, isComplete):
        self.id = id
        self.taskDescripton = taskDescripton
        self.dueDate = dueDate 
        self.isComplete = isComplete

    def markTaskAsComplete():
        pass
    
    def markTaskAsNotComplete():
        pass

class TodoList:
    def __init__(self):
        self.TaskList = []
    
    def addTask(task):
        pass
    
    def displayAllTasks():
        pass
    
    def diplayCompleteTasks():
        pass
    
    def diplayIncompleteTasks():
        pass
    
    def changeTaskStatus(id):
        pass

def fetchTasksFromServer(api):
    pass

def main():
    userInput = "";
    apiEndpoint = "";
    while(userInput != "-1"):
        print("Press 0 to display all tasks")
        print("Press 1 to display Complete tasks")
        print("Press 2 to display Incomplete tasks")
        print("Press a to add a task")
        print("Press e to mark a task as completed or not")
        print("Press -1 to exit")
        userInput = input('Please enter a value: ')
        if(userInput == "0"):
            pass
        if(userInput == "1"):
            pass
        if(userInput == "2"):
            pass
        if(userInput == "a"):
            pass
        if(userInput == "e"):
            pass
        

if __name__ == "__main__":
    main()