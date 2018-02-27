# coding:utf8
"""
--------------------------------------------------------------------------
    File:   score_it.py
    Auth:   zsdostar
    Date:   2018/2/28 3:03
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   
--------------------------------------------------------------------------
"""

import jieba
import jieba.posseg as psg
import pymysql
from collections import Counter
import sys

# with open ('keywords','r') as f:
#     content = f.read().decode('utf8')
# KEY_WORD = content.split()
KEY_WORD = (u'技术',u'物联网',u'发展',u'智能',u'中国',u'市场',u'行业',u'企业',u'全球',u'智慧',u'人工智能',u'城市',u'数据',u'领域',u'服务',u'公司',u'互联网',u'近日',u'科技',u'机器人',u'产业',u'用户',u'产品',u'平台',u'网络',u'未来',u'国家',u'手机',u'正式',u'移动',u'设备',u'合作',u'消息',u'工业',u'物流',u'北京',u'无人',u'建设',u'汽车',u'重要',u'滴滴',u'单车',u'零售',u'美国',u'经济',u'报告',u'AI',u'系统',u'智能家居',u'世界',u'业务',u'自动',u'人们',u'正在',u'时代',u'战略',u'目前',u'我们',u'信息',u'我国',u'国内',u'春节',u'交通',u'安全',u'消费',u'问题',u'今年',u'生活',u'CES',u'时间',u'社会',u'集团',u'规模',u'阿里',u'品牌',u'功能',u'工作',u'苹果',u'预计',u'京东',u'运营商',u'数字',u'全国',u'研究',u'主要',u'通信',u'商用',u'这些',u'方式',u'研发',u'传感器',u'日前',u'计划',u'巨头',u'方面',u'最大',u'IoT',u'有限公司',u'传统',u'大会',u'亚马逊',u'这个',u'体验',u'百度',u'国际',u'今天',u'阿里巴巴',u'机器',u'期间',u'模式',u'项目',u'管理',u'现在',u'消费者',u'测试',u'人类',u'协议',u'去年',u'无人机',u'芯片',u'上线',u'上海',u'解决方案',u'电商',u'巨大',u'微信',u'其中',u'华为',u'机构',u'支付宝',u'苏宁',u'电子',u'全面',u'投资',u'区块',u'视频',u'影响',u'智能手机',u'趋势',u'智能化',u'自己',u'谷歌',u'今日',u'预测',u'ofo',u'持续',u'春运',u'腾讯',u'场景',u'政策',u'运营',u'以下',u'转型',u'融合',u'过去',u'概念',u'重点',u'分析',u'厂商',u'中心',u'记者',u'近年来',u'同比',u'这一',u'美团',u'之一',u'能力',u'终端',u'升级',u'软件',u'人脸识别',u'媒体',u'年度',u'货架',u'标准',u'突破',u'内容',u'日本',u'优势',u'司机',u'基础',u'之后',u'联网',u'如今',u'综合',u'来说',u'硬件',u'主题',u'以来',u'音箱',u'变革',u'商品',u'利用',u'他们',u'家庭',u'最近',u'无人驾驶',u'制造业',u'深圳',u'竞争',u'整个',u'启动',u'摩拜',u'外媒',u'试点',u'旅客',u'部分',u'ETC',u'信息化',u'成功',u'商业',u'CEO',u'之间',u'资源',u'活动',u'乘客',u'范围',u'目标',u'发布会',u'不同',u'自动化',u'专利',u'成本',u'专家',u'如何',u'资本',u'APP',u'生产',u'部署',u'杭州',u'这样',u'速度',u'深度',u'研究院',u'教育',u'空间',u'环境',u'此次',u'监测',u'飞机',u'大家',u'政府',u'布局',u'旗下',u'半导体',u'电信',u'重大',u'所有',u'落地',u'NB',u'设计',u'协会',u'融资',u'韩国',u'关系',u'规划',u'地区',u'音乐',u'新一轮',u'车辆',u'论坛',u'三大',u'高通',u'团队',u'基本',u'三星',u'会议',u'情况',u'过程',u'积极',u'方向',u'核心',u'人员',u'实体',u'主办',u'迅速',u'交通运输',u'官方',u'生态',u'变化',u'双方',u'方案',u'工信部',u'语音',u'信息技术',u'优化',u'试验',u'印度',u'成都',u'代表',u'年底',u'高速公路',u'大型',u'产生',u'当地',u'标志',u'广泛',u'文件',u'领先',u'背后',u'新一代',u'无法',u'以上',u'新型',u'调整',u'风险',u'数据中心',u'部门',u'体系',u'IT',u'哪些',u'新闻',u'扫码',u'网约车',u'各种',u'习惯',u'那么',u'指导',u'其他',u'阶段',u'出租车',u'销售',u'网站',u'股份',u'数量',u'新兴',u'英国',u'价格',u'此前',u'微软',u'健康',u'比特',u'价值',u'拉斯维加斯',u'这种',u'市民',u'挑战',u'小蓝',u'水平',u'风口',u'医疗',u'事件',u'近期',u'时候',u'人民币',u'监控',u'万物',u'当前',u'质量',u'大脑',u'金融',u'董事长',u'家电',u'成熟',u'现实',u'社区',u'顺丰',u'便利',u'本次',u'物联',u'小米',u'印发',u'个人',u'线下',u'业界',u'机场',u'同期',u'效率',u'普及',u'委员会',u'网络安全',u'下面',u'生物',u'之前',u'天猫',u'便捷',u'App',u'WiFi',u'经历',u'数字化',u'货币',u'创业',u'高效',u'整体',u'图像',u'现金',u'因素',u'峰会',u'意见',u'有关',u'供应链',u'上市',u'便利店',u'黄车',u'昨日',u'加密',u'热潮',u'创始人',u'流量',u'二维码',u'什么',u'西安',u'发展趋势',u'iPhone',u'联盟',u'任务',u'它们',u'万达',u'视觉',u'排队',u'公共',u'对外',u'购物',u'基础设施',u'检测',u'跨境',u'工业革命',u'当下',u'内部',u'总部',u'知识产权',u'来看',u'边缘',u'Apple',u'机会',u'亮相',u'广州',u'全资',u'农业',u'铁路',u'Amazon',u'欧洲',u'在线',u'天津',u'制造商',u'关键',u'各国',u'话题',u'摄像头',u'算法',u'新能源',u'之外',u'公交',u'完全',u'德国',u'动力',u'公告',u'月份',u'家居',u'下午',u'产业链',u'一样',u'全部',u'网上',u'达沃斯',u'直接',u'强国',u'ON',u'有人',u'信用',u'最后',u'车主',u'性能',u'北斗',u'指纹',u'观众',u'供应商',u'意义',u'调查',u'顾客',u'难题',u'孩子',u'合作伙伴',u'重庆',u'专业',u'高端',u'会上',u'世纪',u'文章',u'电子展',u'直播',u'道路',u'电子商务',u'压力',u'市场份额',u'革命',u'助力',u'指南',u'首席',u'身份',u'手表',u'中国联通',u'入局',u'艾瑞',u'地铁',u'媒体报道',u'昨天',u'股价',u'民用',u'量子',u'MWC',u'协同',u'苹果公司',u'IDC',u'发改委',u'监管',u'机遇',u'新年',u'程度',u'商店',u'游戏',u'银行',u'大量',u'免费',u'力量',u'这项',u'形式',u'浪潮',u'中国移动',u'组成部分',u'渠道',u'蚂蚁',u'存储',u'计算机',u'晚间',u'人口',u'总量',u'窄带',u'明确',u'押金',u'精准',u'背景',u'在内',u'资金',u'大众',u'这场',u'力度',u'业态',u'细分',u'年会',u'网友',u'所谓',u'公里',u'PC',u'大幕',u'有些',u'中通',u'居民',u'入口',u'主流',u'科学技术',u'无线',u'指数',u'负责人',u'措施',u'结账',u'进站',u'顺风',u'热点',u'格局',u'公众',u'程序',u'驱动',u'手段',u'电子设备',u'优秀',u'福建',u'春节假期',u'实际',u'公开',u'规定',u'国外',u'架构',u'事业部',u'复杂',u'详情',u'Go',u'全省',u'自身',u'附近',u'每个',u'现场',u'购票',u'国内外',u'潜力',u'许可',u'分析师',u'黄金',u'社交',u'人士',u'超级',u'淘宝',u'领导',u'交易',u'科学家',u'方便',u'改革',u'名称',u'大规模',u'规范',u'容易',u'Waymo',u'等等',u'Google',u'威胁',u'先进',u'车牌',u'版本',u'这家',u'明显',u'名单',u'总体',u'尝试',u'状态',u'电脑',u'五大',u'金服',u'数据分析',u'助手',u'网易',u'S9',u'良好',u'现象',u'农村',u'深化',u'第三阶段',u'冬奥会',u'运输',u'简单',u'人民',u'副总裁',u'手术',u'诺基亚',u'结果',u'地位',u'总经理',u'钱包',u'商家',u'单位',u'电池',u'人才',u'运用',u'补贴',u'各行各业',u'账户',u'云鸟',u'公寓',u'商业模式',u'工程',u'英特尔',u'以后',u'物理',u'季度',u'航班',u'环保',u'面向',u'富士康',u'小区',u'历史',u'最高',u'应用领域',u'北京市',u'类型',u'咨询',u'电影',u'广泛应用',u'法律',u'安全性',u'AR',u'灵活',u'电网',u'首款',u'关键词',u'实力',u'电视',u'仪式',u'轻松',u'激烈',u'文化',u'哪里',u'中国电信',u'网民',u'联发科',u'当今',u'技术创新',u'路灯',u'标准化',u'美元',u'应急',u'便携式',u'涨幅',u'各个',u'IBM',u'定义',u'南京',u'一切',u'不足',u'以色列',u'江苏',u'客户',u'下一代',u'返程',u'场所',u'影响力',u'行动',u'城市交通',u'模型',u'跨界',u'市值',u'重磅',u'评估',u'旅途',u'现有',u'牌照',u'代号',u'系列',u'往往',u'Galaxy',u'诈骗',u'小时',u'近几年',u'部长',u'总裁',u'车载',u'酒店',u'卫星',u'电子产品',u'商户',u'医院',u'人工',u'前景',u'增长率',u'商机',u'很大',u'代码',u'考拉',u'空调',u'家中',u'每年',u'潮流',u'蓬勃发展',u'平安',u'份额',u'有力',u'连续',u'令人',u'策略',u'信号',u'上年',u'快捷',u'平均',u'周三',u'盘点',u'差距',u'申通',u'总结',u'热度',u'通信业',u'年代',u'投入使用',u'高铁',u'革命性',u'区域',u'Uber',u'各方',u'文明',u'宁波',u'回家',u'机上',u'节目',u'日程',u'五年',u'香港',u'周期',u'业内',u'松下',u'投资者',u'联通',u'Global',u'本身',u'典型',u'蜂窝',u'之中',u'之下',u'官网',u'日益',u'微波炉',u'PED',u'年轻人',u'人脸',u'基站',u'海外',u'反应',u'S8',u'服务平台',u'一大',u'态势',u'空中',u'上海市',u'硅谷',u'亚洲',u'巴塞罗那',u'当天',u'今后',u'商务',u'上午',u'月初',u'想象',u'VR',u'红包',u'成员',u'方法',u'周边',u'安森美',u'货物',u'决策',u'普通',u'ET',u'青桔',u'这里',u'子公司',u'任何',u'通行',u'高科技',u'Pay',u'眼镜',u'高度',u'较大',u'案例',u'Mobile',u'国务院',u'Research',u'战略性',u'每天',u'电器',u'之际',u'事实上',u'朋友圈',u'陕西',u'盛典',u'门店',u'时刻',u'高级',u'俄罗斯',u'销售额',u'各自',u'航空公司',u'帷幕',u'渗透到',u'岗位',u'挖矿',u'目光',u'进口',u'年初',u'能源',u'全世界',u'新鲜',u'强劲',u'巴西',u'美的',u'大城市',u'奇点',u'高峰论坛',u'层出不穷',u'比重',u'母公司',u'资讯',u'菜鸟',u'医生',u'开业',u'状况',u'步伐',u'交易所',u'培育',u'发布公告',u'节点',u'竞争力',u'矛盾',u'事业',u'头条',u'混合',u'OPPO',u'乡村',u'上市公司',u'纳斯达克',u'AGV',u'Azure',u'频段',u'预期',u'众所周知',u'制高点',u'安卓',u'丰富',u'供电',u'庞大',u'曝光',u'各地',u'依旧',u'全程',u'笔者',u'特色',u'唯一',u'过年',u'现代化',u'最好',u'充分',u'其它',u'年末',u'云商',u'管理局',u'中关村',u'有效',u'频繁',u'财经',u'展览会',u'招聘会',u'裁员',u'IPv6',u'无线通信',u'乐视',u'机械',u'玩家',u'服务器',u'爆发式',u'新品',u'网络攻击',u'线路',u'深圳市',u'房地产',u'本土',u'建设项目',u'下半年',u'O2O',u'替代',u'铁塔',u'动作',u'联系',u'去年同期',u'每日',u'无锡',u'月底',u'现状',u'先后',u'门槛',u'国人',u'大赛',u'个人信息',u'以前',u'重新',u'火热',u'重构',u'通讯',u'上路',u'广阔',u'公安',u'金额',u'特点',u'显著',u'致力于',u'数码',u'高峰',u'提供商',u'董事',u'小店',u'两大',u'河北',u'单日',u'东西',u'城市规划',u'证券',u'海信',u'意法',u'荣获',u'国际标准',u'娱乐',u'新版',u'瑞士',u'保险',u'澳洲',u'RFID',u'布线',u'普遍',u'积分',u'证实',u'掌控',u'浙江',u'航空',u'现代',u'创新型',u'银行卡',u'完整',u'工具',u'Semiconductor',u'成果',u'电动',u'交流',u'高管',u'车队',u'委员',u'盛大举行',u'公路',u'停车场',u'Alphabet',u'强大',u'智能网',u'产值',u'年前',u'动能',u'研讨会',u'主任',u'Facebook',u'爱尔兰',u'第三季度',u'近两年',u'年内',u'维度',u'BAT',u'民众',u'分钟',u'玩法',u'传输',u'业绩',u'总数',u'争相',u'目录',u'大事',u'科学',u'里程',u'周一',u'稳定',u'上周',u'能效',u'NR',u'猎鹰',u'检验',u'短距离',u'春运期间',u'估值',u'早期',u'常见',u'那些',u'零售店',u'广大',u'谈论',u'大奖',u'世界各地',u'李彦宏',u'本质',u'大战',u'收盘',u'平稳',u'第四季度',u'突然',u'备忘录',u'共识',u'美好生活',u'银联',u'QQ',u'额度',u'目的',u'元年',u'造车',u'爱立信',u'当中',u'奖励',u'物流业',u'每股',u'版图',u'乘车',u'愿景',u'历程',u'前所未有',u'索尼',u'强烈',u'电话',u'外界',u'电讯',u'拉开序幕',u'方方面面',u'国家知识产权局',u'各位',u'ST',u'有所',u'门锁',u'应运而生',u'出货量',u'贡献',u'那样',u'监督',u'十大',u'研究所',u'统计数据',u'彻底改变',u'风潮',u'民生',u'AT',u'页面',u'进程',u'具体',u'魔镜',u'信息安全',u'除夕',u'便捷性',u'费用',u'楼宇',u'流程',u'服务商',u'李开复',u'时段',u'商城',u'结构',u'熊瑛',u'网购',u'特性',u'心情',u'马来西亚',u'人数',u'ISO',u'客流',u'阜平县',u'新建',u'原因',u'显然',u'配套',u'民警',u'低功耗',u'无线电',u'本届',u'路线',u'NFC',u'设置',u'以往',u'逻辑',u'严重',u'辅助',u'吉隆坡',u'引擎',u'宽带用户',u'步步高',u'执行官',u'努力',u'业内人士',u'此举',u'行人',u'广东',u'一方面',u'调研',u'乐趣',u'天合光',u'湖北',u'湖南',u'植入',u'女神',u'法国',u'西雅图',u'博士',u'地图',u'新华社',u'河南',u'新年伊始',u'往年',u'漏洞',u'答案',u'光缆',u'动态',u'会员',u'澳大利亚',u'冬天',u'潜在',u'员工',u'防控',u'地方',u'重塑',u'屏幕',u'中控',u'高潮',u'中科院',u'春晚',u'销量',u'钥匙',u'余额',u'关注度',u'工厂',u'利好',u'接下来',u'央行',u'海底',u'收银台',u'海尔',u'权威',u'理论',u'如下',u'远程',u'面前',u'初创',u'嘉宾',u'土豆',u'盛大',u'美国公司',u'资料',u'该项',u'阵营',u'饮水',u'什么样',u'日子',u'全自动',u'ru',u'群体',u'Qualcomm',u'群众',u'意识',u'全力',u'当日',u'思想',u'科勒',u'Brenda',u'北上',u'一卡通',u'脚步',u'消费类',u'贾跃亭',u'父母',u'这份',u'隧道',u'动车',u'列车',u'贸促会',u'势头',u'EMS',u'旅游',u'朋友',u'安检员',u'极大',u'新风',u'赛道',u'故事',u'套餐',u'Gartner',u'参展商',u'航空航天',u'年头',u'非洲',u'异地',u'开发商',u'大厦',u'北大',u'全美',u'加州',u'车站',u'伦敦',u'零售商',u'养老',u'福建省',u'比赛',u'痛点',u'Brands',u'怎样',u'迅猛发展',u'界面',u'博通',u'搅局',u'网络科技',u'天下',u'互通',u'闯红灯',u'学生',u'石油',u'效果',u'主动',u'新车',u'Store',u'年三十',u'大大',u'版权',u'边界',u'iPad',u'所有人',u'空气质量',u'元旦',u'文投',u'根本',u'近来',u'贸易',u'独家',u'虚假',u'经济社会',u'釜山',u'定位',u'Alexa',u'CIO',u'条件',u'厦门',u'CES2018',u'Home',u'力争',u'印象',u'阿联酋',u'行动计划',u'效应',u'眼睛',u'各家',u'颁奖典礼',u'Spotify',u'伟达',u'土地',u'日益增长',u'天气',u'明年',u'软硬件',u'家里',u'排行榜',u'蓄势待发',u'革新',u'助推',u'机票',u'防不胜防',u'最多',u'障碍',u'这次',u'这款',u'供给',u'火车',u'无界',u'虹膜',u'大潮',u'有史以来',u'山东',u'消防安全',u'国家级',u'物品',u'新华书店',u'自家',u'维权',u'腾飞',u'日常生活',u'训练',u'宣传',u'步入',u'一夜之间',u'股东',u'竞争对手',u'工程师',u'身影',u'期限',u'直升机',u'中共中央国务院',u'初期',u'发展潜力',u'有趣',u'假期',u'安全感',u'路段',u'宽带',u'三者',u'报警',u'凸显',u'专项',u'海量',u'总和',u'不断涌现',u'一共',u'社保卡',u'Verizon',u'绿色',u'感觉',u'平昌',u'BG',u'之家',u'模块',u'IDG',u'开户',u'车型',u'标签',u'客服',u'下半场',u'所在',u'每次',u'营收',u'队伍',u'固定',u'生鲜',u'热词',u'住宅',u'电动汽车',u'货箱',u'领导者',u'商场',u'新区',u'细节',u'网络通信',u'本周',u'口号',u'红利',u'副县长',u'从业人员',u'危机',u'市场前景',u'统一',u'寂静',u'设施',u'桥梁',u'一年一度',u'温州',u'Wi',u'移动机器人',u'红外',u'家用',u'评价',u'航天',u'图片',u'办法',u'该国',u'每月',u'源代码',u'面板',u'伊始',u'预警',u'奢侈品',u'火爆',u'疯狂',u'复活',u'彻底',u'马云',u'福州',u'公平',u'整理',u'为什么',u'确实',u'资产',u'大陆',u'发明专利',u'郭台铭',u'级别',u'佣金',u'长江大桥',u'迪拜',u'中央',u'目的地',u'中国人民银行',u'师傅',u'体会',u'Fi',u'不甘落后',u'顶层',u'评审',u'顶尖',u'四川',u'增幅',u'原则',u'前不久',u'热门',u'特拉维夫',u'收费',u'针对性',u'理念',u'年货',u'虚拟现实',u'高德',u'隆重',u'中兴',u'战场',u'工业化',u'实验室',u'台湾',u'模糊',u'青岛',u'舒适',u'应用软件',u'消费市场',u'西班牙',u'轨道交通',u'同行',u'iOS',u'武汉',u'中标',u'Echo',u'联想集团',u'一般',u'跨城',u'话语权',u'东航',u'市面上',u'济南',u'下单',u'商米',u'航空局',u'发票',u'骁龙',u'席卷',u'工信',u'石墨',u'南非',u'文学',u'垃圾桶',u'自营',u'救援',u'ICT',u'据介绍',u'戒指',u'Top',u'陶瓷',u'合资',u'服装',u'合格',u'顺利',u'合资企业',u'领军',u'风向标',u'地铁站',u'工场',u'女儿',u'不可避免',u'央视',u'装置',u'总额',u'胃镜',u'圆通')


def exam(s):
    score = 0.0
    if (u'？' in s) or (u'?' in s) or (u'...' in s) or (u'…' in s) or (u' 本报' in s):
        return -1
    data = [x for x in jieba.cut(s)]
    data = list(set(data))  # list去重
    for i in data:
        if i in KEY_WORD[:40]:
            score += 10
        elif i in KEY_WORD[40:100]:
            score += 8
        elif i in KEY_WORD[100:200]:
            score += 3
        elif i in KEY_WORD[200:600]:
            score += 2
        elif i in KEY_WORD[600:]:
            score += 1
    if 45<len(s)<65:
        score *= (65.0/len(s))
    print score,
    return score

# print exam(s1),exam(s2),exam(s3)

'''
1-40:5
41-100:4
101-200:3
201-600:2
601-1500:1
1501-3000:0.5
'''