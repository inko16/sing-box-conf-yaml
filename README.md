# sing-box 配置文件 YAML版，可转为json
### # 可以日常使用了，需要自己改节点
（cf worker 这个js需要改，需要改。不完善，但能用）

原理: yaml/json在不使用<<锚点时可以等价转换(利用jsonyaml.py, [该实现见旧Branch](https://github.com/inko16/sing-box-conf-yaml/tree/jsonyaml-equal))。旧Branch的实现非常简洁，仅使用最基础的yaml转换json并直接交给singbox使用。

但当yaml中使用了<<这种锚点方式进行引用，简写重复部分时，被复制的地方也会写入json。而singbox目前好像还不可以忽略json中的无意义参数（提示的是error而不是warning），以至于不能像Clash那样写出自由飘逸的配置。

于是我在yaml里写了一行注释，这是singbox文档给出的json结构。
```
# singbox{log,dns,ntp,inbounds,outbounds,route,experimental}
```
并在 [worker](yamljson.cfworker.js) 中处理完yaml-json后，仅将以上内容返回，也就是以上内容外面的所有锚点内容全部舍弃。这样可以提供一定程度的自由度，以及可以跟随singbox对配置文件结构更新。

####  从yaml"编译"为json（yaml可以转为等价json）. 使用示例
```
# bash on windows(admin), with cf worker yaml-json filter
curl https://a.pages.dev/yamljson/a.github.io/conf/sing.yaml -o $TMP/singtmp.json && ~/singbox/sing-box run -c $TMP/singtmp.json
# for your profile security you need to host it safely. this is just an example

```
#####  yaml转为等价json见 [branch jsonyaml-equal](https://github.com/inko16/sing-box-conf-yaml/tree/jsonyaml-equal) 分支
---
- 默认使用tun模式，Windows下需要管理员权限，Android下正常工作。mixed模式(系统代理)好久没用了。
### 进度
- 路由规则需要完善, dns规则需要完善
- tun模式下，节点不支持udp的情况下打开https（h3 quic:8443）时不回落到h2。curl没问题，chrome不行
- 开启sniff-override，好像变慢了，fakeip在tun模式默认使用，弥补dns解析和sniff的损耗。
- iOS不方便使用Testflight，我需要把1.9-rc版的功能注释掉，等1.9正式版出来再用。还没改。
- ...
---
### 重大缺陷
- 官方版不支持node providers还得额外把节点塞进去。不考虑第三方core，因为他们不支持iOS。
- 实测湖北移动不能用。有理由怀疑墙中墙，目前没时间也没有条件处理。
---
### Why this project:
- Sing-box on iOS is free 可以降低用户门槛，我希望更多人能够使用真正的网络
- YAML is human-friendly
- Official sing-box conf, not for third-party modified client, so that iOS can use this.

---
### 吐槽：
- yaml json明明差不多，人家小猫咪配置能写的那么舒服，这音乐盒一大堆括号看着都头疼，音乐盒何必用json呢
- 音乐盒你官方版为什么不搞node provider啊喂，json还没yaml灵活，yaml里引入写个花活还给我报错呜（这个branch就尽量解决一下这个问题）
- 吐槽归吐槽，音乐盒确实还是牛逼
---

[geosite srs编译记录
](https://github.com/SagerNet/sing-geosite/actions/runs/8311894714/job/22746155812
), [geosite 来源](https://github.com/v2fly/domain-list-community/tree/master/data
)

---
### 备注
- 随便用，但发布在Github上以此修改的希望可以留个这个repo的link
- 强烈希望机场主们能用用sing-box，见Why this project
- 文件内的一些数字视作随机数，我脸砸键盘打的。
---
本地用Python的pyyaml转换json示例：
jsonyaml.py可以清晰看到json和yaml几乎是同一个东西，但可读性一个天上一个地下。
注：由于锚点转换会造成json/yaml不等价，该python工具在本branch仅测试用。详见 [branch jsonyaml-equal](https://github.com/inko16/sing-box-conf-yaml/tree/jsonyaml-equal)
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
