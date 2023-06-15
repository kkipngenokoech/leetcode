# PID

PID means a `process identification number`. this is normally assigned automatically to a process.

A process is an executing instance of a process.

this PID is a `non-negative integer`

The process init is the only process that will always have the same PID on any session and on any system, and that PID is 1. This is because init is always the first process on the system and is the ancestor of all other processes.

The default maximum value of PIDs is 32,767. This maximum is important because it is essentially the maximum number of processes that can exist simultaneously on a system

The maximum number of processes on a system is only limited by the amount of physical memory (i.e., RAM) available.

The PIDs for the processes currently on the system can be found by using the ps command or the pstree command (which shows the process names and PIDs in a tree diagram). The top command also shows the PIDs of currently running processes along with other information about them, but it differs in that it continuously updates the information. The pidof command provides the PID of a program whose name is passed to it as an argument (i.e., input).

The PID is needed in order to terminate a frozen or otherwise misbehaving program with the kill command. This command makes it possible to end a program that cannot otherwise be stopped except by rebooting (i.e., restarting) the system, and it is thus an important element in the stability and robustness of Unix-like operating systems.
