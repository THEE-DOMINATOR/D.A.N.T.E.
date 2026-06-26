# think.py
This file is responsible for **all** of D.A.N.T.E.'s thinking. It provides an abstraction layer for the system, so that the call made is **always** think.getResponse. Simply put, no matter which model you use, the function called will be getResponse. 

You can make your own model schema like so: 
```python
elif THINKING_MODEL_MODE == your model:
    # any initial setup needed goes here
    # this is stuff like API keys and imports
    # if your model supports personalization, call os.getenv('PERSONALITY_PREFERENCES') here.
    def getResponse(prompt):
        # logic to get response using prompt
        yield chunks 
```
> [!WARNING]
> Make sure to have your model stream and yield chunks. Failing to do this can break speaking or delay it.

> [!WARNING]
> Failing to enclose your schema in an elif statement or include try...except protections can cause D.A.N.T.E. to crash and burn. Be careful. 

> [!TIP] 
> You should generally import needed libraries within your if statement. This helps save resources. 

## Contributing
If you have thoroughly tested your schema, feel free to submit it as a PR on GitHub! 