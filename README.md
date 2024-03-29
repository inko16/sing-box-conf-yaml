# # Still working

bash on windows(recommended):
```
./jsonyaml.py conf.yaml > $TMP/singbox-test.json && ./sing-box run -c $TMP/singbox-test.json
```

---
```
jsonyaml.py a.json > a.yaml
cat a.json | jsonyaml.py > a.yaml
jsonyaml.py b.yaml > b.json

Windows CMD:
jsonyaml.py > a.yaml
Right Click (Paste json)
Enter(New Line)
Ctrl+Z ^Z(EOF) Enter
```


---
### Why this project:
- Sing-box on iOS is free
- YAML is human-friendly
