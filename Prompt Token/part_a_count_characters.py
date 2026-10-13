from prompt_tokens import PromptTokens

source = PromptTokens(["I", "reside", "in", "Delhi", "."])
total = 0

# ---- WRITE ONLY THIS WHILE LOOP ----
while source.has_next():
    total+=len(source.next_token())
# ------------------------------------

print(total)