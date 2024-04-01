# sing-box 配置文件 YAML版，可直接转为json
### # 可以日常使用了

从yaml"编译"为json（yaml可以转为等价json）
```
# bash on windows(recommended)(admin needed):

./jsonyaml.py conf.yaml min > $TMP/singbox-test.json && \
./sing-box run -c $TMP/singbox-test.json
```
---
- 默认使用tun模式，Windows下需要管理员权限，Android下正常工作。mixed模式应该是正常的。
### 进度
- 路由规则需要完善, dns规则需要完善
- tun模式下，节点不支持udp的情况下打开https（h3 quic:8443）时不回落到h2。curl没问题，chrome不行
- 开启sniff-override，好像变慢了，fakeip在tun模式默认使用，弥补dns解析和sniff的损耗。
- iOS不方便使用Testflight，我需要把1.9-rc版的功能注释掉，等1.9正式版出来再用。还没改。
- ...
---
### 重大缺陷
- 官方版不支持node providers还得额外把节点塞进去。不考虑第三方core，因为他们不支持iOS。
---
### Why this project:
- Sing-box on iOS is free 可以降低用户门槛，我希望更多人能够使用真正的网络
- YAML is human-friendly
- Official sing-box conf, not third-party modified, so that iOS can use this.

---
### 吐槽：
- yaml json明明差不多，人家小猫咪配置能写的那么舒服，这音乐盒一大堆括号看着都头疼，音乐盒何必用json呢
- 音乐盒你官方版为什么不搞node provider啊喂，json还没yaml灵活，yaml里引入写个花活还给我报错呜
- 吐槽归吐槽，音乐盒还是牛逼

---
jsonyaml.py可以清晰看到json和yaml几乎是同一个东西，但可读性一个天上一个地下。
```
# pip install pyyaml
jsonyaml.py a.json > a.yaml
cat a.yaml | jsonyaml.py > a.json
---
Windows CMD Debug(for reading official doc use):
jsonyaml.py > a.yaml
Right Click (Paste json), Enter(New Line)
Ctrl+Z ^Z(EOF) Enter
```
[geosite srs编译记录
](https://github.com/SagerNet/sing-geosite/actions/runs/8311894714/job/22746155812
), [geosite 来源](https://github.com/v2fly/domain-list-community/tree/master/data
)
