 -----Python Data Model----
[Python official doc.](https://docs.python.org/3/reference/datamodel.html) 
3.1 Objects, values and types
* Objects are Python's abstraction for data.
* All data in a Python program:
  - objects
  - relations between objects
(Von Neumann's model)

* An object has
  - Identity
    - Never change once it has been created (Object address in memory)
  - Type
    - Affects almost all aspects of object behavior

  - Value
    - Mutable
      -> Value is changable (id should be not change)
      ex: lists, dictionaries
    - Immutable
      -> For the same id, value cannot be change.
      (If value is changing, the id also change. Namely, a new object.)
      ex: numbers, strings, tuples
    *************************
    The property of value's im/mutable is important.
    Hint: id is changable or not....
    *************************

* Garbage collected
  - When objects become unreachable, they may be garbage-collected.
    - Implementation
      * Postpone
      * Omit

* Container: Object contain references to other object
  ex:
    - tuples, lists and directionaries

3.2 The standard type hierarchy

 * Type
    - None:
      - This type has a single value.
      - This is the single object with this value
      - It's truth value is false

    - NotImplemented: TBD.....

    - numbers.Number: Distinguish between integers, floating point number, complex number
      - Integral
        - Integers(int)
        - Booleans(bool) (Boolean is the type of Intergal)
        - Real(float)
          - Python only support the double precision floating point number
        (Not support single-precision floating point number)
        - Complex
          - ex: 1-3j: 1 => real, 3j => imag

    - Sequences: Finite ordered sets indexed by non-negative numbers
      - Supporting slice: a[i:j]
        (Some sequences also support "extended slicing" a[i:j:k] which selects
        items of a index x where x = i+n*k, n>=0, i <=x<j)
      - Mutability:
          - immutable sequence
            - Strings, Number, Tuples, Bytes
          - mutable sequence
            - Lists, Byte Arrays,
