# Dirty-word-Catcher
Add more dirty word to calculate the counts in your NLP dataset.

---
## Example

kill = bool(re.search(r'\b(K|k)ill\b', f['content'])) #1096

In fact, you don't need to use my regex '\b(K|k)ill\b'. 
You can just turn all the words into lowercase and then type '\bkill\b'.
I'm just too lazy to chage the code.

"#1096" is just my personal record. You can remove it.
