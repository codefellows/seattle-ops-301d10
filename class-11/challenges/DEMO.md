# Ops Challenge - Psutil

## Demo Code

The demo code below introduces concepts necessary to complete the challenge.

```python
#!/usr/bin/env python3

# Libraries are imported at the top of any Python script using the syntax `import [library
import psutil

# Generate CPU times as a tuple
print(f"CPU Time: {psutil.cpu_times()}\n")

# Show current CPU consumption
print(f"CPU Percent: {psutil.cpu_percent()}")

```
