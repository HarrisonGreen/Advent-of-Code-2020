# Advent of Code 2020

## Some thoughts about the problems

*	[Day 7](https://adventofcode.com/2020/day/7) (the one with all the bags) was the first one which I found challenging. I counted the shiny gold bag as being inside itself for a while, which didn't help :man_facepalming:. But a really fun problem.
*	[Day 8](https://adventofcode.com/2020/day/8) (the console boot code one) had a really interesting part 2, where we had to flip one of the instructions to fix the code. I'm a little ashamed to admit I just brute forced this one, instead of using a more clever Ariadne's string type approach. That would certainly have been faster, but the input was small enough that I could get away with it.
*	[Day_11](https://adventofcode.com/2020/day/11) (the one with the ferry terminal seats) was the first of a few "Game of Life" style problems this year. Very enjoyable and produces some cool animations (see below).
*	[Day 14](https://adventofcode.com/2020/day/14) (the bitmask one). I found this one particularly fiddly, especially part 2, and I'm not really pleased with the highly suspect way I loop through the memory addresses.
*	[Day 15](https://adventofcode.com/2020/day/15) (the memory recital game one). I wrote my code for part 1, tried it on the much larger input in part 2, and after waiting for a while with no result, decided it needed some optimising. 

## Animations

There were a couple of days in this year's Advent of Code which I thought gave particularly nice animations. The first of them was [day 11](https://adventofcode.com/2020/day/11), where ferry passengers were getting in and out of seats based on the number of people around them. This is my animation of part 1, where a person will leave a seat if they are surrounded by 4 or more people:

![day11_adjacent_4_animation](https://user-images.githubusercontent.com/76997643/110488749-ad1b1a00-80e6-11eb-8fe9-dd5a61ae648d.gif)

But why does it have to be 4? What happens if we choose a higher or lower number? As it turns out, there is good reason why we shouldn't choose a lower number. But it is interesting to see how it behaves if we set the limit to 5, 6, 7, or 8. The first thing to notice is that it converges a lot quicker - only 11 iterations for the case with a limit of 5 compared to 81 in the original case with a limit of 4! And if we go all the way to 8, it only takes 4 steps:

![day11_adjacent_8_animation](https://user-images.githubusercontent.com/76997643/110488680-970d5980-80e6-11eb-9710-5a6995379bd2.gif)

But whichever number we choose, the behaviour is qualitatively similar, since the passengers can only "see" people sat directly next to them. This means that the events in any given area are independent from what is happening elsewhere, and so we do not see any global patterns emerging.

Then we come to part 2, where our passengers can now see an unlimited distance in any direction. However they are more tolerant now, and will only leave their seat if they can see 5 or more people. Again there is a good reason for this - if you're wondering why then try it with 4 and see what happens! And when we look we see that a pattern appears -  a square tilted on its side:

![day11_direction_5_animation](https://user-images.githubusercontent.com/76997643/110519759-9932e080-8105-11eb-9f26-9de31ec43d0c.gif)

It would be reasonable to think that changing the limit from 5 to 6 wouldn't change things that much - maybe it will just converge a bit quicker like last time, right? Wrong. If you predicted that this would happen, then very well done!

![day11_direction_6_animation](https://user-images.githubusercontent.com/76997643/110521195-583bcb80-8107-11eb-8e5b-b5cb2286838d.gif)

Our square has managed to rotate itself and is now the right way up. The case with 7 is very similar to 6 - we get a regular square getting progressively smaller. But when we increase one more to 8, it just tips it over the edge and our square is no longer stable. So while it starts out as a square, it quickly turns into something resembling a map from one of the old Pokémon games. Or a butterfly. Or something else? I'll let you decide...

![day11_direction_8_animation](https://user-images.githubusercontent.com/76997643/110521773-14959180-8108-11eb-8e89-0c92668426f7.gif)

