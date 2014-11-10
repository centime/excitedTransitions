Siteswap transitions modelization

This repository is a bunch of experiments to get deeper into siteswap. The ultimate goal was to find a algorithm to get entries / exits for excited states, one that would be easy enough that it could be computed in one's head. To do so, I chosed not to use the graph, states modelization, but rather look for an algebrical solution. Well, it works for me, so I'm happy :)

In the graph folder, you can find a naive implementation of the graph approach. It won't deal with much, and no excited stuff, but will grant you some trivial multiplexes.

This script uses the vanilla siteswap notation (
https://en.wikipedia.org/wiki/Siteswap#Vanilla ) which assumes that only
one object is thrown at a time.

It generates transitions between the ground state and excited state
patterns and will bring the simplest sequences to enter and exit the
excited pattern.

Example :
771
66(771)3


If you fail in informing correctly the excited pattern, some corrections
will be proposed.

Example :
7715
Invalid siteswap sequence, you could try one of theses :
666(7175)2
6(7571)4
etc.


Let's juggling!
