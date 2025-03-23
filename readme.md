This is the command line Habit tracker in this project used for tracking the steps ...
uses the pixe.la api to store the data and construct the graph
programe structure as follows

- creates the user to pixe.la
- creates graph for that user by specifying each paramete as mentioned in the documentation
- there is the continue_programe function that gives the feature to intract with code as,

  - writing data to the graph pixels
  - editing that data
  - deleting that data

- then there is the loop that calls the continue function and check the current day data in the pixel and informs the user

You can improve this programe by adding the GUI and integrating the OpenAI api
Pixe.la API documentation:    https://docs.pixe.la/
