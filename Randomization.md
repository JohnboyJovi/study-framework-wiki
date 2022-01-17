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
* ``Non-combined``: This means that this factor is not used to generate the different conditions, but rather as randomness in the task or repetitions. So it is not combined with the other factors but just randomized in parallel. For example if the task is drawing different animals and other factors like brush size and drawing method should be examined, the type of animal to draw should be ``non-combined`` so that ideally each condition (combination of brush size and drawing technique) is evaluated with another animal for all participants to avoid effects of some animals being easier to draw. ``non-combined factors`` are always randomize using [Balanced Latin Squares](https://cs.uwaterloo.ca/~dmasson/tools/latin_square/), potentially reapeating levels if more than given are needed for the conditions computed from the other factors. However, to have those conditions, at least one factor per phase has to not be ``non-combined``


# Number of Participants
Since randomization is to avoid order effects you should make sure that all orders are seen the same number of times for the best possible statistic validity. That means:
* The number of participants should be a multiple of the number of levels of all between-subjects factors
* The number of participants should be a multiple of the number of conditions (per phase). Excluding ``en block`` factors since they reduce the number of orders shown). So, e.g., with 2 random factors with 2 and 3 levels respectively, the number of participants should be a multiple of 6.
* If you are unsure. Use the ``GenerateTestStudyRuns(20)`` method of SFGameInstance and then check in the generated runs (``StudyFramework(StudyRuns``) after which number of participants the orders repeat.