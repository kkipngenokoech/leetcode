# ACID

## Atomicity

transactions are atomic, which means if a transaction fails, the result will be like it never happened. all or nothing

## Consistency

you can define rules for your data, and expect that the data abides by the rules, or else the transaction fails.**data should follow a certain pattern**

## Isolation

run two operations at the same time, and you can expect that the result is as though they were ran one after the other. *data should be seperate and atomic*

## Durability

unplug your server at any time, boot it back up, and it didn’t lose any data
