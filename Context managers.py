class MyContextManager:
 def __enter__(self):
 # Perform resource initialization
  print("Initializing resources")
 # You can optionally return an object that will be assigned to the variable after 'as'
  return self
 def __exit__(self, exc_type, exc_value, traceback):
 # Perform resource cleanup
  print("Cleaning up resources")
 # Handle any exceptions, if needed
 if exc_type:
     print(f"An exception of type {exc_type} occurred: {exc_value}")
 # Return False to propagate the exception, or True to suppress it
 return False
# Using the custom context manager
with MyContextManager() as cm:
 # Perform operations using the resources managed by the context manager
 print("Doing something inside the context manager")
 # You can access the context manager object using the variable assigned after 'as'
 print(f"Context manager object: {cm}")
# Once the block inside the 'with' statement is finished,
# the context manager's __exit__ method is called to clean up the resources.
