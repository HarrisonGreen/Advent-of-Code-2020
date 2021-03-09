# Advent of Code 2020

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

