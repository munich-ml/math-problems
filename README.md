# compute the mean from a list of angles
## the problem
```python
np.array([0, 90]).mean()
```
returns 45 and is what you would expect as mean angle. 

However
```python
np.array([45, 315]).mean()
```
returns 180, while you would expect 0° as the mean angle.

## the solution
- convert to cartesian 
- average x and y
- convert back to angular
