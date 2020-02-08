# math-problems
collection of general math problems

## compute the mean from a list of angles
The problem:
```python
np.array([0, 90]).mean()
```
returns 45 and is what you would expect as mean angle. 

However
```python
np.array([45, 315]).mean()
```
returns 180, while you would expect 0° as the mean angle.

The solution: 
- convert to cartesian 
- average x and y
- convert back to angular

[link to an example implementation](compute_mean_of_angles.py)
