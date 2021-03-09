# Advent of Code 2020

## Animations

There were a couple of days in this year's Advent of Code which I thought gave particularly nice animations. The first of them was [day 11](https://adventofcode.com/2020/day/11), where ferry passengers were getting in and out of seats based on the number of people around them. This is my animation of part 1, where a person will leave a seat if they are surrounded by 4 or more people:

![day11_adjacent_4_animation](https://user-images.githubusercontent.com/76997643/110488749-ad1b1a00-80e6-11eb-8fe9-dd5a61ae648d.gif)

But why does it have to be 4? What happens if we choose a higher or lower number? As it turns out, there is good reason why we shouldn't choose a lower number. But it is interesting to see how it behaves if we set the limit to 5, 6, 7, or 8. The first thing to notice is that it converges a lot quicker - only 11 iterations for the case with a limit of 5 compared to 81 in the original case with a limit of 4! And if we go all the way to 8, it only takes 4 steps:

![day11_adjacent_8_animation](https://user-images.githubusercontent.com/76997643/110488680-970d5980-80e6-11eb-9710-5a6995379bd2.gif)

But whichever number we choose, the behaviour is qualitatively similar, since the passengers can only "see" people sat directly next to them. This means that the events in one area are independent from what is happening elsewhere, and so we do not see any global patterns emerging.
