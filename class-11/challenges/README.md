# Ops Challenge: Psutil

## Overview

Python is known for its versatile and diverse selection of libraries. Libraries are installable toolkits that add new functions to the language on your system. Today you will use Psutil to fetch system information.

`psutil` stands for "process and system utilities". It is a Python library used for system monitoring, resource management, and process control. It allows you to retrieve detailed information about running processes, including their CPU and memory usage, process IDs (PIDs), parent-child relationships, process creation time, and termination of processes. It also enables you to monitor system resources in real-time by providing functions to track network activity, disk I/O, and process-related metrics.

## Resources

- [Python libraries and their features](https://www.codingninjas.com/blog/2020/07/24/python-libraries-and-their-features/)
  - This article defines the terms module, package, and library in the context of understanding what libraries are.
- [Psutil module in Python](https://www.geeksforgeeks.org/psutil-module-in-python/)
- [Five Python libraries for cyber security](https://medium.com/ediblesec/5-python-libraries-for-cyber-security-8f34f5f1e3b8)
  - If you're wondering what libraries you should be practicing to prepare yourself for a cyber role, have a look at Chris Doucette's top five in this article. The libraries mentioned in this article (requests and nmap in particular) should be used ethically and with a firm comprehension of what the tools do and any legal liabilities that may arise from improper use.

## Demonstration

Refer to [DEMO.md](DEMO.md)

## Notes

1. What is the difference between a library and a module in Python?
1. How is `psutil` utilized in networking and cybersecurity?
1. Fill in the details of some methods you might be working with in this challenge.
    - `psutil.cpu_times()`
      - description: It provides information about how the CPU time is distributed across different activities.
      - input: This method does not require any input parameters.
      - output: The output is a tuple containing the CPU times for various categories, such as user mode, system mode, idle time, interrupt time, and more.
    - `psutil.cpu_percent()`
      - description: This method calculates the CPU usage percentage for the whole system or a specific CPU. It measures the percentage of time that the CPU is being utilized by processes.
      - input: It accepts an optional parameter interval which specifies the duration (in seconds) over which the CPU usage is averaged. By default, it uses a 1-second interval.
      - output: The output is a float value representing the CPU usage percentage. It indicates how much of the CPU's processing capacity is currently being used by running processes during the specified interval.
    - `psutil.cpu_times().user`
      - description:
      - input:
      - output:
    - `psutil.cpu_times().system`
      - description:
      - input:
      - output:
    - `psutil.cpu_times().idle`
      - description:
      - input:
      - output:
    - `psutil.cpu_times().nice`
      - description:
      - input:
      - output:
    - `psutil.cpu_times().iowait`
      - description:
      - input:
      - output:
    - `psutil.cpu_times().irq`
      - description:
      - input:
      - output:
    - `psutil.cpu_times().softirq`
      - description:
      - input:
      - output:
    - `psutil.cpu_times().steal`
      - description:
      - input:
      - output:
    - `psutil.cpu_times().guest`
      - description:
      - input:
      - output:
1. Python Methods:
  - `repr()`
    - description:
    - input:
    - output:
  - `str()`
    - description:
    - input:
    - output:
1. What is a float in Python?
