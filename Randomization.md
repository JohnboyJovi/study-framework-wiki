There are three different levels where randomization can be applied (see below)

All randomization is seeded with the participant id, so with the same participant id you will always see the same order. Also the study phase index is used, so two exactly identical study phases (following eachother) will have different orders for the same participant.

*Some examples can be found here: [Randomization/Examples](Randomization/Examples)


# Study Factor

* ``Type``: Within vs. Between:
  * ``Within``: participants see all leveles of this factor
  * ``Between``: participants only see one level of this factor each
* ``Mixing Order``:
  * ``RandomOrder``: Using [Balanced Latin Squares](https://cs.uwaterloo.ca/~dmasson/tools/latin_square/) to balance orders between participants, so every participant sees another order of the conditions. If all factors are ``RandomOrder`` orders are repeated after [product of all factor level] many participants, so the number of participants should ideally be a multiple of that (e.g., for a 2x3 design [one factor with 2 levels, and a second with 3 levels] it should be a multiple of 6).
  * ``En Block``: All conditions with the same level of this factor will be shown en block so right after each other (**at most one factor can be ``En Block``**).
  * ``In Order``: The order of the factors' levels will not be randomized (Latingquare) between subjects. So all subjects see this factor's levels in the order specified for the factor. 
  * :warning: Careful when using ``En Block`` and ``In Order`` together: ``En Block`` is considered first and then the ``In Order`` factors are kept in there given order. Note that order of defining the factors matters, e.g., when using multiple ``In Order`` factors (see [Randomization/Examples](Randomization/Examples#using-inorder-potentially-for-multiple-factors) for clarification).
* ``Non-combined``: This means that this factor is not used to generate the different conditions, but rather as randomness in the task or repetitions. So it is not combined with the other factors but just randomized in parallel. For example if the task is drawing different animals and other factors like brush size and drawing method should be examined, the type of animal to draw should be ``non-combined`` so that ideally each condition (combination of brush size and drawing technique) is evaluated with another animal for all participants to avoid effects of some animals being easier to draw. ``non-combined factors`` are always randomize using [Balanced Latin Squares](https://cs.uwaterloo.ca/~dmasson/tools/latin_square/), potentially reapeating levels if more than given are needed for the conditions computed from the other factors. However, to have those conditions, at least one factor per phase has to not be ``non-combined``. For non-combined factors, there number should be different from the number of conditions (and they should not be multiples of each other), so the best possible shuffling of conditions to non-combined levels is achieved.
* **Repetitions**: if conditions should be repeated multiple times, it is easiest to add an additional Factor, e.g. ``Repetition`` with Levels ``{1,2,3}`` for three repetitions, and then use ``Random`` (repetitions are done fully random), ``EnBlock`` (the second repetitions are only begun once all conditions were seen once, and so on), or ``InOrder`` (e.g., in combination with another ``EnBlock`` Factor of which all repetitions are shown right after eachother). Examples for this can be found in [Randomization/Examples](Randomization/Examples#repeating-all-conditions-multiple-times). In case more involved repetition patterns are required, the ``ConditionSortingCallback()`` function should be used (see below).

# Study Setup

* ``PhasesToOrderRandomize`` can be used to specify phase names of phases which should be randomized in order between participants. So if a study has the phases ``Warmup``, ``Phase1``, ``Break``, ``Phase2`` and ``PhasesToOrderRandomize = { Phase1, Phase2}`` is given. Then participants will alternately see orders ``Warmup``, ``Phase1``, ``Break``, ``Phase2`` and ``Warmup``, ``Phase2``, ``Break``, ``Phase1``.
* ``ConditionSortingCallback()``: this is a function in the ``ASFStudySetup`` class, that in its default implementation does nothing. It can be overridden in C++ (currently blueprints are not supported for this, since that complicated matters a lot). The function receives an ``TArray<USFCondition*>`` and should return a reordered version of this. You can simply change the order of all of these conditions. However, removing or adding entries can have *undefined behavior*!


# Number of Participants
Since randomization is to avoid order effects you should make sure that all orders are seen the same number of times for the best possible statistic validity. That means:
* The number of participants should be a multiple of the number of levels of all between-subjects factors
* The number of participants should be a multiple of the number of conditions (per phase). Excluding ``en block`` factors since they reduce the number of orders shown). So, e.g., with 2 random factors with 2 and 3 levels respectively, the number of participants should be a multiple of 6.
* If you are unsure. Use the ``Generate Test Study Runs`` button of the Study Setup (in the ``Study Setup Debug`` section) and then check in the generated runs (``StudyFramework/StudyRuns``) after which number of participants the orders repeat.