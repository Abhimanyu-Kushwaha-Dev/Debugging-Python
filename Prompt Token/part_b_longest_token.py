from prompt_tokens import PromptTokens

source = PromptTokens(["I", "reside", "in", "Delhi", "."])
longest = ""
length=0
# ---- WRITE ONLY THIS WHILE LOOP ----

while source.has_next():
    s=source.next_token()
    if len(s)>length:
        length=len(s)
        longest=s

        
# ------------------------------------

print(longest)