# Database related terms

## Transaction

A *database transaction* is a unit of work which the DBMS guarantees to reliably perform independent of other transactions:
- *reliability:* The changes of the transaction are either fully performed or not at all. Unexpected events (e.g. power failure) are guaranteed not to leave the database in a partially changed state.
- *independence:* The actions of the transaction are isolated from other actions which might be concurrently (at the same time) performed by other programs.

A database transaction must be ACID.

When writing code, a transaction is *bracketed*, i.e. the code has a form: 
- `BEGIN` (to denote `START TRANSACTION`)
- `...` (the code of the action, typically multiple statements)
- `COMMIT` (to denote the end of the transaction and force its guaranteed storage in the database)

In case of an error within the `...` code the `ROLLBACK` operation returns the database to the state before `begin`.

## ACID

Transaction properties:
- *Atomic:* A transaction must be completed or have no effect.
- *Consistent:* A transaction must lead to a state in which all database constraints are met.
- *Isolated:* A transaction must not affect other transaction.
- *Durable:* A transaction changes must get written to persistent storage.

## Other terms

- *In-memory database:* fast, data is kept permanently in computer memory; no need to access a disk to respond to queries.
- *Cloud database:* the data and the database system exists “somewhere” online and is fully web controlled.
- *Distributed database:* the data and DBMS utilise multiple computers.
