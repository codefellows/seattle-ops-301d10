# Ops Challenge - Python Malware Analysis

## Demo Code

Analyzing malware code can be a potentially risky task, as it involves handling potentially harmful code that can infect systems. However, if you follow proper precautions and use a safe environment, you can minimize the risks.

The demo code below introduces concepts necessary to complete the challenge.


```python
#!/usr/bin/env python3

def changeme( mylist ):
   mylist.append([1,2,3,4]);
   print("Values inside the function: ", mylist)
   return

mylist = [10,20,30];
changeme( mylist );
print("Values outside the function: ", mylist)

```

Break the code into pieces. Identify each component. Use what you know. For example, you know functions must be declared before they can be called.

```python
#!/usr/bin/env python3

# Function definition is here

def changeme( mylist ):
# This changes a passed list into this function

   mylist.append([1,2,3,4]);
   print("Values inside the function: ", mylist)
   return

# The function changeme has been declared. Now you can call changeme function.

# First, the script declares a variable called "mylist" as [10,20,30]
mylist = [10,20,30];

# The function changeme is called with the parameter "mylist" inserted.
changeme( mylist );

# Prints a string then the contents of "mylist" variable
print("Values outside the function: ", mylist)
```

By translating the code line by line and using the concepts we know, we can gradually interpret the meaning of code written by another person.


## Notes

Here are some recommended steps to analyze malware code safely:

1. Isolate the Environment
    - Create a controlled and isolated environment to analyze the malware. Use a dedicated VM or an offline system that is not connected to your network or critical infrastructure. This prevents the malware from spreading or causing damage beyond the isolated environment.
2. Analyze Indicators of Compromise (IOCs)
    - Identify any potential indicators of compromise, such as file names, registry entries, or network connections associated with the malware. Analyze these IOCs to understand the impact and potential mitigation strategies.
3. Use a Debugger
    - A debugger is a useful tool that allows you to pause the execution of the code in order to inspect it's behavior. However, exercise caution when using these tools, as some malware may be designed to detect and evade analysis.
4. Analyze in a Controlled Network
    - If network behavior analysis is required, connect the virtual machine to an isolated network environment, such as a separate subnet or virtual network. Monitor the network traffic and interactions of the malware within this controlled environment.
