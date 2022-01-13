There are two different levels where randomization can be applied

# Study Phase

Here repetitions of all conditions can be specified, so each condition is seen by one participant mutliple times
* ``Number of repetition`` simlpy specifies how often each condition should be seen.
* ``Type of Repetition`` is concerned with the ordering of those repetitions:
  * ``SameOrder``: Repeat all conditions in the same order again NumberOfRepetitions times	 
  * ``DifferentOrder``: Each repetition block is shuffeled, but 2nd repetitions are only done after each condition was seen once, and so on
  * ``FullyRandom``: Repeat all conditions NumberOfRepetitions times, but in an arbitrary order

# Study Factor

* ``Type``: Within vs. Between:
  * ``Within``: participants see all leveles of this factor
  * ``Between``: participants only see one level of this factor each
* ``Mixing Order``:
  * ``RandomOrder``: Using [Balanced Latin Squares](https://cs.uwaterloo.ca/~dmasson/tools/latin_square/) to balance orders between participants, so every participant sees another order of the conditions. If all factors are ``RandomOrder`` orders are repeated after [product of all factor level] many participants, so the number of participants should ideally be a multiple of that (e.g., for a 2x3 design [one factor with 2 levels, and a second with 3 levels] it should be a multiple of 6).
  * ``En Block``: All conditions with the same level of this factor will be shown en block so right after each other.

## Between / Within
* For Between Factors 