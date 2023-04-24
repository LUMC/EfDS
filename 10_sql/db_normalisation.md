# Database normalisation

*[Database normalisation](https://en.wikipedia.org/wiki/Database_normalization):* a multistep process of database (re)structuring/(re)designing to satisfy certain requirements (called normal forms).

Normalisation advantages/properties:

- Easier to guarantee consistency after data modification.
- Easier to extended the database to accommodate new data.
- Reduction of redundant and duplicate data, better database organisation.
- More tables with smaller rows, more compact database.
- Greater flexibility for queries.
- Easier to implement security.

## First normal form (1NF)

> *the key* exists

![1NF](images/1NF.png)

A table satisfies the first normal form when:

- Columns (attributes) have unique names.
- No duplicate rows (tuples): it must be possible to define the <u>primary key</u>.
- Values are atomic (single values cannot be further decomposed, no collections - otherwise a NoSQL database).

## Second normal form (2NF)

> non-key attributes depend on *the whole key*

![2NF](images/2NF.png)

A 1NF-satisfying table satisfies the second normal form when:

- The primary key is a single column.
- Otherwise: identify all non-prime columns. Each non-prime column must depend on all columns of the primary key (not only a part of it).

## Third normal form (3NF)

>  “[Every] non-key [attribute] must provide a fact about the key, the whole key, and nothing but the key”

![3NF](images/3NF.png)

A 2NF-satisfying table satisfies the third normal form when non-prime columns do not have transitive dependencies.
