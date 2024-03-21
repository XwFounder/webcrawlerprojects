#  参考地址： https://www.cnblogs.com/pikeduo/p/16938738.html
# 先说结论，现无法下载无损音乐，也不能下载vip音乐，此代码模拟的是web网页额js加密的过程，向api接口发送参数并获取数据。如果需要下载网易云音乐，不如直接在pc端下载
#  从学习的态度来说，还是从头到屋进行解析
# 1、在首页输入想要听的歌曲名称，获取api接口：https://music.163.com/weapi/cloudsearch/get/web?csrf_token=8795db31dc90d10559f885f9a8106b01
# 对api接口分析：请求方式：post，请求参数类型：application/x-www-form-urlencoded，请求参数：csrf_token，params，encSecKey三个参数，才能获取数据，否则就为空，
# 这里需要注意的是pc端当前网易云如果不进行登录，搜索不出来歌单，那就说明api接口必须要带csrf_token值。我现在也没有办法解决，如果你有这点思路的话，我们可以聊一下
# 那么如果获取这三个参数，可以在启动器上找个js代码，进入js界面，然后根据这三个值进行搜索
import base64
import codecs
import json
import math
import random

import requests
from Crypto.Cipher import AES


# var  bVi1x = window.asrsea(JSON.stringify(i7b), bsu0x(["流泪", "强"]), bsu0x(Xo3x.md),
#                       bsu0x(["爱心", "女孩", "惊恐", "大笑"]));
#       e7d.data = j7c.cr7k({
#     params: bVi1x.encText,
#     encSecKey: bVi1x.encSecKey
#       })
# 根据这些代码可以得出，在执行window.asrsea()函数后，生成了params和encSecKey，那window.asrsea()函数是什么，搜索asrsea,可以得出window.asrsea = d,
# 在找到d行数，function d(d, e, f, g) {
#          var h = {}
#            , i = a(16);
#          return h.encText = b(d, g),
#          h.encText = b(h.encText, i),
#          h.encSecKey = c(i, e, f),
#          h
#      }
#  这里可以看出X7Q = X7Q.replace("api", "weapi");，是走了这个函数方法对api转换成了weapi
#  这里总共涉及到3个函数方法a,b,c,四个参数d,e,f,g,先不着急研究a，b,c,d 四个函数的作用，先研究下d,e,f,g这四个参数，从前面可以看出这四个参数其实是
#  window.asrsea(SON.stringify(i7b), bsu0x(["流泪", "强"]), bsu0x(Xo3x.md),bsu0x(["爱心", "女孩", "惊恐", "大笑"]) )
#  那么就可以从window.asrsea这里进行断点调试了，从调试出来的结果看出
#   i7b: csrf_token: "534c3a0c31c8f8f6a6204182c9e705b1"
#   JSON.stringi.:"{\"csrf_token\":\"534c3a0c31c8f8f6a6204182c9e705b1\"}"
#   bsu0x(["流泪"，"强"])："010001"
#   bs:"08e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b7.-
#   bsux(["爱心"，"女孩"，"惊恐"，"大笑"])："0CoJUm60w8N8jud"
#  'd': "{\"csrf_token\":\"534c3a0c31c8f8f6a6204182c9e705b1\"}",
#     'e': "010001",
#     'f': "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7",
#     'g': "0CoJUm6Qyw8W8jud"
#  在网上找的资料看出来我们要搜索的歌曲名称是在d在当中的，但我在当前网易云映玥下载那边没有找到对应的名称，我有可能会到获取token那边的接口查找下究竟放到那边的，不过不是现在要等到后续，现在的情况可以已经基本确定了d、e、f、g的参数情况了


#  2、函数分析
#  分析a，b,c,d 四钟函调用数
#   function a(a) {
#         var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
#         for (d = 0; a > d; d += 1)
#             e = Math.random() * b.length,
#             e = Math.floor(e),
#             c += b.charAt(e);
#         return c
#     }
# 根据我非常烂的js知识来看，b应该是随机字符串，函数接收字符串的长度，改成python代码就是
# 获取一个随机字符串、length是字符串长度
def generate_str(length):
    str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    res = ""
    for i in range(length):
        index = random.random() * len(str)  # 获取一个字符串的随机长度
        index = math.floor(index)  # 向下调整
        res = res + str[index]  # 累加成一个随机字符串
    return res


#  b()函数
#    function b(a, b) {
#         var c = CryptoJS.enc.Utf8.parse(b)
#           , d = CryptoJS.enc.Utf8.parse("0102030405060708")
#           , e = CryptoJS.enc.Utf8.parse(a)
#           , f = CryptoJS.AES.encrypt(e, c, {
#             iv: d,
#             mode: CryptoJS.mode.CBC
#         });
#         return f.toString()
#  这段js代码是基于AES（高级加密标准）加密过程，用于对输入的字符串进行加密
# 1、CryptoJS.enc.Utf8.parse() 将字符串转换为utf-8的字符数组
# 2、CryptoJS.AES.encrypt()这个函数是使用AES算法进行加密的核心部分。它接受三个参数：待加密的数据、加密密钥和一些参数选项，a是加密内容也是encText、b是固定参数，CryptoJS.mode.CBC表示使用CBC模式进行加密。
#  转换成Python代码就要参考py AES的加密过程
#  AESj加密获取param
def AES_encrypt(text, key):
    iv = '0102030405060708'.encode('utf-8')  # iv偏移量
    text = text.encode('utf-8')  # 将明文转换为utf-8格式
    pad = 16 - len(text) % 16
    text = text + (pad * chr(pad)).encode('utf-8')  # 明文需要转成二进制，且可以被16整除
    key = key.encode('utf-8')  # 将密钥转换为utf-8格式
    encryptor = AES.new(key, AES.MODE_CBC, iv)  # 创建一个AES对象
    encrypt_text = encryptor.encrypt(text)  # 加密
    encrypt_text = base64.b64encode(encrypt_text)  # base4编码转换为byte字符串
    return encrypt_text.decode('utf-8')


#  c函数
#     function c(a, b, c) {
#         var d, e;
#         return setMaxDigits(131),
#         d = new RSAKeyPair(b,"",c),
#         e = encryptedString(d, a)
#     }
#  这段js代码的作用：c函数是RSA加密过程，其中a是随机字符串，b是一个key，也就是上面四个参数中的e，f也是四个参数中的f，返回的是encSeckey
# 由于本人学习的js知识十分粗浅，因此难以看懂这段代码，参考网上流传的版本，改写了代码
#  等到的结果：
#   e = '010001'
#  f="00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"

# RSA加密获得encSeckey
def RSA_encrypt(str, key, f):
    str = str[::-1]  # 随机字符串逆序排列
    str = bytes(str, 'utf-8')  # 将随机字符串转换为byte类型的数据
    sec_key = int(codecs.encode(str, encoding='hex'), 16) ** int(key, 16) % int(f, 16)  # RSA加密
    return format(sec_key, 'x').zfill(256)  # RSA加密后字符串长度为256，不足的补x


#  d函数
# js代码片段：
# function b(a, b) {
#         var c = CryptoJS.enc.Utf8.parse(b)
#           , d = CryptoJS.enc.Utf8.parse("0102030405060708")
#           , e = CryptoJS.enc.Utf8.parse(a)
#           , f = CryptoJS.AES.encrypt(e, c, {
#             iv: d,
#             mode: CryptoJS.mode.CBC
#         });
#         return f.toString()
#     }
# 总结： 这段代码的作用是将输入的字符串使用AES算法和cbc算法进行混合加密，并返回加密后的结果，加密过程中使用了指定的密神额初始向量，来保障了加密的安全性
# 分析：
#
# 首先，将密钥 b 转换为UTF-8编码的字节数组。
#
# 然后，将固定初始向量（IV） "0102030405060708" 转换为UTF-8编码的字节数组。可以定式
#
# 接着，将待加密的字符串 a 转换为UTF-8编码的字节数组。
#
# 使用AES算法和CBC模式，通过调用 CryptoJS.AES.encrypt() 函数对 e 进行加密。传入的参数包括：待加密的数据、加密密钥 c 和初始向量 d。
# 获取参数
def get_params(d, e, f, g):
    i = generate_str(16)  # 生成一个16位的随机字符串
    # i = 'aO6mqZksdJbqUygP'
    encText = AES_encrypt(d, g)
    print(encText)    # 打印第一次加密的params，用于测试d正确
    params = AES_encrypt(encText, i)  # AES加密两次后获得params
    encSecKey = RSA_encrypt(i, e, f)  # RSA加密后获得encSecKey
    return params, encSecKey


#  3、分析返回结果
# 我们知道参数和接口后，就可以向服务器发送请求，获取返回结果，注意请求为post请求

e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"


# 传入msg和url,获取返回的json数据
def get_data(msg, url):
    encText, encSecKey = get_params(msg, e, f, g)  # 获取参数
    params = {
        "params": encText,
        "encSecKey": encSecKey
    }
    headers ={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Referer": "https://music.163.com/search/",
        'Content-Type': 'application/x-www-form-urlencoded',

    }
    re = requests.post(url=url, params=params, verify=True,headers=headers)  # 向服务器发送请求
    return re


# 搜索放回的结果
def main():
    json_data = r'{"logs": "[{\"action\":\"impress\",\"json\":{\"mspm\":\"619df35ce51b6b383f5fafdb\",\"page\":\"mainpage\",\"module\":\"nav_bar\",\"target\":\"friends\",\"reddot\":\"1\",\"mainsite\":\"1\"}}]","csrf_token": "534c3a0c31c8f8f6a6204182c9e705b1"}'
    serch_msg = json_data
    serch_url = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token='
    # 文档中是为登录下的状态，三个参数e,f,g固定不变，只更改msg的值。但登录后直接可以固定下来这个值
    res_data= get_data(serch_msg, serch_url)
    # data = json.loads(res_data.json())
    print(res_data.content)

# 2、音乐信息
# 1、歌词：点击一个音乐进入播放界面，打开F12，筛选后一个一个链接寻找 https://music.163.com/weapi/song/lyric?csrf_token=534c3a0c31c8f8f6a6204182c9e705b1，此链接返回歌词信息
# {
#     "sgc": false,
#     "sfy": false,
#     "qfy": false,
#     "transUser": {
#         "id": 2204059,
#         "status": 99,
#         "demand": 1,
#         "userid": 76837043,
#         "nickname": "烈焰中舞动的火花",
#         "uptime": 1493803368844
#     },
#     "lyricUser": {
#         "id": 2204040,
#         "status": 99,
#         "demand": 0,
#         "userid": 114415020,
#         "nickname": "another_tonary",
#         "uptime": 1493803368844
#     },
#     "lrc": {
#         "version": 5,
#         "lyric": "[00:00.000] 作词 : 羽生みいな\n[00:00.515] 作曲 : Meis Clauson\n[00:01.30]自由の翅\n[00:02.78]月影のシミュラクル -解放の羽- 0P主題歌\n[00:10.45]\n[00:23.35]ここから見る景色は 何故どこか狭く悲しく ah\n[00:32.97]声にならない声で そう君を呼んでいたんだ ah\n[00:43.17]逃げられない蝶のように\n[00:48.00]最期を待つだけじゃないと\n[00:53.03]温かい手 重ねた瞬間（とき）\n[00:58.09]差し込んだ光\n[01:02.03]絡みつくこの糸が 交わされた契約が\n[01:07.14]どれほど命 縛ろうとも\n[01:11.97]いつの日かこの翅(はね）を精一杯広げて\n[01:17.10]君が傍に居てくれるなら\n[01:22.24]きっと飛び立てるの あの空へと\n[01:48.09]仕方のないことだと 何故諦めようとしてた ah\n[01:57.94]紅く染まる暗闇から 抜け出せない気がして ah\n[02:08.16]それでもまだ君と生きたい\n[02:13.07]繫いだ手は震えるけど\n[02:18.05]熱い涙 溢れた瞬間（とき）\n[02:23.06]湧き上がる勇気\n[02:27.08]捕らわれた運命が 立ちはだかる試練が\n[02:32.11]どれほどこの身操ろうとも\n[02:37.00]立ち向かいたい 強く信じるの もっと強く\n[02:42.14]独りじゃないと思えた 君となら\n[02:48.93]飛び立てるの あの空へと\n[02:53.53]忘れかけてた 遠い記憶 あの約束 思い出して\n[03:03.27]取り戻せるの 二人ならば 広い世界を\n[03:12.20]絡みつくこの糸が 交わされた契約が\n[03:17.08]どれほど命 縛ろうとも\n[03:22.01]いつの日かこの翅を 精一杯広げて\n[03:27.06]君が傍に居てくれるなら\n[03:32.00]きっと 光の向こう\n[03:37.11]捕らわれた運命が 立ちはだかる試練が\n[03:42.08]どれほどこの身操ろうとも\n[03:46.93]立ち向かいたい 強く信じるの もっと強く\n[03:52.09]独りじゃないと思えた 君となら\n[03:58.82]飛び立てるの あの空へと\n"
#     },
#     "tlyric": {
#         "version": 5,
#         "lyric": "[by:所間]\n[ti:自由の翅]\n[ar:佐藤ひろ美]\n[al:月影のシミュラクル -解放の羽- 初回限定同梱 オリジナルサウンドトラック]\n[00:01.30]\n[00:02.78]\n[00:10.45]\n[00:23.35]这里所看到的景色 为何会感到如此狭小又悲伤 ah\n[00:32.97]以泣不成声的声音 不断呼喊着你 ah\n[00:43.17]如同无法挣脱的蝴蝶一般\n[00:48.00]只能默默等候终焉的到来\n[00:53.03]温暖的双手重合的瞬间\n[00:58.09]感受到了照射的光芒\n[01:02.03]不管这纠缠不清的丝线与这被迫签下的契约\n[01:07.14]究竟束缚了多少的生命\n[01:11.97]总有一天要用这双翅膀 用尽全力展翅翱翔\n[01:17.10]只要你能够陪伴在我身边\n[01:22.24]一定就能够展翅高飞 向着那片天空\n[01:48.09]为何要说着“这是无可奈何的事情”而准备去放弃一切呢 ah\n[01:57.94]就算觉得无法从这渐渐染红的黑暗中逃脱出去 ah\n[02:08.16]即便如此仍旧想要与你一同活下去\n[02:13.07]虽然紧牵着的手止不住颤抖\n[02:18.05]温热的泪水 满溢的瞬间\n[02:23.06]心中所涌出的勇气\n[02:27.08]不管这被囚禁的命运与这艰辛的试炼\n[02:32.11]会让这幅身躯会承受多少伤害\n[02:37.00]就算如此也想要奋发向上 不断坚信着 变得更加坚强\n[02:42.14]与你在一起的话 就不会感到孤独\n[02:48.93]向着那片天空展翅高飞\n[02:53.53]从将要遗忘的记忆中找回了那个约定\n[03:03.27]我们一起的话 就能夺回那个宽广的世界\n[03:12.20]不管这纠缠不清的丝线与这被迫签下的契约\n[03:17.08]究竟束缚了多少的生命\n[03:22.01]总有一天要用这双翅膀 用尽全力展翅翱翔\n[03:27.06]只要你能够陪伴在我身边\n[03:32.00]肯定就在那光芒的彼岸\n[03:37.11]不管这被囚禁的命运与这艰辛的试炼\n[03:42.08]会让这幅身躯会承受多少伤害\n[03:46.93]就算如此也想要奋发向上 不断坚信着 变得更加坚强\n[03:52.09]与你在一起的话 就不会感到孤独\n[03:58.82]向着那片天空展翅高飞"
#     },
#     "code": 200
# }
# 其中transUser为歌词贡献者，lyricUser为歌词翻译贡献者，lrc里有原版歌词，tlyric里有歌词翻译
# 解析过程和上面一样，调试页面找到d的值即可。
d = '{"id":"473403600","lv":-1,"tv":-1,"csrf_token":""}'
# 歌词文件
lyric_msg = '{"id":"427419615","lv":-1,"tv":-1,"csrf_token":""}'
lyric_url = 'https://music.163.com/weapi/song/lyric?csrf_token='
print(get_data(lyric_msg, lyric_url))
# （2）评论
# https://music.163.com/weapi/comment/resource/comments/get?csrf_token=返回用户评论信息，目前还不需要，不使用。
# （3）音乐信息
# 点击蓝色的播放按钮，发现由多出了一些链接，一个一个找下来。
# https://music.163.com/weapi/v3/song/detail?csrf_token=534c3a0c31c8f8f6a6204182c9e705b1 音乐信息数据
# 注意，这里调试时需要一点技巧，刷新页面，首先在源码里打个断点
# 音乐详细信息,包含了音质等级和可下载权限
detail_msg = r'{"id":"473403600","c":"[{\"id\":\"473403600\"}]","csrf_token":""}'
detail_url = 'https://music.163.com/weapi/v3/song/detail?csrf_token='
print(get_data(detail_msg, detail_url))
# 注意msg要加上r，id为音乐id，可更改，其实没有这个也行，在搜索时，返回的数据里就有音乐的详细信息了。
# 音乐下载地址，level代表音质等级，encodeType代表编码类型，flac可存储无损音质，目前无法下载无损音乐
# 音质 standard标准 higher较高 exhigh极高 lossless无损 hires
# 编码类型 aac flac
song_msg = '{"ids":"[473403600]","level":"lossless","encodeType":"flac","csrf_token":""}'
song_url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token='
print(get_data(song_msg, song_url))
# ids里面是音乐id，既然是一个数组，那想必可以多加几个音乐id，返回多个下载地址。level为音质水平，分四个等级，standard代表标准，higher代表较高，
# exhigh代表极高，lossless代表无损，还有hires，其中lossless和hires都无法下载，不知道加上有会员权限的csrf_token能不能下载。


if __name__ == '__main__':
    main()
