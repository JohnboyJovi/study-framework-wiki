There are two different levels of specifying randomization

# Study Phase

Here repetitions of all conditions can be specified, so each condition is seen by one participant mutliple times
* ``Number of repetition`` simlpy specifies how often each condition should be seen.
* ``Type of Repetition`` is concerned with the ordering of those repetitions:
  * ``SameOrder``: Repeat all conditions in the same order again NumberOfRepetitions times	 
  * ``DifferentOrder``: Each repetition block is shuffeled, but 2nd repetitions are only done after each condition was seen once, and so on
  * ``FullyRandom``: Repeat all conditions NumberOfRepetitions times, but in an arbitrary order

# Study Factor

## Between / Within
* For Between Factors 