# -*- coding: utf-8 -*-
import json
import logging

from django.core.management import BaseCommand

from album.models import MusicTag, Music


logger = logging.getLogger(__name__)

tag_mapping = {
    'sweet': {
        'id': 1,
        'name': '甜蜜',
    },
    'quiet': {
        'id': 2,
        'name': '安静',
    },
    'relax': {
        'id': 3,
        'name': '轻松',
    },
    'lonely': {
        'id': 4,
        'name': '寂寞',
    },
    'happy': {
        'id': 5,
        'name': '开心',
    },
}

music_info = json.loads('''
{
    "musicList": [

        {
            "id": "217",
            "type": "sweet",
            "name": "最初から今まで",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002GFRZG3eQ2U1.m4a?fromtag=0",
            "lyricUrl": ""
        },
        {
            "id": "216",
            "type": "sweet",
            "name": "月光小夜曲纯音乐",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002nD8Sn2sZqfO.m4a?fromtag=0",
            "lyricUrl": ""
        },
        {
            "id": "215",
            "type": "sweet",
            "name": "麦浪",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C1000019fgPk0KeWsI.m4a?fromtag=0",
            "lyricUrl": ""
        },
        {
            "id": "214",
            "type": "sweet",
            "name": "Sunburst",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003PL8Kc3EksFh.m4a?fromtag=0",
            "lyricUrl": ""
        },
        {
            "id": "213",
            "type": "sweet",
            "name": "桜花雨—纯音乐",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002CHUdT3fWgTF.m4a?fromtag=0",
            "lyricUrl": ""
        },
        {
            "id": "212",
            "type": "sweet",
            "name": "Life—Tobu",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002iZhy72Lwxuk.m4a?fromtag=0",
            "lyricUrl": ""
        },
        {
            "id": "211",
            "type": "sweet",
            "name": "sunshine girl",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001Kgauq2ltF8G.m4a?fromtag=0",
            "lyricUrl": ""
        },
        {
            "id": "210",
            "type": "sweet",
            "name": "我们",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100004EyWdO4JZgOn.m4a?fromtag=0",
            "lyricUrl": ""
        },
        {
            "id": "209",
            "type": "sweet",
            "name": "父亲",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100004TSZYg2HaHQi.m4a?fromtag=0",
            "lyricUrl": "lyric/music_209.lrc"
        },
        {
            "id": "208",
            "type": "sweet",
            "name": "缄默",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001ngrj12i7gj5.m4a?fromtag=0",
            "lyricUrl": ""
        },
        {
            "id": "207",
            "type": "sweet",
            "name": "时间都去哪了",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000Qp2Rl3zYVro.m4a?fromtag=0",
            "lyricUrl": "lyric/music_207.lrc"
        },
        {
            "id": "206",
            "type": "sweet",
            "name": "morning",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100004JoOgT1zSO5x.m4a?fromtag=0",
            "lyricUrl": ""
        },
        {
            "id": "205",
            "type": "sweet",
            "name": "我要你",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002XPp4023M50E.m4a?fromtag=0",
            "lyricUrl": "lyric/music_205.lrc"
        },
        {
            "id": "204",
            "type": "sweet",
            "name": "刚好遇见你",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000LBcVm0d9raf.m4a?fromtag=0",
            "lyricUrl": "lyric/music_204.lrc"
        },
        {
            "id": "203",
            "type": "sweet",
            "name": "Summer——久石譲",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000wtbud2Xm0MT.m4a?fromtag=0",
            "lyricUrl": ""
        },
        {
            "id": "202",
            "type": "sweet",
            "name": "故国风——陈佩廷",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003KxjhV3gdpO3.m4a?fromtag=0",
            "lyricUrl": ""
        },
        {
            "id": "201",
            "type": "sweet",
            "name": "一生有你",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002pYWH50s7112.m4a?fromtag=0",
            "lyricUrl": "lyric/music_198.lrc"
        },
        {
            "id": "200",
            "type": "sweet",
            "name": "轻音乐",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000Wuinm0djxPP.m4a?fromtag=0",
            "lyricUrl": ""
        },
        {
            "id": "199",
            "type": "sweet",
            "name": "三生三世——张杰",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000hscqh1l8UlG.m4a?fromtag=0",
            "lyricUrl": ""
        },
        {
            "id": "198",
            "type": "sweet",
            "name": "女人花——梅艳芳",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000x65VD4BdGIQ.m4a?fromtag=0",
            "lyricUrl": ""
        },
        {
            "id": "197",
            "type": "sweet",
            "name": "Love Paradise——陈慧琳 ",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001AL45O06AXLi.m4a?fromtag=0",
            "lyricUrl": "lyric/music_197.lrc"
        },
        {
            "id": "187",
            "type": "sweet",
            "name": "你在就好 ",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001QOfXA0OwPPH.m4a?fromtag=0",
            "lyricUrl": "lyric/music_187.lrc"
        },
        {
            "id": "186",
            "type": "sweet",
            "name": "寂寞的人伤心的歌 ",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002oADQI2zk0Ky.m4a?fromtag=0",
            "lyricUrl": "lyric/music_186.lrc"
        },
        {
            "id": "185",
            "type": "sweet",
            "name": "天若有情 ",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003elgGQ3c1uQN.m4a?fromtag=0",
            "lyricUrl": "lyric/music_185.lrc"
        },
        {
            "id": "184",
            "type": "sweet",
            "name": "告白气球 ",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003OUlho2HcRHC.m4a?fromtag=0",
            "lyricUrl": "lyric/music_184.lrc"
        },
        {
            "id": "183",
            "type": "sweet",
            "name": "大约在冬季 ",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002k94ea4379uy.m4a?fromtag=0",
            "lyricUrl": "lyric/music_183.lrc"
        },
        {
            "id": "182",
            "type": "sweet",
            "name": "好日子 ",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002ZVHJ14bAWAh.m4a?fromtag=0",
            "lyricUrl": "lyric/music_182.lrc"
        },
        {
            "id": "181",
            "type": "sweet",
            "name": "义勇军进行曲 ",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002QB8771D3mif.m4a?fromtag=0",
            "lyricUrl": "lyric/music_181.lrc"
        },
        {
            "id": "180",
            "type": "sweet",
            "name": "爱我中华 ",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003d8yDd2dmxv3.m4a?fromtag=0",
            "lyricUrl": "lyric/music_180.lrc"
        },
        {
            "id": "179",
            "type": "sweet",
            "name": "月满西楼 ",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002HuVt830ZOcB.m4a?fromtag=0",
            "lyricUrl": "lyric/music_179.lrc"
        },

        {
            "id": "178",
            "type": "sweet",
            "name": "花好月圆夜 ",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000zoils1bHYZK.m4a?fromtag=0",
            "lyricUrl": "lyric/music_178.lrc"
        },
        {
            "id": "177",
            "type": "relax",
            "name": "花好月圆夜 ",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000zoils1bHYZK.m4a?fromtag=0",
            "lyricUrl": "lyric/music_177.lrc"
        },

        {
            "id": "176",
            "type": "relax",
            "name": "一生有你 ",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002pYWH50s7112.m4a?fromtag=0",
            "lyricUrl": "lyric/music_176.lrc"
        },
        {
            "id": "175",
            "type": "relax",
            "name": "最亮的心 ",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001NmPTG1fVsUw.m4a?fromtag=0",
            "lyricUrl": "lyric/music_175.lrc"
        },

        {
            "id": "174",
            "type": "relax",
            "name": "恭喜发财 ",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002RdOSi3EZM8f.m4a?fromtag=0",
            "lyricUrl": "lyric/music_174.lrc"
        },
        {
            "id": "173",
            "type": "relax",
            "name": "有时候 ",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001xSkKk2Hw75o.m4a?fromtag=0",
            "lyricUrl": "lyric/music_173.lrc"
        },

        {
            "id": "172",
            "type": "relax",
            "name": "独角戏 ",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001R67eW4YBJXa.m4a?fromtag=0",
            "lyricUrl": "lyric/music_172.lrc"
        },
        {
            "id": "171",
            "type": "happy",
            "name": "军中绿花 ",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000YaY8f1HqwWB.m4a?fromtag=0",
            "lyricUrl": "lyric/music_171.lrc"
        },
        {
            "id": "170",
            "type": "relax",
            "name": "咱们结婚吧 ",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001TqDdv4QWZqb.m4a?fromtag=0",
            "lyricUrl": "lyric/music_170.lrc"
        },
        {
            "id": "169",
            "type": "relax",
            "name": "七夕 ",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100004YrWpR44shMm.m4a?fromtag=0",
            "lyricUrl": "lyric/music_169.lrc"
        },
        {
            "id": "168",
            "type": "relax",
            "name": "渡红尘 ",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001RYNBo3AK8pp.m4a?fromtag=0",
            "lyricUrl": "lyric/music_168.lrc"
        },
        {
            "id": "167",
            "type": "relax",
            "name": "以后的以后 ",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001cP3t82HI31e.m4a?fromtag=0",
            "lyricUrl": "lyric/music_167.lrc"
        },
        {
            "id": "166",
            "type": "relax",
            "name": "樱花草 ",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001xiJdl0t4NgO.m4a?fromtag=0",
            "lyricUrl": "lyric/music_166.lrc"
        },
        {
            "id": "165",
            "type": "relax",
            "name": "荷塘月色 ",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100004Zeemn1ScQMX.m4a?fromtag=0",
            "lyricUrl": "lyric/music_165.lrc"
        },
        {
            "id": "164",
            "type": "relax",
            "name": "父亲 ",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100004TSZYg2HaHQi.m4a?fromtag=0",
            "lyricUrl": "lyric/music_164.lrc"
        },

        {
            "id": "163",
            "type": "relax",
            "name": "当你老了 ",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000J9uzi2jx51d.m4a?fromtag=0",
            "lyricUrl": "lyric/music_163.lrc"
        },
        {
            "id": "162",
            "type": "relax",
            "name": "风吹麦浪 ",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C1000019fgPk0KeWsI.m4a?fromtag=0",
            "lyricUrl": "lyric/music_162.lrc"
        },
        {
            "id": "161",
            "type": "relax",
            "name": "阳光宅男 ",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001bnNGN127Kbq.m4a?fromtag=0",
            "lyricUrl": "lyric/music_161.lrc"
        },
        {
            "id": "160",
            "type": "relax",
            "name": "渔家傲.忆端午 ",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001qeJep4YldZi.m4a?fromtag=0",
            "lyricUrl": ""
        },
        {
            "id": "159",
            "type": "relax",
            "name": "快乐小宇宙",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003tmKzk12Yr3e.m4a?fromtag=0",
            "lyricUrl": ""
        },
        {
            "id": "158",
            "type": "relax",
            "name": "童年",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100004YZMGx1EXDgl.m4a?fromtag=0",
            "lyricUrl": "lyric/music_158.lrc"
        },
        {
            "id": "157",
            "type": "relax",
            "name": "两情相悦",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001Mxe9a440fag.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "156",
            "type": "relax",
            "name": "白天不懂夜的黑",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C1000010G1U73qRdAB.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "155",
            "type": "relax",
            "name": "秋风落叶",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003MyZlI0kFgAD.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "154",
            "type": "relax",
            "name": "快乐宝贝",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000CGTjr1aQAUj.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "153",
            "type": "relax",
            "name": "旅行的意义",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001ojJlO3h2XuK.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "152",
            "type": "relax",
            "name": "致青春",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002SWGnT13k5sD.m4a?fromtag=0",
            "lyricUrl": null
        },

        {
            "id": "151",
            "type": "relax",
            "name": "守护家",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000fhYAh36i31d.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "150",
            "type": "relax",
            "name": "星语星愿",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000aKoHL1IqG5O.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "149",
            "type": "relax",
            "name": "宁夏",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100004NFs8H4V8meS.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "148",
            "type": "lonely",
            "name": "紫色的花海",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C1000046MzPE2hdU4v.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "149",
            "type": "lonely",
            "name": "渔舟唱晚",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003Mqcva1uLPxz.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "147",
            "type": "lonely",
            "name": "桑吉平措-禅韵",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000Y61fa40UmNe.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "146",
            "type": "lonely",
            "name": "冷漠&何龙雨-错过缘分错过了你",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002DLCAC0wfqEA.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "145",
            "type": "happy",
            "name": "Twins-星光游乐园",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000WdVBm1QT41A.m4a?fromtag=0",
            "lyricUrl": ""
        },
        {
            "id": "144",
            "type": "happy",
            "name": "徐良-自由",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000V2zyj2dw3rV.m4a?fromtag=0",
            "lyricUrl": "lyric/music_143.lrc"
        },

        {
            "id": "137",
            "type": "lonely",
            "name": "张靓颖-是否",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003c7I3E0RkwCH.m4a?fromtag=0",
            "lyricUrl": "lyric/music_137.lrc"
        },
        {
            "id": "136",
            "type": "happy",
            "name": "张赫宣-我们不该这样的",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002fxPjv4WhI5E.m4a?fromtag=0",
            "lyricUrl": "lyric/music_136.lrc"
        },

        {
            "id": "134",
            "type": "lonely",
            "name": "马頔-南山南",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C1000030moFt21TOxK.m4a?fromtag=0",
            "lyricUrl": "lyric/music_134.lrc"
        },
        {
            "id": "133",
            "type": "happy",
            "name": "贝瓦儿歌-新年好",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003aFIzq0TJywb.m4a?fromtag=0",
            "lyricUrl": "lyric/music_133.lrc"
        },
        {
            "id": "132",
            "type": "happy",
            "name": "TFBOYS-大梦想家",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003hTE6N2jHGN5.m4a?fromtag=0",
            "lyricUrl": "lyric/music_132.lrc"
        },
        {
            "id": "131",
            "type": "happy",
            "name": "冯曦妤-A Little Love",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001IAqkK0p2b7s.m4a?fromtag=0",
            "lyricUrl": "lyric/music_131.lrc"
        },

        {
            "id": "129",
            "type": "lonely",
            "name": "黑子沛-老同学",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C1000017rQ5x2UKuMU.m4a?fromtag=0",
            "lyricUrl": "lyric/music_129.lrc"
        },
        {
            "id": "128",
            "type": "happy",
            "name": "黑鸭子-铃儿响叮当(英文版)",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002MDs9D297mKd.m4a?fromtag=0",
            "lyricUrl": "lyric/music_128.lrc"
        },
        {
            "id": "127",
            "type": "lonely",
            "name": "曹磊-车站",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001HMzzO4FpTh0.m4a?fromtag=0",
            "lyricUrl": "lyric/music_127.lrc"
        },
        {
            "id": "126",
            "type": "sweet",
            "name": "婚礼进行曲(门德尔松)",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002WC3EL1JOydg.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "125",
            "type": "sweet",
            "name": "梦中的婚礼",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003WYx6o1HgolF.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "124",
            "type": "sweet",
            "name": "李佳薇-感谢爱人",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003n07gK4Ee6hT.m4a?fromtag=0",
            "lyricUrl": "lyric/music_124.lrc"
        },
        {
            "id": "123",
            "type": "lonely",
            "name": "欧阳菲菲-感恩的心",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002ZJJXz3wPK24.m4a?fromtag=0",
            "lyricUrl": "lyric/music_123.lrc"
        },
        {
            "id": "122",
            "type": "lonely",
            "name": "周亮-感恩歌",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000JHDJm4OYCdX.m4a?fromtag=0",
            "lyricUrl": "lyric/music_122.lrc"
        },
        {
            "id": "121",
            "type": "relax",
            "name": "老狼-同桌的你",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000bb4fp0qHlpz.m4a?fromtag=0",
            "lyricUrl": "lyric/music_121.lrc"
        },
        {
            "id": "120",
            "type": "happy",
            "name": "周华健-朋友 (Live)",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000c3ohn2KPrcl.m4a?fromtag=0",
            "lyricUrl": "lyric/music_120.lrc"
        },
        {
            "id": "119",
            "type": "quiet",
            "name": "曹方-风吹过下雨天",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000tDl300uRW4V.m4a?fromtag=0",
            "lyricUrl": "lyric/music_119.lrc"
        },
        {
            "id": "118",
            "type": "quiet",
            "name": "仙女山的月亮",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002Kcj1N2TZBNe.m4a?fromtag=0",
            "lyricUrl": "lyric/music_118.lrc"
        },
        {
            "id": "117",
            "type": "lonely",
            "name": "风往北吹",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002N8xrS017IMc.m4a?fromtag=0",
            "lyricUrl": "lyric/music_117.lrc"
        },
        {
            "id": "116",
            "type": "lonely",
            "name": "你是我最爱的女人",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000yzXSe3pfYsN.m4a?fromtag=0",
            "lyricUrl": "lyric/music_116.lrc"
        },
        {
            "id": "115",
            "type": "relax",
            "name": "人民警察之歌",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100004g9HdS4HRfXr.m4a?fromtag=0",
            "lyricUrl": "lyric/music_115.lrc"
        },
        {
            "id": "114",
            "type": "quiet",
            "name": "人生何处不相逢",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003VpJoJ4Dw4Wp.m4a?fromtag=0",
            "lyricUrl": "lyric/music_114.lrc"
        },

        {
            "id": "112",
            "type": "sweet",
            "name": "至少还有你",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002QOSPX0bEK4f.m4a?fromtag=0",
            "lyricUrl": "lyric/music_112.lrc"
        },
        {
            "id": "111",
            "type": "sweet",
            "name": "月亮代表我的心",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001olDJ21HU1OT.m4a?fromtag=0",
            "lyricUrl": "lyric/music_111.lrc"
        },
        {
            "id": "110",
            "type": "sweet",
            "name": "小城故事",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001YoUs11jvsIK.m4a?fromtag=0",
            "lyricUrl": "lyric/music_110.lrc"
        },
        {
            "id": "109",
            "type": "sweet",
            "name": "我只在乎你",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100004YTPIV1dKIyK.m4a?fromtag=0",
            "lyricUrl": "lyric/music_109.lrc"
        },
        {
            "id": "108",
            "type": "sweet",
            "name": "甜蜜蜜",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000sdZNg1W94eK.m4a?fromtag=0",
            "lyricUrl": "lyric/music_108.lrc"
        },

        {
            "id": "106",
            "type": "relax",
            "name": "火苗",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003jRGq044xuI0.m4a?fromtag=0",
            "lyricUrl": "lyric/music_106.lrc"
        },
        {
            "id": "105",
            "type": "relax",
            "name": "高原蓝",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C1000019JQrV1zMaUN.m4a?fromtag=0",
            "lyricUrl": "lyric/music_105.lrc"
        },
        {
            "id": "104",
            "type": "relax",
            "name": "月光下的凤尾竹",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002fMT0k0XLu2G.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "103",
            "type": "relax",
            "name": "万水千山总是情",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003SDBHO2nEA2f.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "102",
            "type": "relax",
            "name": "琵琶语(古筝)",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003ROPdD2G7ylY.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "101",
            "type": "relax",
            "name": "红日",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001qy18T16r5ZO.m4a?fromtag=0",
            "lyricUrl": "lyric/music_101.lrc"
        },
        {
            "id": "100",
            "type": "happy",
            "name": "唐诗三百首",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C1000005nBz44H6swj.m4a?fromtag=0",
            "lyricUrl": "lyric/music_100.lrc"
        },
        {
            "id": "99",
            "type": "happy",
            "name": "小龙人",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100004GhUHU38GD0Y.m4a?fromtag=0",
            "lyricUrl": "lyric/music_99.lrc"
        },
        {
            "id": "98",
            "type": "happy",
            "name": "葫芦娃",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100004VT0bS0b3Cmu.m4a?fromtag=0",
            "lyricUrl": "lyric/music_98.lrc"
        },
        {
            "id": "97",
            "type": "happy",
            "name": "叮当猫",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001RDxZ12LaYaE.m4a?fromtag=0",
            "lyricUrl": "lyric/music_97.lrc"
        },
        {
            "id": "96",
            "type": "happy",
            "name": "采蘑菇的小姑娘",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002K3jml2D0Ai9.m4a?fromtag=0",
            "lyricUrl": "lyric/music_96.lrc"
        },
        {
            "id": "95",
            "type": "lonely",
            "name": "相见恨晚",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C1000024EahM3XyANc.m4a?fromtag=0",
            "lyricUrl": "lyric/music_95.lrc"
        },
        {
            "id": "94",
            "type": "lonely",
            "name": "伤痕",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000AmfL42HbvXN.m4a?fromtag=0",
            "lyricUrl": "lyric/music_94.lrc"
        },
        {
            "id": "93",
            "type": "lonely",
            "name": "当爱己成往事",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001UK2LJ0KU9ay.m4a?fromtag=0",
            "lyricUrl": "lyric/music_93.lrc"
        },
        {
            "id": "92",
            "type": "lonely",
            "name": "父亲",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100004TSZYg2HaHQi.m4a?fromtag=0",
            "lyricUrl": "lyric/music_92.lrc"
        },
        {
            "id": "91",
            "type": "lonely",
            "name": "十年",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001OyHbk2MSIi4.m4a?fromtag=0",
            "lyricUrl": "lyric/music_91.lrc"
        },
        {
            "id": "90",
            "type": "quiet",
            "name": "城里的月光",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002jAecU3mKDM1.m4a?fromtag=0",
            "lyricUrl": "lyric/music_90.lrc"
        },
        {
            "id": "89",
            "type": "quiet",
            "name": "好人好梦",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C1000035XwH21eRMxl.m4a?fromtag=0",
            "lyricUrl": "lyric/music_89.lrc"
        },
        {
            "id": "88",
            "type": "quiet",
            "name": "恋曲1990",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000Jd2XU1i8Dpj.m4a?fromtag=0",
            "lyricUrl": "lyric/music_88.lrc"
        },

        {
            "id": "86",
            "type": "quiet",
            "name": "心经",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003Bw6Bn2bGXX3.m4a?fromtag=0",
            "lyricUrl": "lyric/music_86.lrc"
        },
        {
            "id": "85",
            "type": "happy",
            "name": "Happy Birthday生日快乐",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001sTnpH11fDye.m4a?fromtag=0",
            "lyricUrl": "lyric/music_85.lrc"
        },

        {
            "id": "83",
            "type": "sweet",
            "name": "今天是你的生日",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001uyd8G0T0T8i.m4a?fromtag=0",
            "lyricUrl": "lyric/music_83.lrc"
        },
        {
            "id": "82",
            "type": "sweet",
            "name": "可爱的祖国",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100004Z1WJy1wDC2b.m4a?fromtag=0",
            "lyricUrl": "lyric/music_82.lrc"
        },
        {
            "id": "81",
            "type": "happy",
            "name": "歌唱祖国",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002B9WYu0DbTZL.m4a?fromtag=0",
            "lyricUrl": "lyric/music_81.lrc"
        },
        {
            "id": "80",
            "type": "sweet",
            "name": "花好月圆夜",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000zoils1bHYZK.m4a?fromtag=0",
            "lyricUrl": "lyric/music_80.lrc"
        },
        {
            "id": "79",
            "type": "relax",
            "name": "被风吹过的夏天",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C1000018qunY0L4Bkx.m4a?fromtag=0",
            "lyricUrl": "lyric/music_79.lrc"
        },

        {
            "id": "77",
            "type": "relax",
            "name": "每时每刻",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000b9FfW2qhhQX.m4a?fromtag=0",
            "lyricUrl": "lyric/music_77.lrc"
        },
        {
            "id": "197",
            "type": "sweet",
            "name": "新年快乐",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002YLNH63r3VIn.m4a?fromtag=0",
            "lyricUrl": ""
        },
        {
            "id": "196",
            "type": "sweet",
            "name": "大吉大利",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001oIRL31k5W0C.m4a?fromtag=0",
            "lyricUrl": "lyric/music_196.lrc"
        },
        {
            "id": "195",
            "type": "sweet",
            "name": "365个祝福",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000SEg1R3Dknct.m4a?fromtag=0",
            "lyricUrl": "lyric/music_195.lrc"
        },
        {
            "id": "194",
            "type": "sweet",
            "name": "好运来",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C1000003FEwa0lFHzk.m4a?fromtag=0",
            "lyricUrl": "lyric/music_194.lrc"
        },
        {
            "id": "193",
            "type": "sweet",
            "name": "jingle bells",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003KyC4f3dk0kf.m4a?fromtag=0",
            "lyricUrl": ""
        },
        {
            "id": "192",
            "type": "sweet",
            "name": "雪人",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000r8ihf4XMTQz.m4a?fromtag=0",
            "lyricUrl": ""
        },
        {
            "id": "191",
            "type": "sweet",
            "name": "铃儿响叮当",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002MDs9D297mKd.m4a?fromtag=0",
            "lyricUrl": ""
        },
        {
            "id": "190",
            "type": "sweet",
            "name": "千里之外",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003FRy0r0wyGHl.m4a?fromtag=0",
            "lyricUrl": "lyric/music_190.lrc"
        },
        {
            "id": "189",
            "type": "sweet",
            "name": "sant aclaus is coming to town",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001MDqWD2Qrl2T.m4a?fromtag=0",
            "lyricUrl": ""
        },
        {
            "id": "188",
            "type": "sweet",
            "name": "We Wish You A Merry Christmas ",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000lJNEQ08D5HD.m4a?fromtag=0",
            "lyricUrl": ""
        },

        {
            "id": "75",
            "type": "lonely",
            "name": "笑红尘",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001IazE54bpTz7.m4a?fromtag=0",
            "lyricUrl": "lyric/music_75.lrc"
        },
        {
            "id": "74",
            "type": "sweet",
            "name": "幸福感",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000laXtp4W6YU2.m4a?fromtag=0",
            "lyricUrl": "lyric/music_74.lrc"
        },
        {
            "id": "73",
            "type": "happy",
            "name": "玩腻",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001yaqrz0tIkfN.m4a?fromtag=0",
            "lyricUrl": "lyric/music_73.lrc"
        },
        {
            "id": "72",
            "type": "happy",
            "name": "小小贝壳",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C1000011AmO84HTNPu.m4a?fromtag=0",
            "lyricUrl": "lyric/music_72.lrc"
        },
        {
            "id": "71",
            "type": "quiet",
            "name": "回忆的沙漏",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100004TYbSN3tr1sd.m4a?fromtag=0",
            "lyricUrl": "lyric/music_71.lrc"
        },
        {
            "id": "70",
            "type": "quiet",
            "name": "夜曲",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001zMQr71F1Qo8.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "69",
            "type": "sweet",
            "name": "特别的爱给特别的你",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001JD1SR29d1hS.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "68",
            "type": "sweet",
            "name": "最浪漫的事",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C1000018QcSt0WosON.m4a?fromtag=0",
            "lyricUrl": "lyric/music_68.lrc"
        },
        {
            "id": "67",
            "type": "sweet",
            "name": "约定",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001Bv8v03LusX7.m4a?fromtag=0",
            "lyricUrl": "lyric/music_67.lrc"
        },
        {
            "id": "66",
            "type": "quiet",
            "name": "女人花",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000x65VD4BdGIQ.m4a?fromtag=0",
            "lyricUrl": "lyric/music_66.lrc"
        },
        {
            "id": "65",
            "type": "sweet",
            "name": "因为爱",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001db1Qb1vax0J.m4a?fromtag=0",
            "lyricUrl": "lyric/music_65.lrc"
        },
        {
            "id": "64",
            "type": "happy",
            "name": "开学了",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003Vi7qw4aCq4o.m4a?fromtag=0",
            "lyricUrl": "lyric/music_64.lrc"
        },
        {
            "id": "63",
            "type": "sweet",
            "name": "七夕",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100004YrWpR44shMm.m4a?fromtag=0",
            "lyricUrl": "lyric/music_63.lrc"
        },
        {
            "id": "62",
            "type": "relax",
            "name": "意大利灵魂慢摇曲",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001L8aVP0qpwtc.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "61",
            "type": "sweet",
            "name": "鹊桥汇",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002kXd7v0oCWAr.m4a?fromtag=0",
            "lyricUrl": "lyric/music_61.lrc"
        },
        {
            "id": "60",
            "type": "happy",
            "name": "童心未泯",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003zbUrB3I5OD5.m4a?fromtag=0",
            "lyricUrl": "lyric/music_60.lrc"
        },
        {
            "id": "59",
            "type": "sweet",
            "name": "暖暖",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003Sn9Rg4N3oNq.m4a?fromtag=0",
            "lyricUrl": "lyric/music_59.lrc"
        },
        {
            "id": "58",
            "type": "happy",
            "name": "Sexy Love",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002rZv4R0AQIlO.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "57",
            "type": "lonely",
            "name": "离别的秋天",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000pJ4WS2WAQcM.m4a?fromtag=0",
            "lyricUrl": "lyric/music_57.lrc"
        },
        {
            "id": "56",
            "type": "happy",
            "name": "Big Big World",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003AC4Vq2gG1XN.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "55",
            "type": "lonely",
            "name": "郁金香",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000e9Tiu4SiV3s.m4a?fromtag=0",
            "lyricUrl": "lyric/music_55.lrc"
        },
        {
            "id": "54",
            "type": "quiet",
            "name": "Summer Wine",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002nCjju0GWDbV.m4a?fromtag=0",
            "lyricUrl": "lyric/music_54.lrc"
        },
        {
            "id": "53",
            "type": "quiet",
            "name": "萤火",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100004DdzMX3NiIiL.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "52",
            "type": "sweet",
            "name": "爱，很简单",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001yZ7Tf0kudte.m4a?fromtag=0",
            "lyricUrl": "lyric/music_52.lrc"
        },
        {
            "id": "51",
            "type": "relax",
            "name": "新的心跳",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100004LHkGL1GVdZo.m4a?fromtag=0",
            "lyricUrl": "lyric/music_51.lrc"
        },
        {
            "id": "50",
            "type": "happy",
            "name": "虫儿飞",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100004TntDX3aSzNr.m4a?fromtag=0",
            "lyricUrl": "lyric/music_50.lrc"
        },
        {
            "id": "49",
            "type": "sweet",
            "name": "粉红色的回忆",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C1000003mXKU3KZ34F.m4a?fromtag=0",
            "lyricUrl": "lyric/music_49.lrc"
        },
        {
            "id": "48",
            "type": "lonely",
            "name": "因为爱情",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100004HdPmN0HZipA.m4a?fromtag=0",
            "lyricUrl": "lyric/music_48.lrc"
        },
        {
            "id": "47",
            "type": "lonely",
            "name": "栀子花开",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002tHK1K42Ajjo.m4a?fromtag=0",
            "lyricUrl": "lyric/music_47.lrc"
        },
        {
            "id": "46",
            "type": "quiet",
            "name": "蝴蝶泉边",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002K2oMf256F7j.m4a?fromtag=0",
            "lyricUrl": "lyric/music_46.lrc"
        },
        {
            "id": "45",
            "type": "happy",
            "name": "快乐童年",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002mmg554Y23LQ.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "44",
            "type": "relax",
            "name": "四季",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002ex7Ug3EZzVm.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "43",
            "type": "quiet",
            "name": "夏天的风",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C1000011HJEz1KxzDp.m4a?fromtag=0",
            "lyricUrl": "lyric/music_43.lrc"
        },
        {
            "id": "42",
            "type": "relax",
            "name": "星光",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003vNkp14ASF31.m4a?fromtag=0",
            "lyricUrl": "lyric/music_42.lrc"
        },
        {
            "id": "41",
            "type": "lonely",
            "name": "美好的时光",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001vvW412AzHQ3.m4a?fromtag=0",
            "lyricUrl": "lyric/music_41.lrc"
        },
        {
            "id": "40",
            "type": "happy",
            "name": "Again",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003JrYoV3NG6M8.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "39",
            "type": "quiet",
            "name": "Day dream",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001YGJzC10yluA.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "38",
            "type": "quiet",
            "name": "きっとまたいつか",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100004bffOW1ouAtc.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "37",
            "type": "happy",
            "name": "Flower dance",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003AepR40yJdm8.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "36",
            "type": "quiet",
            "name": "Love Theme",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002QLpqZ1kQ7U9.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "35",
            "type": "relax",
            "name": "Summer",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000wtbud2Xm0MT.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "34",
            "type": "quiet",
            "name": "ひとり",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C1000046rXGY0j7CZq.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "33",
            "type": "quiet",
            "name": "星际流浪",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C10000292vHZ1M99LR.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "32",
            "type": "relax",
            "name": "独一无二的朋友",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000E7NVI1BBJdU.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "31",
            "type": "happy",
            "name": "邻家的龙猫",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C1000031SmU11KKBwC.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "30",
            "type": "quiet",
            "name": "爱情雨",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002gJgMj49mbr5.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "29",
            "type": "relax",
            "name": "Always with me",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000H2wY40B7N1f.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "28",
            "type": "lonely",
            "name": "Love is",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C1000009KLIb4aQZ54.m4a?fromtag=0",
            "lyricUrl": null
        },

        {
            "id": "26",
            "type": "quiet",
            "name": "遇见",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001xJbdb2MBaaz.m4a?fromtag=0",
            "lyricUrl": "lyric/music_26.lrc"
        },
        {
            "id": "25",
            "type": "relax",
            "name": "With An Orchid",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003NTHtg31vxGL.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "24",
            "type": "lonely",
            "name": "千与千寻",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001MnnU24Y2lOw.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "23",
            "type": "quiet",
            "name": "Kiss The Rain",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001T5Ogt4F8lht.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "22",
            "type": "quiet",
            "name": "My soul",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C1000015xqSa3G50mK.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "21",
            "type": "lonely",
            "name": "千千阙歌",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000E8jPw26JFub.m4a?fromtag=0",
            "lyricUrl": null
        },

        {
            "id": "19",
            "type": "sweet",
            "name": "遇到",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003qTYEG1Pyq0M.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "18",
            "type": "quiet",
            "name": "夜空中最亮的星",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000r33x73Dri5q.m4a?fromtag=0",
            "lyricUrl": "lyric/music_18.lrc"
        },
        {
            "id": "17",
            "type": "happy",
            "name": "我相信",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003qKG2W4g6itJ.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "16",
            "type": "relax",
            "name": "曾经的你",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100004XcdPX08dOus.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "15",
            "type": "happy",
            "name": "青春纪念册",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C1000008yfgO0dmovi.m4a?fromtag=0",
            "lyricUrl": "lyric/music_15.lrc"
        },
        {
            "id": "14",
            "type": "relax",
            "name": "朋友仔",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003D4Spc0TwgQI.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "13",
            "type": "quiet",
            "name": "后会无期",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100004gZy7l1GYJ1Q.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "12",
            "type": "lonely",
            "name": "平凡之路",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000T1Ws32MWrUj.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "11",
            "type": "lonely",
            "name": "那些花儿",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001aF6Ng0dsLK5.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "10",
            "type": "relax",
            "name": "那些年",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100003WgIMf3cZfLm.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "9",
            "type": "sweet",
            "name": "好听",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001blMSP0K3WpH.m4a?fromtag=0",
            "lyricUrl": "lyric/music_9.lrc"
        },
        {
            "id": "8",
            "type": "relax",
            "name": "踮起脚尖爱",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002Y9Tks1fQTr3.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "7",
            "type": "relax",
            "name": "花开半夏",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002DOccg14Iyms.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "6",
            "type": "quiet",
            "name": "时间煮雨",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100002ysySy4eT0k6.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "5",
            "type": "quiet",
            "name": "知足",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C1000033P66R0qEtlT.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "4",
            "type": "lonely",
            "name": "醉相思",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C1000006IhBH1giHb0.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "3",
            "type": "lonely",
            "name": "一生最爱的是你",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000GZag14DvUDC.m4a?fromtag=0",
            "lyricUrl": "lyric/music_3.lrc"
        },
        {
            "id": "2",
            "type": "lonely",
            "name": "一曲红尘",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100001hefQQ1yXsez.m4a?fromtag=0",
            "lyricUrl": null
        },
        {
            "id": "1",
            "type": "quiet",
            "name": "再度重相逢",
            "musicUrl": "http://dl.stream.qqmusic.qq.com/C100000EK3pm0pDotN.m4a?fromtag=0",
            "lyricUrl": null
        }
    ]
}
''')

class Command(BaseCommand):
    def handle(self, *args, **options):
        music_tags = []
        for tag  in tag_mapping.values():
            music_tags.append(MusicTag(
                id=tag['id'],
                name=tag['name'],
            ))
        MusicTag.objects.bulk_create(music_tags)

        music_list = music_info['musicList']
        music_list.reverse()

        musics = []
        music_mapping = {}
        for i, music_data in enumerate(music_list):
            music_id = i + 1
            music = Music(
                id=music_id,
                name=music_data['name'],
                url=music_data['musicUrl'],
                lyric_url=music_data['lyricUrl'] or '',
            )
            musics.append(music)
            music_mapping[music_id] = music
        Music.objects.bulk_create(musics, 50)

        for i, music_data in enumerate(music_list):
            music_id = i + 1
            music = music_mapping[music_id]
            music.tags.add(tag_mapping[music_data['type']]['id'])
