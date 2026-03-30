# ActionSpace Design Notes

## Motivation

In Mesa, agent constraints such as energy limits, movement rules, or state restrictions are typically implemented inside the `step()` method.

Example:

```python
self.energy -= 1
if self.energy < 0:
    self.remove()
