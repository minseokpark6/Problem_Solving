def solution(q, r, code):
    return "".join(c for idx, c in enumerate(code) if idx%q==r)