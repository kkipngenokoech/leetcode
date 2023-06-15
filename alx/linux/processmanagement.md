# PROCESS MANAGEMENT

in linux there can be two types of processes:

1. Foreground processes
2. Background processes

## FOREGROUND PROCESSES

it depends on the user for input - interactive processes

## BACKGROUND PROCESSES

run independently of the user

these are automatic process

## process states in linux

A process in Linux can go through different states after it’s created and before it’s terminated.

they include:

1. Running - A process in running state means that it is running or it’s ready to run
2. Sleeping - The process is in a sleeping state when it is waiting for a resource to be available.
   1. A process in Interruptible sleep will wakeup to handle signals, whereas a process in Uninterruptible sleep will not.
3. Stopped - A process enters a stopped state when it receives a stop signal.
4. Zombie - Zombie state is when a process is dead but the entry for the process is still present in the table.

## commands for managing linux processes

### Top

this command is used to track processes running on the system

### ps

is it a short form for Process Status, it displays information of currently running processes, unlike top, it does not display real time information.

## kill

it is used to stop a process in linux process, kill command sends a signal to the process

you normally send a `kill [pid]` that is the process ID of the process you want to kill

## change a priority of a process

n Linux, you can prioritize between processes. The priority value for a process is called the ‘Niceness’ value. Niceness value can range from -20 to 19. 0 is the default value.

The fourth column in the output of top command is the column for niceness value.

when starting a process and you want to give priority to it: `$ nice -n [value] [process name]` and if the process is already running you can give priority to it: `renice [value] -p 'PID'`
