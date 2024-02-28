funcdef = "run = function(f, a)"
funcdef = funcdef + "\n    if a.len == 0 then return f"

args = []
for i in range(0, 100):
    args.append("a["+str(i)+"]")
    line = "\n{tab}if a.len == {len} then return f({args})"
    funcdef = funcdef + line.format(tab=" "*4, len=i+1, args=", ".join(args))

funcdef = funcdef + "\nend function"
print(funcdef)
