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

---
### 吐槽：
- yaml json明明差不多，人家小猫咪配置能写的那么强，这音乐盒一大堆括号看着都头疼，音乐盒何必用json呢
- 音乐盒你官方版为什么不搞node provider啊喂，json还没yaml灵活，yaml里引入写个花活还给我报错呜
- 别问我为啥不改singbox，我想兼容官方版，我不确定哪个修改版是最广泛使用的，不像人家mihomo

---
### 路由思路：
- 【神奇流量】常用的部分走direct
- 一些不怎么登陆的、可能影响隐私的【神奇流量】走proxy
- 其余统统走proxy
