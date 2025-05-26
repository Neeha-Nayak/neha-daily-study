# 🐢🐇 Fast and Slow Pointers Pattern (Tortoise and Hare)

This folder contains solutions that use the **Fast and Slow Pointer** technique — a common pattern for solving cycle detection, middle-finding, and duplication problems in linked lists, arrays, or number sequences.

---

## 🧠 Key Idea

Use two pointers that move at different speeds:
- `slow` moves one step at a time
- `fast` moves two steps at a time

They either meet at a cycle, help find midpoints, or uncover structural patterns without using extra space.

---

## 📌 Use Cases

- Detecting cycles in sequences or linked lists
- Finding the middle of a linked list
- Identifying duplicates using Floyd’s cycle detection
- Problems requiring O(n) time and O(1) space

---

## 📋 Problem List

| # | Problem | Level | Solution | Notes |
|----|----------------------------------------|--------|----------|-------------------------------|
| 1 | [Happy Number](https://leetcode.com/problems/happy-number/) | Easy | ✔️ | Cycle detection in number sequences |
| 2 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | ⬜ | Detect if a cycle exists |
| 3 | [Find Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) | Medium | ✔️ | Floyd’s cycle method |
| 4 | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | Easy | ✔️ | Find middle using slow pointer |
| 5 | [Circular Array Loop](https://leetcode.com/problems/circular-array-loop/) | Medium | ⬜ | Detect cycle in circular array |

---

## 🧩 Code Template

```python
slow = start
fast = start

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        # cycle detected or pointers met
