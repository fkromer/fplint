# fplint

Checklist about Python Functional Programming best practices/idioms for a potential linter (plugin).

# Rules

## Classes

* C01: assert no usage of classes with attributes and properties -> reason: attributes and properties introduce state -> exceptions: classes to implement configuration or caching (classes w.o. attributes for namespacing of related functions OK) (Lott 2018, p. 26)
* C02: assert no class inheritage used -> reason: classes interited from could introduce state via attributes, properties and/or non-pure functions

## Functions

* F01: assert no global statement used -> reason: global data dependency introduces state (Lott 2018, p.24)
* F02: assert no non-local statement used in non-nested function definitions -> reason: non local data dependency introduces state (Lott 2018, p. 24)

## Data types

* D01: assert no usage of mutable built-in data types -> reason: data with mutable data type introduces state (Lott 2018, p. 26)

# References

Lott, S. (2018). *Functional Python Programming*. 2nd ed. Birmingham: Packt Publishing.
