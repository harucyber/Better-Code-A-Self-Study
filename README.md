# Better-Code-A-Self-Study
A few general optimization and techniques to make my code better.

## Study 1: [Code Speed Optimization](https://github.com/RinSoftwareDeveloper/Better-Code-A-Self-Study/tree/main/self-study/code%20speed%20optimization)
The purpose of this is to see how fast could I generate the fibinachi sequece, trying to improve how fast I could generate it in python using different methods.
| Version | Calculations (35 Terms) | Lines of Code | Computing Time |
| --- | --- | --- | --- |
| Base | 48,315,667 Eval | 23 Lines | 9.8842 Sec |
| Basic Opt. | 48,315,632 Eval | 12 Lines | 4.3868 Sec |
| Iterative Opt. Standard | 13 Eval | 8 Lines | 0 Sec |

Base Version and Basic Optimizations used recursive programming. Thus, it had to recalcuate each value every single time it added a new digit, resulting in insane numbers. 

Here is an example of how recursive programming applied in the first two tests:
```js
0, 1, (0 + 1), ((0+1)+(0+1)), (((0+1) + (0+1))+(0+1)), ((((0+1)+(0+1))+(0+1))+((0+1)+(0+1)))...
```

While this doesn't seem so bad, you can see the calculaton numbers go up very quickly:

```js
0 -> 1 Calculation
1 -> 1 Calculation
0 + 1 -> 2 Calculation
((0+1)+(0+1)) = 5 Calculation
(((0+1) + (0+1))+(0+1)) = 11 Calculation
((((0+1)+(0+1))+(0+1))+((0+1)+(0+1))) = 24 Calculation
```

It is exponential as well. See the graph here:

![image](https://user-images.githubusercontent.com/127797972/231359573-52d25da7-0a4e-43f7-9120-a874e3163614.png)

However, iterative used a different approach.

Instead of recalculating it every single time, it changes each previous recursion to match the number before, assuring that it will not be reoccuring calculations, saving 48,000,000+ calculations.
