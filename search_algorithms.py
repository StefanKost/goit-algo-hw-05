def boyer_moore_search(text: str, pattern: str) -> int:
    m, n = len(pattern), len(text)
    if m > n:
        return -1

    # Build skip table
    skip = {pattern[i]: m - i - 1 for i in range(m - 1)}

    i = m - 1
    while i < n:
        j = m - 1
        k = i
        while j >= 0 and text[k] == pattern[j]:
            j -= 1
            k -= 1
        if j < 0:
            return k + 1  # match position
        i += skip.get(text[i], m)

    return -1


# Knuth Morris Pratt
def kmp_search(text: str, pattern: str) -> int:
    m, n = len(pattern), len(text)
    if m > n:
        return -1

    def compute_lps() -> list[int]:
        res = [0] * m
        length = 0
        k = 1

        while k < m:
            if pattern[k] == pattern[length]:
                length += 1
                res[k] = length
                k += 1
            elif length != 0:
                length = res[length - 1]
            else:
                res[k] = 0
                k += 1

        return res

    lps = compute_lps()
    i = j = 0

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            return i - j  # match found

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1


def rabin_karp_search(text: str, pattern: str, base: int = 256, mod: int = 101) -> int:
    m, n = len(pattern), len(text)
    if m > n:
        return -1

    h = pow(base, m - 1, mod)
    p_hash = t_hash = 0

    # Compute initial hashes for pattern and first window of text
    for i in range(m):
        p_hash = (base * p_hash + ord(pattern[i])) % mod
        t_hash = (base * t_hash + ord(text[i])) % mod

    # Slide the pattern over text
    for i in range(n - m + 1):
        if p_hash == t_hash and text[i:i + m] == pattern:
            return i  # match found
        if i < n - m:
            t_hash = (base * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % mod
            if t_hash < 0:
                t_hash += mod

    return -1