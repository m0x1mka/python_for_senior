def remove_marks(text, marks):
    ans = [i for i in text if i not in marks]
    if not remove_marks.__dict__:
        remove_marks.__dict__["count"] = 0
    remove_marks.__dict__["count"] += 1
    return "".join(ans)
