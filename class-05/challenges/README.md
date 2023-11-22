# Ops Challenge: Clearing Logs

## Overview

Clearing logs using Bash typically involves using command-line tools to delete or truncate log files. Log files are commonly used to store system, application, or other program-generated information for diagnostic and monitoring purposes. Clearing logs might be necessary to free up disk space, maintain privacy, or simply manage the log file size.

Here are a few common methods to clear logs using Bash:

1. **Deleting Log Files:**
  If you want to completely remove log files, you can use the `rm` command. For example, to delete a single log file named "app.log", you can use:

  ```bash
  rm /path/to/app.log
  ```

  To delete multiple log files using wildcards (`*`), you can use:

  ```bash
  rm /path/to/*.log
  ```

  Be cautious when using `rm` as it **permanently** deletes files.

2. **Truncating Log Files:**
  Truncating a log file means removing its content while retaining the file itself. This is useful if you want to clear the log's content without deleting the file. You can use the `>`, `echo`, or `truncate` commands.

  Using `>`:

  ```bash
  > /path/to/app.log
  ```

  Using `echo`:

  ```bash
  echo -n "" > /path/to/app.log
  ```

  Using `truncate`:

  ```bash
  truncate -s 0 /path/to/app.log
  ```

## Resources

- [How to empty (truncate) Log files in Linux](https://computingforgeeks.com/how-to-empty-truncate-log-files-in-linux/)

## Demonstration

Refer to [DEMO.md](DEMO.md)
