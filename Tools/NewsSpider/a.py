# coding:utf8
"""
--------------------------------------------------------------------------
    File:   a.py
    Auth:   zsdostar
    Date:   2018/2/22 19:57
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   提取一句完整的话
--------------------------------------------------------------------------
"""
import re

u = u'据工信部公布的《2017年通信业统计公报》显示，初步核算，2017年我国电信业务总量达到27557亿元（按照2015年不变单价计算），比上年增长76．4％，增幅同比提高42．5个百分点。电信业务收入12620亿元，比上年增长6．4％，增速同比提高1个百分点。2012－2017年固定通信和移动通信收入占比变化情况在电信业务收入中，全年固定通信业务收入完成3549亿元，比上年增长8．4％。移动通信业务实现收入9071亿元，比上年增长5．7％，在电信业务收入中占比为71．9％，较上年回落0．5个百分点。在固定通信业务中，2017年固定数据及互联网业务收入达到1971亿元，比上年增长9．5％，在电信业务收入中占比由上年的15．2％提升到15．6％，拉动电信业务收入增长1．4个百分点，对全行业业务收入增长贡献率达21．9％。受益于光纤接入速率大幅提升，家庭智能网关、视频通话、IPTV等融合服务加快发展。全年IPTV业务收入121亿元，比上年增长32．1％；物联网业务收入比上年大幅增长86％。2017年，在移动通信业务中移动数据及互联网业务收入5489亿元，比上年增长26．7％，在电信业务收入中占比从上年的38．1％提高到43．5％，对收入增长贡献率达152．1％。随着高速互联网接入服务发展和移动数据流量消费快速上升，话音业务（包括固定话音和移动话音）继续呈现大幅萎缩态势。2017年完成话音业务收入2212亿元，比上年下降33．5％，在电信业务收入中的占比降至17．5％，比上年下降7．3个百分点。'
u = u[:160]

print re.search(u'.+\u3002', u).group()