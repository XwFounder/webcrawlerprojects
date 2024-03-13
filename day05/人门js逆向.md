# 1.关于js逆向
什么事js逆向：在页面输入密码: wanruiba,但提交后密码居然变成(密文)：c739492f2837ed5c6927914a55467874。
这其实是，在网页中的JS代码在发送请求之前，对我们的密码进行了处理（加密）。
如果我们后续想要模拟请求发送时、必须去网站中找到他的加密方式或加密算法，然后用代码实现加密+请求发送而我们根据现象，**去网站的js代码寻找算法的行为，就是js逆向**

# 2 逆向实战
## 北大未名案例
逻辑分析行为步骤：分析、断点调试、实现

分析：

1、警提请求cookie中的skey，因为他很想登录后的凭证，skey是一个字符串类型 ，login()请求中的载荷要注意对应的t,
    而要怎么进行逆向？，首先筛选js代码片段，浏览器选择Fatch/XHR，点击启动器，那就可以看到关于触发这个行为或者代码发起的行为,选择对应的方法查看
```js
 var r = BDWM.getGlobalTimestamp()
                  , s = CryptoJS.MD5(i + n + r + i).toString().toLowerCase();
                $.post("ajax/login.php", {
                    username: n,
                    password: i,
                    keepalive: $('input[name="keepalive"]').prop("checked") ? 1 : 0,
                    time: r,
                    t: s
                }, function(e) {})
```
通过上面的js代码片段可以看出，t是密码的加密方式，而使用的加密方式是MD5算法进行加密的，在分析下(i + n + r + i)可以得出MD5加密的方式
i:密码,n：账号，r：时间戳；北大未名网址使用的MD5算法，通过密码、账号、时间戳、密码的方式进行加密，得到t这个MD5加密后值，在进行js逆向时要注重的是他们的加密方式、加密的规则又是什么，然后通过一系列的分析与测试等到真正的加密方式
2、可以用上**在线加密工具**，配合分析

# 3 媒想到
https://www.94mxd.com.cn/signin

1、分析
寻找发送lgoin()js代码片段,以及部门关键代码
```js
// 关键代码片段
setMethod('POST')
             .setHeader({
                 'Content-Type': 'application/json'
     }) 
// 设置发送请求未json格式
```
```js
  pwd = hashPwd(pwd);
// 根据已知信息，显示对pwd进行加密，有可能走了这个方法进行加密，而hashPwd方法就是在import {checkEmail, checkPassword, getUrlArg, hashPwd} from "../utils"; 这个包里面
export function hashPwd(pwd) {
    pwd = md5(pwd + 'Hq44cyp4mT9Fh5eNrZ67bjifidFhW%fb0ICjx#6gE59@P@Hr8%!WuYBa1yvytq$qh1FEM18qA8Hp9m3VLux9luIYpeYzA2l2W3Z');
    return pwd;
}
// 加密方式通过md5加密，加密规则：pwd+固定值
```
最后的结果
```pycon
import hashlib
import requests

data_string = "qwe123456" + "Hq44cyp4mT9Fh5eNrZ67bjifidFhW%fb0ICjx#6gE59@P@Hr8%!WuYBa1yvytq$qh1FEM18qA8Hp9m3VLux9luIYpeYzA2l2W3Z"
obj = hashlib.md5()
obj.update(data_string.encode("utf-8"))
md5_string = obj.hexdigest()
res = requests.post(
    url="https://www.94mxd.com.cn/mxd/user/signin",
    json={
        "email": "22107@163.com",
        "password": md5_string
    },
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Content-Type": "application/json",
        "Referer": "https://www.94mxd.com.cn/signin",
        "Origin": "https://www.94mxd.com.cn"
    }
)
print(res.text)
print(res.cookies.get_dict())
```

